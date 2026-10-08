Title: FONDECYT Regular 1261870: AI- and HPC-driven performance-based seismic design
Date: 2026-10-03 10:00:00
Category: pages
Slug: project-fondecyt-1261870
Authors: [jaabell]
Summary: High-fidelity performance-based seismic design of structures driven by artificial intelligence and high-performance computing.
Lang: en
Template: project
status: hidden

[← All research projects]({filename}03projects.md)

**High-Fidelity Performance-Based Seismic Design of Structures Driven by Artificial Intelligence and High-Performance Computing**

*FONDECYT Regular 1261870 · ANID (Chile) · Principal Investigator: José A. Abell · Universidad de los Andes · started 2026*

<div style="background:#f3f7fb; border-left:4px solid #2a6db0; padding:14px 18px; margin:20px 0;">
<strong>PhD and postdoctoral opportunities.</strong> See <a href="#join">who can join</a> below, then read the <a href="{filename}/posts/GroupNews/phd-postdoc-research-opportunities.md">recruitment post</a> for funding and eligibility.
</div>

## The problem

Performance-based earthquake engineering (PBEE) asks a simple question with an expensive answer: *how likely is this structure to exceed a given damage state when the ground shakes?* Answering it means running numerical models of the structure through many earthquake records and building fragility curves from the results.

Those results depend strongly on modeling choices: structural nonlinearity, soil-structure interaction, and how the earthquake motion enters the model. High-fidelity models capture these effects, but they're far too slow for a design process where engineers need to try, compare and refine many alternatives.

<img src="{static}/images/projects/fondecyt-1261870/drm-high-fidelity-model.png" alt="High-fidelity soil-structure model with domain reduction method input" style="width:100%; margin:10px 0;"/>
<p style="text-align:center"><em>High-fidelity reference: a nonlinear building and soil model excited by a three-dimensional seismic wave field through the domain reduction method (DRM).</em></p>

## The idea

The project develops a simulation-based design framework that combines **artificial intelligence**, **high-performance computing** and **high-fidelity modeling**:

- **Neural Elements.** A new kind of structural macro-element for walls, beams and columns, built on neural ordinary differential equations. They're trained on large sets of detailed 3D nonlinear simulations of structural components (validated against laboratory tests) and run inside ordinary nonlinear finite-element models, predicting both forces and the evolution of damage.
- **Foundation macro-elements.** Efficient models of nonlinear soil-foundation behavior, so the whole soil-structure system is represented and beneficial interactions between foundation and superstructure can be exploited.
- **HPC-powered design exploration.** A library of pre-trained elements lets many candidate designs be evaluated in parallel; the most promising ones are then verified with full high-fidelity simulations.

<img src="{static}/images/projects/fondecyt-1261870/building-neural-elements.png" alt="Building assembled from neural elements and foundation macro-elements" style="width:60%; display:block; margin:10px auto;"/>
<p style="text-align:center"><em>A building assembled from Neural Elements (walls, columns) connected to foundation macro-elements.</em></p>

## Application

The framework will be applied to reinforced concrete buildings in **Santiago, Chile**, under two kinds of seismic hazard: physics-based simulated earthquakes on a nearby shallow crustal fault (which let uncertainty be traced from the earthquake source to the structural response, including near-field effects), and recorded subduction-zone earthquakes as considered by the Chilean seismic code.

The tools will be implemented in [OpenSees](https://opensees.github.io/OpenSeesDocumentation/) and released openly, building on the group's open-source work (e.g. [ShakerMaker](https://github.com/jaabell/ShakerMaker)).

## Join the project {: #join }

We're looking for **PhD students** and **postdoctoral researchers** who want to work at the intersection of earthquake engineering, computational mechanics and machine learning. Useful backgrounds (no one needs all of them):

- nonlinear finite elements and structural or geotechnical earthquake engineering;
- machine learning for physical systems (neural ODEs, scientific ML);
- scientific programming: C++ and Python, OpenSees, parallel computing.

You'll have access to the group's in-house high-performance computing cluster (multi-node CPU and GPU compute with high-speed networking and storage) and to an international collaboration network.

PhD candidates can be Chilean or international and would enroll in the doctoral program at Universidad de los Andes. **This PhD opportunity requires being awarded an ANID doctoral scholarship.** Postdoctoral candidates must be **Chilean nationals** under the applicable ANID provisions. I can discuss project fit and support the relevant applications; scholarship awards are competitive. [Read the full opportunity and application guidance]({filename}/posts/GroupNews/phd-postdoc-research-opportunities.md), or email [jaabell@uandes.cl](mailto:jaabell@uandes.cl) with a short CV and a few lines on your interests.
