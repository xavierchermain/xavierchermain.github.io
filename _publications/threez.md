---
layout: publication
title: Towards Accessible Non-Planar FFF Using Triple Z-Axis Kinematics
authors: <a href="https://github.com/iota97">Giovanni Cocco</a>, Eric Garner, Vincent Belle, <a href="https://members.loria.fr/CZanni/">Cédric Zanni</a>, <b>Xavier Chermain</b>
journal: Proceedings of the ACM Symposium on Computational Fabrication
year: 2025
article: https://xavierchermain.github.io/data/pdf/Cocco2025Towards.pdf
supplementary_video: https://youtu.be/A3cuJ4mAvRI
code: https://xavierchermain.github.io/data/code/Cocco2025Towards.py
id_name: Cocco2025Towards
doi: https://doi.org/10.1145/3745778.3766652
id_number: 10
---
{% include math.html %}

## Abstract

We present a novel approach to non-planar fused filament fabrication (FFF) aimed at making this advanced technique more accessible to the maker and research communities. By enabling the print bed to tilt using three independently actuated Z-axes, our method allows standard 3D printers-such as the commercially available RatRig-to perform non-planar printing with minimal hardware modifications. Specifically, only simple extensions to the rails and bed screws are required. This enables complex, curved-layer fabrication without the need for expensive or sophisticated robotic arms.

We derive the kinematic model of the 3Z configuration and provide an open-source Python implementation that maps 3D toolpaths to machine commands. We provide a detailed study of this machine design's strengths and limitations in the context of FFF, including a build volume study, tolerance analysis, and technical details on trajectory interpolation in machine space. Several models were 3D printed using non-planar deposition to demonstrate the feasibility of the proposed approach, with our experiments achieving bed tilts of up to 30 degrees.

By lowering the entry barrier to non-planar FFF, we aim to empower a broader community of makers, educators, and researchers to experiment, innovate, and contribute to the growing field of advanced additive manufacturing.
