---
layout: publication
title: Glint Rendering based on a Multiple-Scattering Patch BRDF
authors: <b>Xavier Chermain</b>, <a href="http://www.unilim.fr/pages_perso/frederic.claux/">Frédéric Claux</a>, and <a href="http://www.unilim.fr/pages_perso/stephane.merillou/">Stéphane Merillou</a>
journal: Computer Graphics Forum (Proceedings of the Eurographics Symposium on Rendering)
year: 2019
doi: https://doi.org/10.1111/cgf.13767
article: https://xavierchermain.github.io/data/pdf/Chermain2019Glint.pdf
supplementary_video: https://drive.google.com/file/d/1rso4I6UNYxjq5K5DA3WxUVIebYOU0A1L/view
code: https://drive.google.com/file/d/1NCz8GUDxhYkRkGnReBxNOZYNaftqE8Sn/view
slides: https://drive.google.com/file/d/1V4tLT3Y5PvddguqA0Zxpb3sfma8ILC2-/view
id_name: Chermain2019Glint
id_number: 2
---
{% include math.html %}

## Abstract

Rendering materials such as metallic paints, scratched metals and rough plastics requires glint integrators that can capture all micro-specular highlights falling into a pixel footprint, faithfully replicating surface appearance. Specular normal maps can be used to represent a wide range of arbitrary micro-structures. The use of normal maps comes with important drawbacks though: the appearance is dark overall due to back-facing normals and importance sampling is suboptimal, especially when the micro-surface is very rough. We propose a new glint integrator for specular surfaces relying on a multiple-scattering patch-based BRDF addressing these issues. To do so, our method uses a modified version of microfacet-based normal mapping [Schüssler et al. 2017] designed for glint rendering, leveraging symmetric microfacets. To model multiple-scattering, we re-introduce the lost energy caused by a perfectly specular, single-scattering formulation instead of using expensive random walks. This reflectance model is the basis of our patch-based BRDF, enabling robust sampling and artifact-free rendering with a natural appearance. Additional calculation costs amount to about 40% in the worst cases compared to previous methods [Yan et al. 2016, Chermain et al. 2018].
