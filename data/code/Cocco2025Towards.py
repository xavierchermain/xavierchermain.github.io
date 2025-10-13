'''
MIT License

Copyright (c) 2025 Giovanni Cocco and Inria

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

'''
This file provides a reference implementation of the kinematics. See the end of the file for a usage example.

Note: RepRap firmware does not allow negative machine axis values. In non-planar printing, the values of z0, z1, or z2 may become negative, but the firmware clamps these values, resulting in incorrect bed positioning. This issue can be resolved by offsetting the machine's z-axes origin using the G-code command G92.
'''

import numpy as np

def Kinematic(ball_0_position, ball_1_position, ball_2_position, balls_z_position, slot_0_angle, slot_1_angle, slot_2_angle):
	"""
	Return a kinematic object initialized with the given machine parameters.

	Parameters:
		ball_0_position (2 components 1D numpy array): X-Y position of the first ball in bed-space.
			Equivalent to the X and Y machine coordinates to have the nozzle at the center of the ball during planar printing.
		ball_1_position (2 components 1D numpy array): X-Y position of the second ball in bed-space.
		ball_2_position (2 components 1D numpy array): X-Y position of the third ball in bed-space.
		balls_z_position (scalar): Z position of the balls in bed-space.
			Equivalent to either the negative distance from the top of the bed to the center of the balls or the Z machine coordinate to have the nozzle at the center of the balls during planar printing.
		slot_0_angle (scalar): Angle in degrees of the first rail with respect to the machine X-axis.
			Measured counterclockwise when viewed from above.
		slot_1_angle (scalar): Angle in degrees of the second rail with respect to the machine X-axis.
		slot_2_angle (scalar): Angle in degrees of the third rail with respect to the machine X-axis.

	Returns:
		Kinematic: Kinematic object exposing 'forward' and 'inverse' methods as described below.

		inverse(position, orientation):
			Return the machine coordinates given a tool position and orientation.
			Parameters:
				position (3 components 1D numpy array): Tool position in bed-space.
				orientation (3 components 1D numpy array): Tool orientation in bed-space, given as a unit vector in the upper hemisphere (e.g., for planar printing, (0, 0, 1)).
			Returns:
				x, y, z0, z1, z2 (5 components 1D numpy array): Machine coordinates corresponding to the given position and orientation.

		forward(x, y, z0, z1, z2):
			Return the tool position and orientation given the machine coordinates.
			Parameters:
				x, y, z0, z1, z2: Machine coordinates.
			Returns:
				position (3 components 1D numpy array): Tool position in bed-space.
				orientation (3 components 1D numpy array): Tool orientation in bed-space.
	"""

	# Initialize the constraints (Eq. 3) and constants for the inverse kinematics
	slot_0_normal = np.array((-np.sin(np.radians(slot_0_angle)), np.cos(np.radians(slot_0_angle))))
	slot_1_normal = np.array((-np.sin(np.radians(slot_1_angle)), np.cos(np.radians(slot_1_angle))))
	slot_2_normal = np.array((-np.sin(np.radians(slot_2_angle)), np.cos(np.radians(slot_2_angle))))
	constraint_0 = np.array((*slot_0_normal, 0, 0))
	constraint_1 = np.array((*slot_1_normal, 0, -np.dot(ball_1_position-ball_0_position, slot_1_normal)))
	constraint_2 = np.array((*slot_2_normal, 0, -np.dot(ball_2_position-ball_0_position, slot_2_normal)))
	l1 = ball_1_position - ball_0_position
	l2 = ball_2_position - ball_0_position
	l1_rot = np.array((-l1[1], l1[0]))
	l2_rot = np.array((-l2[1], l2[0]))
	ball_0_3d_position = np.array((ball_0_position[0], ball_0_position[1], balls_z_position))

	# Initialize the additional constants for the forward kinematics
	slot_0_direction = np.array((-slot_0_normal[1], slot_0_normal[0]))
	s0d_s1n = np.dot(slot_0_direction, slot_1_normal)
	s0d_s2n = np.dot(slot_0_direction, slot_2_normal)
	Cf = np.dot(constraint_2[-1]*slot_1_normal-constraint_1[-1]*slot_2_normal, slot_0_direction)
	
	def normalize(v):
		return v/np.linalg.norm(v)
	
	def solve_weierstrass(A, B, C):
		# Solve A*cos(x) + B*sin(x) + C = 0 and return the solution with the smallest absolute value (Eq. 11)
		return 0 if A + C == 0 else 2*np.arctan((C + A)/(-B - np.sign(B)*np.sqrt(B**2 + (A + C)*(A - C))))
	
	def rotate(vector, axis, angle):
		return vector*np.cos(angle) + np.cross(axis, vector)*np.sin(angle)+axis*np.dot(axis, vector)*(1-np.cos(angle))

	def get_angle_to_match_z(vector, axis, target_z):
		# Solve for the angle (Eq. 18)
		C = axis[2]*np.dot(vector, axis)
		A = vector[2]-C
		C -= target_z
		B = np.cross(axis, vector)[2]
		return solve_weierstrass(A, B, C)
	
	def inverse(position, orientation):
		# Define the tangent space (Eq. 4)
		normal = normalize(np.array((-orientation[0], -orientation[1], orientation[2])))
		bitanget = normalize(np.cross(normal, np.array((1, 0, 0))))
		tangent = normalize(np.cross(bitanget, normal))
		TBN = np.array((tangent, bitanget, normal))

		# Initialize the 2D line constraints (Eq. 5)
		n0 = (TBN @ constraint_0[:-1])[:-1]
		n1 = (TBN @ constraint_1[:-1])[:-1]
		k1 = constraint_1[-1]
		n2 = (TBN @ constraint_2[:-1])[:-1]
		k2 = constraint_2[-1]

		# Solve for theta and t (Eqs. 8 and 9)
		d = np.array((-n0[1], n0[0]))
		d_n1 = np.dot(d, n1)
		d_n2 = np.dot(d, n2)
		l1_n1 = np.dot(l1, n1)
		l1_rot_n1 = np.dot(l1_rot, n1)
		A = d_n1*np.dot(l2, n2) - d_n2*l1_n1
		B = d_n1*np.dot(l2_rot, n2) - d_n2*l1_rot_n1
		C = np.dot(k2*n1 - k1*n2, d)
		theta = solve_weierstrass(A, B, C)
		ct = np.cos(theta)
		st = np.sin(theta)
		t = -(l1_n1*ct + l1_rot_n1*st + k1)/d_n1

		# Compute the ball 0 position and the deltas in Z (Eq. 12)
		b0_2d = t*d
		R = np.array(((ct, -st), (st, ct)))
		R_3d = np.array(((R[0][0], R[0][1], 0), (R[1][0], R[1][1], 0), (0, 0, 1)))
		b1_2d = b0_2d + R @ l1
		b2_2d = b0_2d + R @ l2
		TBN_T = TBN.T
		b0 = TBN_T @ np.array((*b0_2d, 0))
		Z = TBN_T[2]
		b1_z = np.dot(Z, np.array((*b1_2d, 0)))
		b2_z = np.dot(Z, np.array((*b2_2d, 0)))
		delta_z1 = b1_z - b0[2]
		delta_z2 = b2_z - b0[2]

		# Apply the transform and return the machine coordinates (Eqs. 14 and 15)
		pos = TBN_T @ R_3d @ (position - ball_0_3d_position) + ball_0_3d_position
		return pos[0] + b0[0], pos[1] + b0[1], pos[2], pos[2]-delta_z1, pos[2]-delta_z2

	def forward(x, y, z0, z1, z2):
		# Solve for the rotation to match the Z values (Eqs. 16 and 17)
		vector1 = np.array((*l1, 0))
		axis1 = normalize(np.array((-l1[1], l1[0], 0)))
		angle1 = get_angle_to_match_z(vector1, axis1, z0-z1)

		vector2 = rotate(np.array((*l2, 0)), axis1, angle1)
		vector1 = rotate(vector1, axis1, angle1)
		axis2 = normalize(vector1)
		angle2 = get_angle_to_match_z(vector2, axis2, z0-z2)

		# Get l1' and l2' (Eq. 20)
		l1p = rotate(vector1, axis2, angle2)[0:2]
		l2p = rotate(vector2, axis2, angle2)[0:2]
		l1p_rot = np.array((-l1p[1], l1p[0]))
		l2p_rot = np.array((-l2p[1], l2p[0]))

		# Solve for theta and t (Eqs. 21 and 22)
		l1_n1 = np.dot(l1p, slot_1_normal)
		l1_rot_n1 = np.dot(l1p_rot, slot_1_normal)
		A = s0d_s1n*np.dot(l2p, slot_2_normal) - s0d_s2n*l1_n1
		B = s0d_s1n*np.dot(l2p_rot, slot_2_normal) - s0d_s2n*l1_rot_n1
		theta = solve_weierstrass(A, B, Cf)
		t = -(l1_n1*np.cos(theta) + l1_rot_n1*np.sin(theta) + constraint_1[-1])/s0d_s1n
		b0 = t*slot_0_direction

		# Get the orientation (Eq. 23)
		up = np.array((0, 0, 1))
		normal = rotate(rotate(rotate(up, axis1, angle1), axis2, angle2), up, theta)
		orientation = np.array((-normal[0], -normal[1], normal[2]))

		# Get the position (Eq. 23)
		pos = np.array((x-b0[0], y-b0[1], z0)) - ball_0_3d_position
		position = rotate(rotate(rotate(pos, up, -theta), axis2, -angle2), axis1, -angle1) + ball_0_3d_position

		return position, orientation

	# Return a kinematic object
	return type('Kinematic', (), {'inverse': lambda *x: inverse(*x[1:]), 'forward': lambda *x: forward(*x[1:])})()


'''
Usage example
'''
if __name__ == '__main__':
	# Initialize a kinematic object with the machine parameters
	kinematic = Kinematic(np.array((-4.07, -12.16)), np.array((304.93, -12.16)), np.array((150.43, 296.84)), -45.7, 29.89, 150.11, -90)

	# Define the target tool position in bed-space
	position = np.array((150, 150, 20))

	# Define the target tool orientation in bed-space
	theta, phi = np.deg2rad(20), np.deg2rad(45)
	orientation = np.array((np.cos(phi)*np.sin(theta), np.sin(phi)*np.sin(theta), np.cos(theta)))

	# Get the machine coordinates using the inverse kinematics
	x, y, z0, z1, z2 = kinematic.inverse(position, orientation)

	# Get the position and orientation back using the forward kinematics
	pos, orient = kinematic.forward(x, y, z0, z1, z2)

	# Print the computed values
	print(f'Inverse kinematics: ([{position[0]:.4f}, {position[1]:.4f}, {position[2]:.4f}], [{orientation[0]:.4f}, {orientation[1]:.4f}, {orientation[2]:.4f}]) -> ({x:.4f}, {y:.4f}, {z0:.4f}, {z1:.4f}, {z2:.4f})\nForward kinematics: ({x:.4f}, {y:.4f}, {z0:.4f}, {z1:.4f}, {z2:.4f}) -> ([{pos[0]:.4f}, {pos[1]:.4f}, {pos[2]:.4f}], [{orient[0]:.4f}, {orient[1]:.4f}, {orient[2]:.4f}])')
