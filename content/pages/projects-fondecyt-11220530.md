Title: FONDECYT de Iniciación 11220530: Model uncertainty in earthquake performance assessment
Date: 2026-10-03 10:00:00
Category: pages
Slug: project-fondecyt-11220530
Authors: [jaabell]
Summary: Quantification of incremental model uncertainty in earthquake performance assessment through multi-fidelity simulation and Bayesian inference (completed).
Lang: en
Template: project
status: hidden

[← All research projects]({filename}03projects.md)

**Quantification of Incremental Model Uncertainty in Earthquake Performance Assessment through Multi-Fidelity Simulation and Bayesian Inference**

*FONDECYT de Iniciación 11220530 · ANID (Chile) · Principal Investigator: José A. Abell · Universidad de los Andes · 2022–2025 · completed*

## Motivation

How much does the way we model a building, its soil and the incoming earthquake change the response we predict? This project quantified that *incremental model uncertainty* by comparing models of increasing physical fidelity against a high-fidelity reference, for reinforced concrete buildings in Santiago, Chile, threatened by the **San Ramón Fault**, a shallow crustal fault running along the city's eastern edge.

Shallow crustal earthquakes are rare, so they're poorly represented in recorded data and in current risk estimates, but they can be highly destructive near the fault. That makes them a natural target for physics-based simulation.

## What we did

<img src="{static}/images/projects/fondecyt-11220530/santiago-sites.jpg" alt="Study sites in the Santiago basin and the San Ramón Fault trace" style="float:right; width:45%; margin:0 0 10px 18px;"/>

- **Earthquake scenarios.** High-resolution rupture models of a magnitude 6.7 event on the San Ramón Fault, combined with wave-propagation simulations using [ShakerMaker](https://github.com/jaabell/ShakerMaker), to estimate ground motions at sites across the Santiago basin.
- **Simulated ground-motion database.** Multiple synthetic earthquake realizations computed with high-performance resources to explore the variability of seismic hazard in the Santiago basin.
- **Buildings at several levels of fidelity.** Two reinforced concrete buildings (an existing building on the fault's hanging wall, and one representative of Chilean practice) analyzed in OpenSees with fixed-base, plane-wave and domain reduction method (DRM) models.
- **Statistics of the differences.** A similarity score to quantify how modeling simplifications change the predicted engineering demand parameters.

<div style="clear:both;"></div>

<img src="{static}/images/projects/fondecyt-11220530/rupture-realizations.jpg" alt="Ten realizations of slip on the San Ramón Fault rupture" style="width:45%; display:block; margin:10px auto;"/>
<p style="text-align:center"><em>Ten realizations of fault slip for the San Ramón Fault scenario.</em></p>

## Key findings

- Modeling simplifications **significantly change** the predicted structural response.
- **Fixed-base models** were the least reliable, introducing substantial bias and uncertainty.
- **Plane-wave models** came much closer to the DRM reference, but missed some high-frequency effects.
- The modeling effort needed depends on which response quantity matters, so in some situations cheaper models are good enough.

<img src="{static}/images/projects/fondecyt-11220530/fixed-base-vs-drm-damage.jpg" alt="Evolution of damage in a building model: fixed-base vs DRM" style="width:85%; display:block; margin:10px auto;"/>
<p style="text-align:center"><em>Damage evolution in the walls of the same building, modeled as fixed-base (top) and with DRM input (bottom).</em></p>

## Publications

- A. Hurtado Valdés, E. Torres, G. Camata, M. Petracca, J. G. F. Crempien, J. A. Abell. *Impact of Soil–Structure Interaction Modeling Simplifications and Structural Nonlinearity on Uncertainty in EDPs: A Case Study on an Existing RC Building in Santiago.* Earthquake Engineering & Structural Dynamics 54(8), 2062–2083, 2025. [doi:10.1002/eqe.4340](https://doi.org/10.1002/eqe.4340)
- A. Hurtado, T. Vergara, E. Torres, J. A. Abell. *Importance of detailed modeling of near-field seismic wave complexity in the estimation of earthquake response of reinforced-concrete buildings.* World Conference on Earthquake Engineering, 2024.

More on the [Publications]({filename}04publications.md) page. This work continues in the [FONDECYT Regular 1261870]({filename}projects-fondecyt-1261870.md) project.
