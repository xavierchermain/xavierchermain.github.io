---
layout: page
title: Glint Rendering based on a Multiple-Scattering Patch BRDF
permalink: /ms_glints/
---

Xavier Chermain, Frédéric Claux and Stéphane Mérillou

[EGSR 2019, CGF Track], DOI: [10.1111/cgf.13767](https://doi.org/10.1111/cgf.13767)

![Our 2019 EGSR, CGF Track, paper]({{site.baseurl}}/data/img/Chermain2019Glint.png)

# Abstract

Rendering materials such as metallic paints, scratched metals and rough plastics requires glint integrators that can capture all micro-specular highlights falling into a pixel footprint, faithfully replicating surface appearance. Specular normal maps can be used to represent a wide range of arbitrary micro-structures. The use of normal maps comes with important drawbacks though: the appearance is dark overall due to back-facing normals and importance sampling is suboptimal, especially when the micro-surface is very rough. We propose a new glint integrator for specular surfaces relying on a multiple-scattering patch-based BRDF addressing these issues. To do so, our method uses a modified version of microfacet-based normal mapping [Schüssler et al. 2017] designed for glint rendering, leveraging symmetric microfacets. To model multiple-scattering, we re-introduce the lost energy caused by a perfectly specular, single-scattering formulation instead of using expensive random walks. This reflectance model is the basis of our patch-based BRDF, enabling robust sampling and artifact-free rendering with a natural appearance. Additional calculation costs amount to about 40% in the worst cases compared to previous methods [Yan et al. 2016, Chermain et al. 2018].

# [Author version]({{site.baseurl}}/data/pdf/Chermain2019Glint.pdf)

# [Video file](https://drive.google.com/file/d/1rso4I6UNYxjq5K5DA3WxUVIebYOU0A1L/view?usp=sharing)

# [Code](https://drive.google.com/file/d/1NCz8GUDxhYkRkGnReBxNOZYNaftqE8Sn/view?usp=sharing)

# [Slides](https://drive.google.com/file/d/1V4tLT3Y5PvddguqA0Zxpb3sfma8ILC2-/view?usp=sharing)

[EGSR 2019, CGF Track]: http://egsr2019.icube.unistra.fr/program.html