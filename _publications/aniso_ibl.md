---
layout: publication
title: Anisotropic Specular Image-Based Lighting Based on BRDF Major Axis Sampling
authors: Giovanni Cocco, <a href="https://members.loria.fr/CZanni/">Cédric Zanni</a>, and <b>Xavier Chermain</b>
journal: Computer Graphics Forum (Proceedings of Pacific Graphics)
year: 2024
article: https://drive.google.com/file/d/1j_NFhLSngmOycLUZ2mTV_lCL_a4NXBTb/view?usp=sharing
supplementary_video: https://youtu.be/Z_WuhOlMXBs
supplementary_document_1: https://drive.google.com/file/d/1YoB62muv_2_43qRE79NEw0AQMOWxNWTv/view?usp=sharing
code: https://github.com/iota97/AnisotropyEditor
visualizer: https://github.com/xavierchermain/brdf_major_axis
shadertoy: https://www.shadertoy.com/view/4fV3W3
id_name: Cocco2024Anisotropic
doi: https://doi.org/10.1111/cgf.15233
replicability: https://www.replicabilitystamp.org/index.html#https-github-com-iota97-anisotropyeditor
slides: https://drive.google.com/file/d/1BkFt4dmwM6w4N0cFWnANLJLyIAPIdKJC/view?usp=sharing
id_number: 8
---
{% include math.html %}

## Abstract

Anisotropic specular appearances are ubiquitous in the environment: brushed
stainless steel pans, kettles, elevator walls, fur, or scratched plastics.
Real-time rendering of these materials with image-based lighting is challenging
due to the complex shape of the bidirectional reflectance distribution function
(BRDF). We propose an anisotropic specular image-based lighting method that can
serve as a drop-in replacement for the standard bent normal technique [Rev11].
Our method yields more realistic results with a 50% increase in computation
time of the previous technique, using the same high dynamic range (HDR)
pre-integrated environment image. We use several environment samples positioned
along the major axis of the specular microfacet BRDF. We derive an analytic
formula to determine the two closest and two farthest points from the reflected
direction on an approximation of the BRDF confidence region boundary. The two
farthest points define the BRDF major axis, while the two closest points are
used to approximate the BRDF width. The environment level of detail is derived
from the BRDF width and the distance between the samples. We extensively
compare our method with the bent normal technique and the ground truth using
the GGX specular BRDF.
