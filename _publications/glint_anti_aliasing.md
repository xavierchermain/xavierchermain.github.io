---
layout: publication
title: Real-Time Geometric Glint Anti-Aliasing with Normal Map Filtering
authors: <b>Xavier Chermain</b>, <a href="https://simon-lucas.fr/">Simon Lucas</a>, <a href="https://igg.icube.unistra.fr/index.php/Basile_Sauvage">Basile Sauvage</a>, <a href="https://dpt-info.u-strasbg.fr/~dischler/">Jean-Michel Dischler</a>, and <a href="https://cg.ivd.kit.edu/staff/prof/dachsbacher/mitarbeiter_dachsbacher.php">Carsten Dachsbacher</a>
journal: Proceedings of the Symposium on Interactive 3D Graphics and Games (I3D) 
year: 2021
doi: https://doi.org/10.1145/3451257
article: https://xavierchermain.github.io/data/pdf/Chermain2021RealTime.pdf
supplementary_document_1: https://xavierchermain.github.io/data/pdf/Chermain2021RealTimeSupplemental.pdf
supplementary_video: https://drive.google.com/file/d/1ibMFMDC_eYOp7E7moFwiC3G_bolYhkA1/view?usp=sharing
code: https://github.com/ASTex-ICube/aa_real_time_glint
presentation: https://youtu.be/dwi5qJ6oPjE?t=4269
id_name: Chermain2021RealTime
id_number: 5
---
{% include math.html %}

## Abstract

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
