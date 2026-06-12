---
layout: post
title:  "SGP'26 Article: Volume-Filling Curve"
date:   2026-06-12 00:00:00 +0100
categories: Posts
---
![Teaser Volume-Filling Curve Paper]({{site.baseurl}}/data/img/Cocco2026Wave_big.png)

**Wave-Guided Field-Aligned Volume-Filling Curves Will Be Presented at [SGP 2026](https://sgp26.org/)**

We present a constructive method for generating field-aligned, volume-filling curves in watertight 3D volumes. Existing approaches rely on slow gradient-based optimization and often struggle to simultaneously achieve good field alignment, regular spacing, and scalability. To overcome this limitation, we adopt a constructive strategy: a set of well-spaced, aligned curves is constructed and then stitched together to form a single closed curve. Our core idea is to represent the intermediate curves as the intersection of two 3D wavefronts orthogonal to the tangent field. The wavefronts are the isosurfaces of two wave fields that can be optimized efficiently. This formulation enables the generation of high-quality volume-filling curves with improved alignment and spacing compared to prior work, while scaling to outputs with more than 10 million vertices. We further demonstrate robustness on 4398 solids from the Thingi10K dataset. Our current method assumes watertight inputs whose smallest geometric feature exceeds twice the target curve spacing.

Project page: [link](https://xavierchermain.github.io/publications/volume-filling-curve)

Authors: [Giovanni Cocco](https://github.com/iota97) and Xavier Chermain

[Université de Lorraine](https://www.univ-lorraine.fr/), [CNRS](https://www.cnrs.fr/en), [Inria](https://inria.fr/en), [LORIA](https://www.loria.fr/en/) (Nancy, France)
