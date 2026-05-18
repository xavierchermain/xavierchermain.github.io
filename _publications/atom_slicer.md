---
layout: publication
title: AtomSlicer - Constant-Thickness Field-Aligned Non-Planar Slicing and Continuous Toolpaths for FFF
authors: <a href="https://github.com/iota97">Giovanni Cocco</a>, Vincent Belle, Eric Garner, <a href="https://www.antexel.com">Sylvain Lefebvre</a>, <b>Xavier Chermain</b>
journal: ACM Transactions on Graphics (Proceedings of SIGGRAPH)
year: 2026
article: https://drive.google.com/file/d/1pyoNb_oZMt0jiCMNW1M6_K9OF46vOif2/view?usp=sharing
supplementary_document_1: https://drive.google.com/file/d/1QtaMKUJvQeGQpCDTNnC9gETSy4kmSVgX/view?usp=sharing
supplementary_video: https://youtu.be/jU7nQ7Nd51A
code: https://github.com/iota97/AtomSlicer
id_name: Cocco2026AtomSlicer
doi: https://doi.org/10.1145/3811363
id_number: 12
---

## Abstract

Multi-axis fused filament fabrication (FFF) reduces staircase artifacts and support material by adapting nozzle orientation. However, reliable and highly customizable printing requires layers and toolpaths combining a number of challenging properties: following prescribed fields, preserving constant bead geometry, avoiding stops, retractions, and collisions.

We present AtomSlicer, which takes a 3D tool-orientation field and per-layer 2-RoSy tangent direction fields, to generate field-aligned non-planar layers of near-constant thickness, and compute collision-free deposition toolpaths that are continuous within each layer, and as continuous as possible across layers.

AtomSlicer encodes geometry with three orthogonal phase fields sampled into oriented atoms, partitions them into fabricable layers, reconstructs layer meshes, and synthesizes 2-RoSy-aligned toolpaths. Unlike prior methods it treats user- or optimizer-defined fields as constraints, producing a feasible toolpath or reporting non-fabricability rather than modifying the specification. We validate on varied shapes, including a large Thingi10k study, and 13 printed models using constant extrusion per unit path length under a fixed bead profile. AtomSlicer reduces non-extruding travel to a few percent, cuts travel moves by one to two orders of magnitude versus planar and Atomizer baselines, and is 9x-60x faster than Atomizer.
