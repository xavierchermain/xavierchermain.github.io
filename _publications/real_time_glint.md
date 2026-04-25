---
layout: publication
title: Procedural Physically based BRDF for Real-Time Rendering of Glints
authors: <b>Xavier Chermain</b>, <a href="https://igg.icube.unistra.fr/index.php/Basile_Sauvage">Basile Sauvage</a>, <a href="https://dpt-info.u-strasbg.fr/~dischler/">Jean-Michel Dischler</a>, and <a href="https://cg.ivd.kit.edu/staff/prof/dachsbacher/mitarbeiter_dachsbacher.php">Carsten Dachsbacher</a>
journal: Computer Graphics Forum (Proceedings of Pacific Graphics)
year: 2020
doi: https://doi.org/10.1111/cgf.14141
article: https://xavierchermain.github.io/data/pdf/Chermain2020Procedural.pdf
supplementary_video: https://drive.google.com/file/d/1IiKbuvoVmccRpcmvsdao_GJVVMtXJg_p/view
code: https://github.com/ASTex-ICube/real_time_glint
slides: https://xavierchermain.github.io/data/pdf/Chermain2020ProceduralSlides.pdf
presentation: https://www.youtube.com/watch?v=PWhf5Lp8ZHo
two_minute_papers: https://www.youtube.com/watch?v=x2zDrSgrlYQ
shadertoy: https://www.shadertoy.com/view/wstcRH
pbrt: https://github.com/ASTex-ICube/importance_sampling_glint
id_name: Chermain2020Procedural
id_number: 4
---
{% include math.html %}

## Abstract

Physically based rendering of glittering surfaces is a challenging problem in computer graphics. Several methods have proposed
off-line solutions, but none is dedicated to high-performance graphics. In this work, we propose a novel physically based BRDF
for real-time rendering of glints. Our model can reproduce the appearance of sparkling materials (rocks, rough plastics, glitter
fabrics, etc.). Compared to the previous real-time method, which is not physically based, our BRDF uses normalized
NDFs and converges to the standard microfacet BRDF for a large number of microfacets. Our method procedurally
computes NDFs with hundreds of sharp lobes. It relies on a dictionary of 1D marginal distributions: at each location two of
them are randomly picked and multiplied (to obtain a NDF), rotated (to increase the variety), and scaled (to control standard
deviation/roughness). The dictionary is multiscale, does not depend on roughness, and has a low memory footprint (less than
1 MiB).
