---
layout: publication
title: Atomizer - Beyond Non-Planar Slicing for Fused Filament Fabrication
authors: <b>Xavier Chermain</b>, <a href="https://github.com/iota97">Giovanni Cocco</a>, <a href="https://members.loria.fr/CZanni/">Cédric Zanni</a>, Eric Garner, Pierre-Alexandre Hugron, and <a href="https://www.antexel.com/sylefeb/research">Sylvain Lefebvre</a>
journal: Computer Graphics Forum (Proceedings of the Symposium on Geometry Processing)
year: 2025
article: https://drive.google.com/file/d/1P4MiYd7Qz1rJdqrq3-CEuzC4vQ2PIMeO/view?usp=sharing
supplementary_video: https://youtu.be/d9SBcfkywqA
code: https://github.com/xavierchermain/atomizer
id_name: Chermain2025Atomizer
doi: https://doi.org/10.1111/cgf.70189
id_number: 9
award: SGP Honorable Mention
presentation: https://youtu.be/eSx_QZnCSgU?si=AmJYgOVWYTSyOnbN
---
{% include math.html %}

## Abstract

Fused filament fabrication (FFF) enables users to quickly design and fabricate
parts with unprecedented geometric complexity, fine-tuning both the structural
and aesthetic properties of each object. Nevertheless, the full potential of
this technology has yet to be realized, as current slicing methods fail to fully
exploit the deposition freedom offered by modern 3D printers. In this work, we
introduce a novel approach to toolpath generation that moves beyond the
traditional layer-based concept. We use frames, referred to as atoms, as solid
elements instead of slices. We optimize the distribution of atoms within the
part volume to ensure even spacing and smooth orientation while accurately
capturing the part's geometry. Although these atoms collectively represent the
complete object, they do not inherently define a fabrication plan. To address
this, we compute an extrusion toolpath as an ordered sequence of atoms that,
when followed, provides a collision-free fabrication strategy. This general
approach is robust, requires minimal user intervention compared to existing
techniques, and integrates many of the best features into a unified framework:
precise deposition conforming to non-planar surfaces, effective filling of
narrow features -- down to a single path -- and the capability to locally print
vertical structures before transitioning elsewhere. Additionally, it enables
entirely new capabilities, such as anisotropic appearance fabrication on curved
surfaces.
