---
layout: page
title: Orientable Dense Cyclic Infill for Anisotropic Appearance Fabrication
permalink: /fdm_aa/
---
{% include math.html %}

**Xavier Chermain**, [Cédric Zanni](https://members.loria.fr/CZanni/), [Jonàs Martínez](https://sites.google.com/site/jonasmartinezbayona/), Pierre-Alexandre Hugron, and [Sylvain Lefebvre](https://www.antexel.com/sylefeb/research)

[SIGGRAPH 2023](https://s2023.siggraph.org/), DOI: [10.1145/3592412](https://doi.org/10.1145/3592412)

![Our SIGGRAPH 2023 teaser]({{site.baseurl}}/data/img/Chermain2023Teaser.png)

# Abstract

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

# Resources

- [Article]({{site.baseurl}}/data/pdf/Chermain2023Orientable.pdf)
- [Supplemental Video](https://youtu.be/aUDzZrlRnNU)
- [Code](https://github.com/mfx-inria/anisotropic_appearance_fabrication)
- [BibTeX]({{site.baseurl}}/data/bibtex/Chermain2023Orientable.txt)

# Updated for errata

- 2023-05-24: Equation 7: Integration domain changed from $$\mathbb{R}$$ to $$\left[0, \frac{1}{f}\right]$$.
