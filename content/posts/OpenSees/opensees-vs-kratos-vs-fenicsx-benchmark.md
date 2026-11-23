Title: OpenSees vs. Kratos vs. FEniCSx: HPC Benchmark! Who wins?
Slug: opensees-vs-kratos-vs-fenicsx-benchmark
Date: 2026-11-23 13:30:00
Modified: 2026-11-23 13:30:00
Tags: OpenSees, Kratos, FEniCSx, HPC, Benchmark, YouTube
Author: jaabell
Summary: I put OpenSeesMP, Kratos and FEniCSx through the same steel I-beam collapse test on the Esmeralda cluster — same mesh, same material, same load history — and compared both their answers and their speed.

<!-- PELICAN_BEGIN_SUMMARY -->

<div class="videoWrapper" align="left">
<iframe width="640" height="480" src="https://www.youtube.com/embed/RNrx1UnJPFE" frameborder="0" allowfullscreen></iframe>
</div>

I put **OpenSeesMP**, **Kratos Multiphysics**, and **FEniCSx** through the same test on the Esmeralda cluster: a steel I-beam cantilever, meshed with quadratic tetrahedra, loaded by increasing its own weight until it approaches plastic collapse. Same geometry, same material model, same load history — how closely do the three solvers agree, and how fast does each get there?

<!-- PELICAN_END_SUMMARY -->

The video compares deformed shapes, stress fields, and load–displacement curves against the theoretical plastic bending limit, then breaks down timings from 4 to 32 MPI ranks — including the cost of writing full results, RoCE vs. TCP, what changed after fixing node12's memory configuration, and why the single-rank RTX 5090 pilot took longer than the CPU solve.

**Explore it yourself:** the [interactive 3D explorer](https://joseabell.com/apps/beam-benchmark-e25983d5a2ab5975/index.html) behind the video lets you drive the same comparison — pick any two runs, scrub the load history, inspect individual elements, and step through a guided presentation with per-solver details.

**Code and data:** everything is on GitHub at [jaabell/three-way-benchmark](https://github.com/jaabell/three-way-benchmark) — the data-preparation pipeline, the explorer's source, and the validation record.

Computing resources provided by Esmeralda through ANID–Fondecyt project 11220530.
