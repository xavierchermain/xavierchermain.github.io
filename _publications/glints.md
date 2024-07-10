---
layout: publication
title: A Microfacet Based BRDF for the Accurate and Efficient Rendering of High Definition Specular Normal Maps
authors: <b>Xavier Chermain</b>, <a href="http://www.unilim.fr/pages_perso/frederic.claux/">Frédéric Claux</a>, and <a href="http://www.unilim.fr/pages_perso/stephane.merillou/">Stéphane Merillou</a>
journal: The Visual Computer
year: 2018
doi: https://doi.org/10.1007/s00371-018-1606-7
article: https://rdcu.be/baa11
supplementary_video: https://drive.google.com/file/d/1fs3Y9WlUNfyRhGnf4pIJdtTumhN4XQPm/view?usp=sharing
code: https://drive.google.com/file/d/1NCz8GUDxhYkRkGnReBxNOZYNaftqE8Sn/view
id_name: Chermain2018AMicrofacet
id_number: 1
---
{% include math.html %}

## Abstract

Complex specular microstructures found in glittery, scratched or brushed metal materials exhibit high frequency variations in reflected light intensity. These variations are important for the human eye and give materials their uniqueness and personality. To model such microsurfaces, high definition normal maps are very effective. The works of Yan et al. 2014 and 2016 enable the rendering of such material representations by evaluating a microfacet based BRDF related to a whole ray footprint. Still, in specific configurations and especially at grazing angles, their method does not fully capture the expected material appearance. We propose to build  upon their work and tackle the problem of accuracy using a more physically based reflection model. To do so, the normal map is approximated with a mixture of anisotropic, noncentered Beckmann normal distribution functions from which a closed form for the masking-shadowing term can be derived. Based on our formal definition, we provide a fast approximation leading to a performance overhead varying from 5% to 20% compared to the method of Yan et al. 2016. Our results show that we more closely match ground truth renderings than their methods.
