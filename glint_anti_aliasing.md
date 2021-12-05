---
layout: page
title: Real-Time Geometric Glint Anti-Aliasing with Normal Map Filtering
permalink: /glint_anti_aliasing/
---

**Xavier Chermain**, [Simon Lucas](https://simon-lucas.fr/), [Basile Sauvage](https://igg.icube.unistra.fr/index.php/Basile_Sauvage), [Jean-Michel Dischler](https://dpt-info.u-strasbg.fr/~dischler/) and [Carsten Dachsbacher](https://cg.ivd.kit.edu/english/dachsbacher/)

[i3D](http://i3dsymposium.github.io/2021/index.html), DOI: [10.1145/3451257](https://doi.org/10.1145/3451257)

![Our 2021 i3D paper]({{site.baseurl}}/data/img/i3D2021.png)

# Abstract

Real-time geometric specular anti-aliasing is required when using a low number
of pixel samples and high-frequency specular lobes. Several methods have been
proposed for mono-lobe bidirectional reflection distribution functions (BRDFs),
but none for multi-lobe BRDFs, e.g., a glinty BRDF. We present the first method
for real-time geometric glint anti-aliasing (GGAA). It eliminates most of the
inconsistent appearing and disappearing of glints on surfaces with significant
curvatures during animations. The technique uses the glinty BRDF of Chermain et
al. 2020 and leverages hardware GPU-filtering of
textures to filter slope distributions on the fly. We also improve this glinty
BRDF by adding a correlation factor of slope. This BRDF parameter allows
convergence to normal distribution functions that are not aligned on the
surface's axes. Above all, this parameter makes glint rendering compatible with
normal map filtering using LEAN mapping. Using GGAA increases the rendering time
from 0.6 % to 4.2 % and it requires 1/3 more memory due to MIP mapping of
tabulated slope distributions. The results are compared with references using a
thousand samples per pixel.

# [Author version]({{site.baseurl}}/data/pdf/Chermain2021RealTime.pdf)

# [Supplementary material]({{site.baseurl}}/data/pdf/Chermain2021RealTimeSupplemental.pdf)

# [Video](https://drive.google.com/file/d/1ibMFMDC_eYOp7E7moFwiC3G_bolYhkA1/view?usp=sharing)

# [Presentation on Youtube (with Q&A)](https://youtu.be/dwi5qJ6oPjE?t=4269)

# [Code](https://github.com/ASTex-ICube/aa_real_time_glint)

# [Bibtex]({{site.baseurl}}/data/bibtex/Chermain2021RealTime.txt)