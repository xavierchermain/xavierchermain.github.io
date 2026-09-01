---
layout: page
title: ANISO
permalink: /aniso/
---

<style>
.aniso-lead { font-size: 1.18rem; line-height: 1.55; margin-bottom: 1rem; }
.aniso-meta { display: flex; flex-wrap: wrap; gap: .45rem; margin: .8rem 0 1.2rem; }
.aniso-pill { display: inline-block; padding: .2rem .65rem; border: 1px solid #d5d5d5; border-radius: 999px; font-size: .9rem; }
.aniso-hero { margin: 1.2rem 0 1.8rem; }
.aniso-hero img { width: 100%; height: auto; border-radius: 6px; }
.aniso-caption { font-size: .88rem; color: #666; margin-top: .4rem; }
.aniso-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin: 1rem 0 1.6rem; }
.aniso-card { border: 1px solid #e1e1e1; border-radius: 7px; padding: 1rem; }
.aniso-card h3 { margin-top: 0; font-size: 1.05rem; }
.aniso-gallery img { width: 100%; height: 155px; object-fit: cover; border-radius: 5px; }
.aniso-gallery a { text-decoration: none; }
.aniso-person { margin-bottom: .35rem; }
.aniso-video { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 1rem 0; }
.aniso-video iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
/* Publication cards use a grid instead of the site's float-based publication layout.
   This keeps summaries and links aligned with the text column even when they
   extend below the teaser image. */
.aniso-pubitem { display: grid; grid-template-columns: 125px minmax(0, 1fr); column-gap: 2em; align-items: start; margin: 2em 0; line-height: 1em; }
.aniso-pubteaser img { display: block; width: 125px; height: auto; border: 0; }
.aniso-pubcontent { min-width: 0; }
.aniso-pubitem .publinks { line-height: 1.45; }
@media (max-width: 600px) {
  .aniso-gallery img { height: auto; }
  .aniso-pubitem { grid-template-columns: 90px minmax(0, 1fr); column-gap: 1rem; }
  .aniso-pubteaser img { width: 90px; }
}
</style>

<p class="aniso-lead"><strong>Orienting 3D-printing toolpaths to create new reflections.</strong></p>

<div class="aniso-meta">
  <span class="aniso-pill">ANR JCJC</span>
  <span class="aniso-pill">2024–2028</span>
  <span class="aniso-pill">ANR-24-CE10-6403</span>
  <span class="aniso-pill">Computer graphics &amp; additive manufacturing</span>
</div>

<div class="aniso-hero">
  <img src="{{site.baseurl}}/data/img/aniso_atomslicer_house.png" alt="Three photographs of an AtomSlicer 3D-printed house showing anisotropic reflections from different viewpoints" />
  <div class="aniso-caption"><strong>Anisotropic appearance fabricated with AtomSlicer.</strong> The local orientation of deposition toolpaths controls the reflections visible on the printed surface. The three views show how the appearance changes with viewpoint.</div>
</div>

## Project goal

ANISO develops digital tools and manufacturing processes to control the local orientation of material deposition in 3D printing. This control makes it possible to create customized **anisotropic appearances**—direction-dependent reflections similar to brushed metal—on planar surfaces and 3D objects using a single material, without paint or added chemical treatments.

The scientific challenge is to go from a desired spatially varying orientation to a **dense, regular, continuous and manufacturable trajectory**. The project combines computational geometry, computer graphics and digital fabrication. It targets fused filament fabrication (FFF) and surface brushing; current results primarily focus on non-planar and multi-axis FFF.

<details>
<summary><strong>Résumé en français</strong></summary>
<p>ANISO développe des outils numériques et des procédés de fabrication permettant de contrôler localement l’orientation du dépôt de matière en impression 3D. Ce contrôle permet de créer, avec un matériau unique, des apparences anisotropes personnalisées — comparables aux reflets d’un métal brossé — sur des surfaces planes ou des objets 3D, sans peinture ni traitement chimique ajouté.</p>
<p>Le défi consiste à transformer une orientation souhaitée, variable dans l’espace, en trajectoires denses, régulières, continues et effectivement fabricables. Le projet combine géométrie numérique, informatique graphique et fabrication numérique.</p>
</details>

## From orientation fields to fabricated objects

<div class="aniso-grid">
  <div class="aniso-card">
    <h3>1. Design orientations</h3>
    <p>Represent the desired local anisotropy as direction fields on surfaces or inside volumes.</p>
  </div>
  <div class="aniso-card">
    <h3>2. Generate filling curves</h3>
    <p>Construct field-aligned curves with controlled spacing, robust stitching and scalability to complex geometries.</p>
  </div>
  <div class="aniso-card">
    <h3>3. Make them manufacturable</h3>
    <p>Generate non-planar, continuous toolpaths while controlling bead geometry, nozzle accessibility and collisions.</p>
  </div>
</div>

## Publications and results

The project has produced a sequence of complementary results, from real-time rendering of anisotropic materials to geometric algorithms, machine kinematics and experimentally validated toolpaths.

{% assign aniso_publications = site.publications | where: "aniso", true | sort: "id_number" | reverse %}
{% for pub in aniso_publications %}
<div class="aniso-pubitem">
    <div class="aniso-pubteaser">
        <a href="{{ pub.url }}">
            <img src="{{site.baseurl}}/data/img/{{ pub.id_name }}_small.png" alt="{{ pub.title }} teaser" />
        </a>
    </div>
    <div class="aniso-pubcontent">
        <div class="pubtitle">{{ pub.title }}</div>
        <div class="pubauthors">{{ pub.authors }}</div>
        <div class="pubinfo">{{ pub.journal }}, {{ pub.year }}</div>
        {% if pub.award %}<div class="pubinfo"><b>{{ pub.award }}</b></div>{% endif %}
        {% if pub.aniso_summary %}<div class="pubinfo" style="margin-top:.35rem;">{{ pub.aniso_summary }}</div>{% endif %}
        <div class="publinks">
            <a href="{{ pub.url }}"><i class="fas fa-link"></i> Project page</a>
            {% if pub.doi %}&nbsp;&nbsp;<a href="{{ pub.doi }}"><i class="fas fa-external-link-alt"></i> DOI</a>{% endif %}
        </div>
    </div>
</div>
{% endfor %}

### Scientific foundation

ANISO builds on our 2023 SIGGRAPH work, [*Orientable Dense Cyclic Infill for Anisotropic Appearance Fabrication*]({{site.baseurl}}/publications/fdm-aa), which demonstrated that orienting continuous FFF deposition paths can directly control anisotropic reflections on printed surfaces. ANISO extends this idea from planar patterns toward general 3D surfaces, volumes, non-planar toolpaths and fabrication-aware algorithms.

## Open-source software and prototypes

{% for pub in aniso_publications %}
{% if pub.code %}
- **{{ pub.title | split: " - " | first }}:** [code]({{ pub.code }}){% if pub.cad %} · [CAD / machine design]({{ pub.cad }}){% endif %}{% if pub.replicability %} · [replicability stamp]({{ pub.replicability }}){% endif %}
{% endif %}
{% endfor %}

A dedicated **triple-Z-axis FFF prototype** was also developed from a desktop printer. By independently actuating the three Z axes, the print bed can tilt to execute non-planar trajectories with limited hardware modifications, providing an accessible platform for experimental validation.

## Videos and demonstrations

The following presentation gives a broad introduction to **Atomizer**, why conventional slicing is restrictive, and how the project approaches non-planar toolpath generation.

<div class="aniso-video">
<iframe src="https://www.youtube-nocookie.com/embed/eSx_QZnCSgU" title="Atomizer presentation" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

{% for pub in aniso_publications %}
{% if pub.supplementary_video or pub.presentation %}
- **{{ pub.title | split: " - " | first }}:** {% if pub.presentation %}[presentation]({{ pub.presentation }}){% endif %}{% if pub.presentation and pub.supplementary_video %} · {% endif %}{% if pub.supplementary_video %}[supplementary video]({{ pub.supplementary_video }}){% endif %}
{% endif %}
{% endfor %}

## Gallery

<div class="aniso-grid aniso-gallery">
  <div class="aniso-card">
    <a href="{{site.baseurl}}/publications/atom-slicer"><img src="{{site.baseurl}}/data/img/aniso_atomslicer_house.png" alt="AtomSlicer anisotropic appearance" /></a>
    <p><strong>AtomSlicer:</strong> anisotropic appearance on a non-planar printed object.</p>
  </div>
  <div class="aniso-card">
    <a href="{{site.baseurl}}/publications/atomizer"><img src="{{site.baseurl}}/data/img/Chermain2025Atomizer_big.png" alt="Atomizer teaser" /></a>
    <p><strong>Atomizer:</strong> toolpath generation beyond conventional layer-based slicing.</p>
  </div>
  <div class="aniso-card">
    <a href="{{site.baseurl}}/publications/threez"><img src="{{site.baseurl}}/data/img/Cocco2025Towards_big.png" alt="Triple Z-axis printer teaser" /></a>
    <p><strong>Triple-Z kinematics:</strong> an accessible platform for non-planar FFF.</p>
  </div>
  <div class="aniso-card">
    <a href="{{site.baseurl}}/publications/surface-filling-curve"><img src="{{site.baseurl}}/data/img/Cocco2026FieldAlignedSurface_big.png" alt="Field-aligned surface-filling curve teaser" /></a>
    <p><strong>Surface-filling curves:</strong> robust field-aligned trajectories on general surfaces.</p>
  </div>
</div>

## People

<div class="aniso-person"><strong><a href="https://xavierchermain.github.io/">Xavier Chermain</a></strong> — Principal investigator and project coordinator</div>
<div class="aniso-person"><strong><a href="https://github.com/iota97">Giovanni Cocco</a></strong> — PhD student</div>
<div class="aniso-person"><strong>Eric Garner</strong> — Postdoctoral researcher</div>
<div class="aniso-person"><strong><a href="https://www.linkedin.com/in/vincent-belle/">Vincent Belle</a></strong> — Research engineer</div>
<div class="aniso-person"><strong><a href="https://www.antexel.com/sylefeb/research">Sylvain Lefebvre</a></strong> — Advisor</div>

The project is carried out in the [MFX team](https://mfx.loria.fr/) at [LORIA](https://www.loria.fr/en/), with [Université de Lorraine](https://www.univ-lorraine.fr/), [CNRS](https://www.cnrs.fr/en) and [Inria](https://www.inria.fr/en/centre-inria-nancy-grand-est), Nancy, France.

## Funding

ANISO is funded by the French National Research Agency (ANR) through the **JCJC — Young Researchers** instrument.

- **Project:** *Anisotropic Appearance Fabrication With High-Resolution and Spatially Varying Orientations*
- **ANR reference:** [ANR-24-CE10-6403](https://anr.fr/Projet-ANR-24-CE10-6403)
- **Period:** October 2024 – October 2028
- **Call:** Industry 4.0: People, Organization, Technologies

The PhD work is also co-funded by the **Région Grand Est**.

<div style="max-width:250px; margin:1.5rem auto;">
  <img src="{{site.baseurl}}/data/img/anr_logo.jpg" alt="Agence nationale de la recherche logo" style="width:100%;" />
</div>

## Contact

Interested in the project, its software, or potential collaborations? Contact **Xavier Chermain** at [xavier.chermain@inria.fr](mailto:xavier.chermain@inria.fr).
