---
layout: post
title:  "SIG'26 Article: AtomSlicer"
date:   2026-05-29 00:00:00 +0100
categories: Posts
---
![Teaser AtomSlicer Paper]({{site.baseurl}}/data/img/Cocco2026AtomSlicer_big.png)

**AtomSlicer Will Be Presented at [SIGGRAPH26](https://s2026.siggraph.org/)**

*AtomSlicer - Constant-Thickness Field-Aligned Non-Planar Slicing and Continuous Toolpaths for FFF*

AtomSlicer generates field-aligned non-planar layers and collision-free multi-axis FFF toolpaths from prescribed tool-orientation and tangent direction fields, maintaining near-constant bead geometry while avoiding stops, retractions, and collisions when possible. It treats these fields as constraints rather than modifying them, reporting non-fabricability when needed, and achieves far less non-extruding travel, one to two orders of magnitude fewer travel moves, and 9×–60× faster computation than Atomizer across large-scale and physical-print validations.

Project page: [link](https://xavierchermain.github.io/publications/atom-slicer)

Authors: [Giovanni Cocco](https://github.com/iota97), Vincent Belle, Eric Garner, [Sylvain Lefebvre](https://www.antexel.com) and Xavier Chermain

[Université de Lorraine](https://www.univ-lorraine.fr/), [CNRS](https://www.cnrs.fr/en), [Inria](https://inria.fr/en), [LORIA](https://www.loria.fr/en/) (Nancy, France)
