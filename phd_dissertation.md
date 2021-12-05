---
layout: page
title: Rendu basé physique de micro-reflet
permalink: /phd_dissertation/
---

Xavier Chermain

* Ph.D. Dissertation. Advisors: [Frédéric Claux](http://www.unilim.fr/pages_perso/frederic.claux/) and [Stéphane Merillou](http://www.unilim.fr/pages_perso/stephane.merillou/).
* Defense date: 27 November 2019. 
* Doctor of Philosophy in Computer Science of the University of Limoges, France.

![Teaser thesis]({{site.baseurl}}/data/img/Chermain2019Rendu.png)

# Abstract

Glint rendering, useful for simulating the appearance of glittery materials,
brushed metal or scratched plastic, is a theoretical and technical challenge in
computer graphics. It involves the use of spatially varying patch bidirectional
reflectance distribution functions (P-BRDFs) with high frequencies.
In this thesis we propose two new P-BRDFs based on specular normal
maps. Unlike the previous method [Yan et al. 2016], our first
BRDF prevents any creation of energy through footprint-dependent normalisation.
This normalisation is possible thanks to a new representation of the normal map
based on a mixture of non-centered and non-axis aligned Beckmann NDFs. The
second method improves the first one and prevents, for the first time, any
creation and loss of energy, by simulating multiple scattering in the
microgeometry. It enables artifact-free rendering of opaque and sparkling
surfaces. In addition, we provide an optimal sampling algorithm using the
visibility information of the normals. The key idea of this method is the
definition of a V-cavity for each point of the surface. To simulate multiple
scattering inside it, we compensate for the energy lost by a single scattering
model, by reintegrating lost energy with an energy compensation BRDF. The
rendering time and memory footprint of our methods are in the same order of
magnitude than previous methods.

# [Dissertation](https://drive.google.com/file/d/1i72HQVgKEBGAhmvtHJXeqkOGiZgEk3bH/view?usp=sharing), in French.