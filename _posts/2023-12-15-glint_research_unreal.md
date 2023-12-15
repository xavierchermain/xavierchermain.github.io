---
layout: post
title:  "My Glint Research in Unreal Engine"
date:   2023-12-15 00:00:00 +0100
categories: Posts
---

The new Substrate Materials in [Unreal Engine](https://www.unrealengine.com) 5.3 allows designers to put glitter on appearance: [https://youtu.be/XpPy5iQ-c6w](https://youtu.be/XpPy5iQ-c6w)

![Glittery car]({{site.baseurl}}/data/img/glint_unreal_screenshot.png)


The appearance model used is one of my research results: [https://xavierchermain.github.io/glint_anti_aliasing/](https://xavierchermain.github.io/glint_anti_aliasing/).

At [SIGGRAPH 2023](https://s2023.siggraph.org/), [Sebastien Hillaire](https://sebh.github.io/) and [Charles de Rousiers](https://www.linkedin.com/in/charles-de-rousiers-912a7936) did a presentation to describe the new material system in [Unreal Engine](https://www.unrealengine.com), and they decided to add support for glint: [https://advances.realtimerendering.com/s2023/index.html#Strata](https://advances.realtimerendering.com/s2023/index.html#Strata)

![Citation of our article]({{site.baseurl}}/data/img/glint_unreal_slide.png)

The shader graph is simple, and the [documentation](https://docs.unrealengine.com/5.3/en-US/overview-of-substrate-materials-in-unreal-engine/) is clear. In less than one hour, I was able to set up a glittery appearance. I can't wait to see the glittery 3D scenes the artists will create.

![Shader graph]({{site.baseurl}}/data/img/glint_unreal_nodes.png)

The glittery model was developed at the [University of Strasbourg](https://www.unistra.fr/) during my post-doc with [Simon Lucas](https://simon-lucas.fr/), [Basile Sauvage](https://igg.icube.unistra.fr/index.php/Basile_Sauvage), [Jean-Michel Dischler](https://dpt-info.u-strasbg.fr/~dischler/) and [Carsten Dachsbacher](https://cg.ivd.kit.edu/english/dachsbacher/)

WebGL: [http://igg.unistra.fr/People/reproctex/Demos/Real_Time_Glint/](http://igg.unistra.fr/People/reproctex/Demos/Real_Time_Glint/)

Shadertoy: [https://www.shadertoy.com/view/wstcRH](http://igg.unistra.fr/People/reproctex/Demos/Real_Time_Glint/)
