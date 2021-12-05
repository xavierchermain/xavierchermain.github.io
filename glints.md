---
layout: page
title: A microfacet based BRDF for the accurate and efficient rendering of high definition specular normal maps
permalink: /glints/
---

Xavier Chermain, Frédéric Claux and Stéphane Mérillou

[Visual Computer], DOI: [10.1007/s00371-018-1606-7](https://doi.org/10.1007/s00371-018-1606-7)

![Our 2018 Visual Computer paper]({{site.baseurl}}/data/img/Chermain2018AMicrofacet.png)

# Abstract

Complex specular microstructures found in glittery, scratched or brushed metal materials exhibit high frequency variations in reflected light intensity. These variations are important for the human eye and give materials their uniqueness and personality. To model such microsurfaces, high definition normal maps are very effective. The works of Yan et al. 2014 and 2016 enable the rendering of such material representations by evaluating a microfacet based BRDF related to a whole ray footprint. Still, in specific configurations and especially at grazing angles, their method does not fully capture the expected material appearance. We propose to build  upon their work and tackle the problem of accuracy using a more physically based reflection model. To do so, the normal map is approximated with a mixture of anisotropic, noncentered Beckmann normal distribution functions from which a closed form for the masking-shadowing term can be derived. Based on our formal definition, we provide a fast approximation leading to a performance overhead varying from 5% to 20% compared to the method of Yan et al. 2016. Our results show that we more closely match ground truth renderings than their methods.

# [Published, view-only version](https://rdcu.be/baa11)
# [Author version](https://drive.google.com/file/d/1JcfiksYqxI0XQ3CNV2E2gD4G2nGVf1Bb/view?usp=sharing)
# [Video file](https://drive.google.com/file/d/1fs3Y9WlUNfyRhGnf4pIJdtTumhN4XQPm/view?usp=sharing)

[Visual Computer]: https://link.springer.com/journal/371