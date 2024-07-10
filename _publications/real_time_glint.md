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

We present a method to 3D print surfaces exhibiting a prescribed varying field
of anisotropic appearance using only standard fused filament fabrication
printers. This enables the fabrication of patterns triggering reflections
similar to that of brushed metal with direct control over the directionality of
the reflections. Our key insight, on which we ground the method, is that the
direction of the deposition paths leads to a certain degree of surface
roughness, which yields a visual anisotropic appearance. Therefore, generating
dense cyclic infills aligned with a line field allows us to grade the
anisotropic appearance of the printed surface. To achieve this, we introduce a
highly parallelizable algorithm for optimizing oriented, cyclic paths. Our
algorithm outperforms existing approaches regarding efficiency, robustness, and
result quality. We demonstrate the effectiveness of our technique in conveying
an anisotropic appearance on several challenging test cases, ranging from
patterns to photographs reinterpreted as anisotropic appearances.
