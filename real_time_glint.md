---
layout: page
title: Procedural Physically based BRDF for Real-Time Rendering of Glints
permalink: /real_time_glint/
---

**Xavier Chermain**, [Basile Sauvage](https://igg.icube.unistra.fr/index.php/Basile_Sauvage), [Jean-Michel Dischler](https://dpt-info.u-strasbg.fr/~dischler/) and [Carsten Dachsbacher](https://cg.ivd.kit.edu/english/dachsbacher/)

[Pacific Graphic 2020, CGF issue](https://pg2021.org/), DOI: [10.1111/cgf.14141](https://doi.org/10.1111/cgf.14141)

![Our 2020 Pacific Graphic, CGF Issue, paper]({{site.baseurl}}/data/img/Chermain2020ProceduralTeaser.png)

# Abstract

Physically based rendering of glittering surfaces is a challenging problem in
computer graphics. Several methods have proposed off-line solutions, but none is
dedicated to high-performance graphics. In this work, we propose a novel
physically based BRDF for real-time rendering of glints. Our model can reproduce
the appearance of sparkling materials (rocks, rough plastics, glitter fabrics,
etc.). Compared to the previous real-time
method [Zirr and al. 2016], which is not physically based, our
BRDF uses normalized NDFs and converges to the standard microfacet
BRDF [Cook and Torrance 1982] for a large number of microfacets. Our method
procedurally computes NDFs with hundreds of sharp lobes. It relies on a
dictionary of 1D marginal distributions: at each location two of them are
randomly picked and multiplied (to obtain a NDF), rotated (to increase the
variety), and scaled (to control standard deviation/roughness). The dictionary
is multiscale, does not depend on roughness, and has a low memory footprint
(less than 1 MiB).

# [Author version]({{site.baseurl}}/data/pdf/Chermain2020Procedural.pdf)

# [Published version](https://doi.org/10.1111/cgf.14141)

# [Video](https://drive.google.com/file/d/1IiKbuvoVmccRpcmvsdao_GJVVMtXJg_p/view?usp=sharing)

# [Video Two Minute Papers](https://youtu.be/x2zDrSgrlYQ) 
Thanks to [Károly Zsolnai-Fehér](https://users.cg.tuwien.ac.at/zsolnai/) for the video.

# [WebGL](http://igg.unistra.fr/People/reproctex/Demos/Real_Time_Glint/)
Thanks to [Sylvain Thery](https://igg.icube.unistra.fr/index.php/Sylvain_Thery) for the WebGL implementation.

# [OpenGL](https://github.com/ASTex-ICube/real_time_glint)

# [Shadertoy](https://www.shadertoy.com/view/wstcRH)

# [pbrt-v3](https://github.com/ASTex-ICube/importance_sampling_glint)

# [Youtube presentation](https://youtu.be/PWhf5Lp8ZHo)

# [Slides]({{site.baseurl}}/data/pdf/Chermain2020ProceduralSlides.pdf)

# [Bibtex]({{site.baseurl}}/data/bibtex/Chermain2020ProceduralBibtex.txt)