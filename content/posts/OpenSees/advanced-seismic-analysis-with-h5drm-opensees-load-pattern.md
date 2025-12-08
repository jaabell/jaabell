Title: Advanced seismic analysis with H5DRM OpenSees load pattern
Slug: advanced-seismic-analysis-with-h5drm-opensees-load-pattern
Date: 2022-08-22 17:47:42
Modified: 2022-09-01 14:22:59
Tags: OpenSees, analysis, seismic, DRM, YouTube, earthquake
Author: jaabell
Lang: EN

<!-- PELICAN_BEGIN_SUMMARY -->


<div class="videoWrapper" align="left">
<iframe width="640" height="480" src="https://www.youtube.com/embed/4BxzkkUzYok" frameborder="0"  allowfullscreen></iframe>
</div>


Check out the new H5DRM load pattern for DRM-based seismic analysis on OpenSees. You can find the documentation and all the example files [here](https://opensees.github.io/OpenSeesDocumentation/user/manual/model/H5DRM.html).


DRM stands for the Domain Reduction Method. It is a game-changer for seismic analysis. The DRM allows the analyst to subject their soil-structure systems to earthquake input featuring rich 3D motions. That is, you're no-longer restricted to assuming that the in-coming seismic wave-field is a planar wave, which is what 99% of analysis nowadays still assume. This is very important for several types of structures, for example as I showed was true [for nuclear power plants subjected to near-field earthquake motions](https://doi.org/10.1002/eqe.3026).

<!-- PELICAN_END_SUMMARY -->

To reap the full benefits of the DRM you need to simulate your motions with specialized software for seismological wave-propagation simulation (I used [SW4](https://geodynamics.org/resources/sw4) in my PhD work). To bring these simulations closer to the engineering community, my colleagues and I recently launched the python library [ShakerMaker](https://shakermaker.readthedocs.io/en/latest/) (yes, thus named because of the Oasis song), that can be easily used to simulate 3-D motions and directly generate the output in the H5DRM data format that I just introduced into OpenSees. ShakerMaker requires more modest computational resources at the expense that it can simulate only horizontally layered half-spaces representing earth's crust. I argue that this is sufficient for many cases where structures are sensitive to the three-dimensionality of seismic waves, and I pretend to prove it. You can run ShakerMaker in a modest workstation or small server to generate complex motions. It still helps to have your [own little HPC cluster though]({filename}../buidling-a-computer-cluster-for-opensees.md).  

**But!** *You can also do classical plane-wave earthquake response analysis with the DRM and get some huge benefits*. 

What benefits? The DRM has the great advantage of separating the place in the model where earthquake input occurs from the place where you need to enforce boundary conditions (BCs). This is huge because in more traditional modeling we just ask too much of our BCS: provide static equilibrium and at the same time a dynamic input. This is avoided altogether with the DRM. The way to do this is also explained in the above-cited paper and I'm coming up with new tools soon to make this available to OpenSees users. 

Here is a video of a structure analyzed using all these tools. The OpenSees documentation website for H5DRM has a simpler example that also shows this. 

<div class="videoWrapper" align="left">
<iframe width="640" height="480" src="https://www.youtube.com/embed/WOhd4KzacxI" frameborder="0"  allowfullscreen></iframe>
</div>

Finally, I want to bring attention to the H5DRM data format we devised for ShakerMaker and OpenSees. I would wish that this format becomes a standard for the exchange of DRM motion datasets and becomes implemented by seismic programs like SW4 and Hercules, and also by FE analysis software like LS-Dyna, Abaqus, Plaxis, Ansys, etc. Alternatively, I would also take any other format that became popular, or maybe improvements on this format. We just need to be able to store and exchange these datasets so that fancy seismic computations that are being done on large supercomputers today can have an additional impact on engineering by allowing us to subject civil engineering structural models to rich seismic wave fields coming from these large sims. 