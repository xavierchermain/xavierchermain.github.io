---
layout: publication
title: Wave-Guided Field-Aligned Volume-Filling Curves
authors: <a href="https://github.com/iota97">Giovanni Cocco</a>, <b>Xavier Chermain</b>
journal: Computer Graphics Forum (Proceedings of the Symposium on Geometry Processing)
year: 2026
article: https://drive.google.com/file/d/1JBiY003G_58wd__hLbhH3NbZ-1tUVex0/view?usp=sharing
supplementary_document_1: https://drive.google.com/file/d/1xewpo4Xv6HPFIkqE5hKm9QOkosWvz1J8/view?usp=sharing
supplementary_video: https://youtu.be/XH03-9Jdeo0
code: https://github.com/iota97/Volume-Filling-Curve
id_name: Cocco2026Wave
doi: http://doi.org/10.1111/cgf.70512
id_number: 13
---
{% include math.html %}

## Abstract

We present a constructive method for generating field-aligned, volume-filling curves in watertight 3D volumes. Existing approaches rely on slow gradient-based optimization and often struggle to simultaneously achieve good field alignment, regular spacing, and scalability. To overcome this limitation, we adopt a constructive strategy: a set of well-spaced, aligned curves is constructed and then stitched together to form a single closed curve. Our core idea is to represent the intermediate curves as the intersection of two 3D wavefronts orthogonal to the tangent field. The wavefronts are the isosurfaces of two wave fields that can be optimized efficiently. This formulation enables the generation of high-quality volume-filling curves with improved alignment and spacing compared to prior work, while scaling to outputs with more than 10 million vertices. We further demonstrate robustness on 4398 solids from the Thingi10K dataset. Our current method assumes watertight inputs whose smallest geometric feature exceeds twice the target curve spacing.
