---
layout: publication
title: Field-Aligned Surface-Filling Curve via Implicit Stitching
authors: <a href="https://github.com/iota97">Giovanni Cocco</a>, <b>Xavier Chermain</b>
journal: Computer Graphics Forum (Proceedings of Eurographics)
year: 2026
article: https://drive.google.com/file/d/1NTi1p0Pt80ZEInHtYynQEmG17UJ1ax6m/view?usp=drive_link
supplementary_document_1: https://drive.google.com/file/d/1Wnp1KnzMhDivdX3QdUF44gbEQmG9-em5/view?usp=drive_link
supplementary_video: https://youtu.be/NqGd6WglHH8
code: https://github.com/iota97/Surface-Filling-Curve
id_name: Cocco2026FieldAlignedSurface
doi: https://doi.org/10.1111/cgf.70361
id_number: 11
---
{% include math.html %}

## Abstract

We present a robust and scalable method for generating field-aligned surface-filling curves on general manifolds. Building upon prior work on stripe pattern generation and field-aligned surface-filling curves, our approach introduces a novel stitching strategy that operates directly in the implicit domain. Unlike previous methods that extract and stitch isolines post hoc, we perform stitching by manipulating the scalar field itself, enabling an efficient and robust solution that generalizes beyond planar surfaces. We demonstrate more than an order of magnitude speed-up and improved alignment with input direction fields when compared to state-of-the-art geometric flow methods. Robustness is validated on the Thingi10K dataset. Moreover, the method integrates with Blender 4.5 for interactive curve generation on small models, and scales to massive meshes - producing surface-filling curves with over ten million vertices in under twenty-five minutes.
