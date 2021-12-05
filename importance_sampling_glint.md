---
layout: page
title: Importance Sampling of Glittering BSDFs based on Finite Mixture Distributions
permalink: /importance_sampling_glint/
---

**Xavier Chermain**, [Basile Sauvage](https://igg.icube.unistra.fr/index.php/Basile_Sauvage), [Jean-Michel Dischler](https://dpt-info.u-strasbg.fr/~dischler/) and [Carsten Dachsbacher](https://cg.ivd.kit.edu/english/dachsbacher/)

[EGSR 2021](https://egsr.eu/2021/), DOI: [10.2312/sr.20211289](https://doi.org/10.2312/sr.20211289)

![Our EGSR 2021 teaser]({{site.baseurl}}/data/img/Chermain2021ImportanceSampling.png)

# Abstract

We propose an importance sampling scheme for the procedural glittering BSDF of
Chermain et al. 2020. Glittering BSDFs have multi-lobe visible normal
distribution functions (VNDFs) which are difficult to sample. They are typically
sampled using a mono-lobe Gaussian approximation, leading to high variance and
fireflies in the rendering. Our method optimally samples the multi-lobe VNDF,
leading to lower variance and removing firefly artefacts at equal render time.
It allows, for example, the rendering of glittering glass which requires an
efficient sampling of the BSDF. The procedural VNDF of Chermain et al. is a
finite mixture of tensor products of two 1D tabulated distributions. We sample
the visible normals from their VNDF by first drawing discrete variables
according to the mixture weights and then sampling the corresponding 1D
distributions using the technique of inverse cumulative distribution functions
(CDFs). We achieve these goals by tabulating and storing the CDFs, which uses
twice the memory as the original work. We prove the optimality of our VNDF
sampling and validate our implementation with statistical tests.

# [Author version]({{site.baseurl}}/data/pdf/Chermain2021ImportanceSampling.pdf)

# [Video](https://drive.google.com/file/d/15orwWKInCu6wblrcKzz4CKpZZojuzWPT/view?usp=sharing)

# [Code](https://github.com/ASTex-ICube/importance_sampling_glint)

# [Supplementary material 1]({{site.baseurl}}/data/pdf/Chermain2021ImportanceSamplingSupplemental1.pdf)

# [Supplementary material 2]({{site.baseurl}}/data/pdf/Chermain2021ImportanceSamplingSupplemental2.pdf)

# [Presentation on Youtube (with Q&A)](https://youtu.be/iETDEkcRI8M?t=1029)

# [Bibtex]({{site.baseurl}}/data/bibtex/Chermain2021ImportanceSampling.txt)