Title: Structural Response Sensitivity to Rupture Parameter Variations: A High-Fidelity Analysis of a 10-Story Building on the San Ramón Fault
Slug: structural-response-sensitivity-rupture-parameters-san-ramon-fault
Date: 2026-11-03 18:00:00
Modified: 2026-11-03 18:00:00
Tags: Papers, Conference, Earthquake Engineering, Soil-Structure Interaction, Domain Reduction Method, San Ramón Fault, Interactive
Author: jaabell
Image: /images/blogposts/srf-sensitivity-san-ramon/srf-explorer-cover.png
Summary: New conference paper (PBD-V, Puerto Varas) quantifying how stochastic rupture variability on the San Ramón Fault affects the seismic response of a 10-story building, with a full 3D interactive data explorer.

My student **Patricio Palacios B.** is presenting this work this week at **PBD-V 2026**, the 5th International Conference on Performance-Based Design in Earthquake Geotechnical Engineering, in Puerto Varas, Chile (4–6 November 2026). Co-authored with Nicolás Mora Bowen and myself, the paper asks a question that matters a lot for near-fault design: if you only run *one* rupture scenario for a given magnitude, how wrong could your structural demand estimate be?

The answer, from a campaign of 72 soil-structure interaction analyses: quite wrong, close to the fault. We generated stochastic finite-fault ground motions for Mw 6.5 and Mw 6.6 scenarios on the San Ramón Fault (three stochastic realizations each), propagated them into a 10-story reinforced-concrete building through the Domain Reduction Method at three sites spanning 3.3 to 22.5 km from the fault, and ran a three-factor ANOVA at every floor to disaggregate response variance into magnitude, stochastic slip distribution, and source-to-site distance. Source-to-site distance dominates (60–95% of variance), but at the nearest station, inter-realization displacement differences exceed 100% — a single deterministic scenario just isn't enough to characterize near-fault structural demand.

## Explore the model in 3D

Patricio built a full interactive explorer of the fault, the ground motions, the soil domain and the building response — it runs right in your browser, phone included.

<p style="text-align:center; margin: 24px 0;">
<a href="{static}/apps/srf/explorer/index.html" class="btn btn-primary" style="padding:12px 28px; font-size:1.05rem;">🌋 Open the interactive explorer →</a>
</p>

<img src="{static}/images/blogposts/srf-sensitivity-san-ramon/srf-explorer-fault-model.png" alt="3D terrain model of the San Ramón Fault with the finite-fault rupture plane and recording sites, from the interactive explorer" style="width:100%; margin:10px 0; border-radius:8px;"/>
<p style="text-align:center"><em>The San Ramón Fault model and recording sites, one of eleven chapters in the interactive explorer.</em></p>

<div style="text-align:center; margin: 28px 0;">
<img src="{static}/images/blogposts/srf-sensitivity-san-ramon/srf-explorer-qr.png" alt="QR code linking to the interactive SRF explorer" style="width:160px; height:160px;"/>
<p style="margin:6px 0 0; font-size:0.85rem; opacity:0.7;">Scan to open on your phone — handy if you're at the conference.</p>
</div>

Citation: Patricio Palacios B., Nicolás Mora Bowen, José A. Abell. *Structural Response Sensitivity to Rupture Parameter Variations: A High-Fidelity Analysis of a 10-Story Building on the San Ramón Fault.* 5th International Conference on Performance-Based Design in Earthquake Geotechnical Engineering (PBD-V), Puerto Varas, Chile, 2026. [Read the paper (PDF)]({static}/pdfs/palacios-moraBowen-abell-2026-pbdv-san-ramon-fault.pdf)
