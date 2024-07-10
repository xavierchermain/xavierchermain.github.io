---
layout: publication
title: Orientable Dense Cyclic Infill for Anisotropic Appearance Fabrication
authors: <b>Xavier Chermain</b>, <a href="https://members.loria.fr/CZanni/">Cédric Zanni</a>, <a href="https://sites.google.com/site/jonasmartinezbayona/">Jonàs Martínez</a>, Pierre-Alexandre Hugron, and <a href="https://www.antexel.com/sylefeb/research">Sylvain Lefebvre</a>
journal: ACM Transactions on Graphics (Proceedings of SIGGRAPH)
year: 2023
doi: https://doi.org/10.1145/3592412
article: https://drive.google.com/file/d/1z6Pf9so2r7tBpWEzHGP-b6aU0yFtz-DD/view?usp=sharing
supplementary_video: https://youtu.be/aUDzZrlRnNU
code: https://github.com/mfx-inria/anisotropic_appearance_fabrication
slides: https://drive.google.com/file/d/18OoTWXBn98SmZHrDsus1_H7m-fMFy0eX/view?usp=sharing
presentation: https://dl.acm.org/doi/suppl/10.1145/3592412/suppl_file/papers_555_VOD.mp4
replicability: https://www.replicabilitystamp.org#https-github-com-mfx-inria-anisotropic-appearance-fabrication
id_name: Chermain2023Orientable
id_number: 7
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

## Updated for errata

- 2023-05-24: Equation 7: Integration domain changed from $$\mathbb{R}$$ to $$\left[0, \frac{1}{f}\right]$$.
