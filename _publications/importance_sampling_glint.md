---
layout: publication
title: Importance Sampling of Glittering BSDFs based on Finite Mixture Distributions
authors: <b>Xavier Chermain</b>, <a href="https://igg.icube.unistra.fr/index.php/Basile_Sauvage">Basile Sauvage</a>, <a href="https://dpt-info.u-strasbg.fr/~dischler/">Jean-Michel Dischler</a>, and <a href="https://cg.ivd.kit.edu/staff/prof/dachsbacher/mitarbeiter_dachsbacher.php">Carsten Dachsbacher</a>
journal: Proceedings of the Eurographics Symposium on Rendering (EGSR)
year: 2021
doi: https://doi.org/10.2312/sr.20211289
article: https://xavierchermain.github.io/data/pdf/Chermain2021ImportanceSampling.pdf
supplementary_video: https://drive.google.com/file/d/15orwWKInCu6wblrcKzz4CKpZZojuzWPT/view?usp=sharing
supplementary_document_1: https://xavierchermain.github.io/data/pdf/Chermain2021ImportanceSamplingSupplemental1.pdf
supplementary_document_2: https://xavierchermain.github.io/data/pdf/Chermain2021ImportanceSamplingSupplemental2.pdf
code: https://github.com/ASTex-ICube/importance_sampling_glint
presentation: https://youtu.be/iETDEkcRI8M?t=1029
id_name: Chermain2021ImportanceSampling
id_number: 6
---
{% include math.html %}

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
