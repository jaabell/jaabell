Title: All about tetrahedral elements 
Slug: all-about-tetrahedral-elements
Date: 2023-08-31 14:09:49
Modified: 2023-08-31 14:09:49
Tags: OpenSees, OpenSeesPy, gmsh, modeling, YouTube
Author: jaabell
Lang: EN


<!-- PELICAN_BEGIN_SUMMARY -->


<div class="videoWrapper" align="left">
<iframe width="640" height="480" src="https://www.youtube.com/embed/2doC5QXQXOI" frameborder="0"  allowfullscreen></iframe>
</div>

This tutorial explores the advantages on using high-order meshes for finite-element modeling of solids using continuum formulations. 
<!-- PELICAN_END_SUMMARY -->

Please get the latest version of gmsh2opensees from [here](https://github.com/jaabell/gmsh2opensees). 

If you want to use my latest opensees code to run these examples (needed for high-order visualization of stress results) get my OpenSees github fork (10nt-thermal branch) from [here](https://github.com/jaabell/OpenSees/tree/10nt-thermal). Otherwise comment that function and use the other one for plotting.

Documentation:

* [FourNodeTetrahedron](https://opensees.github.io/OpenSeesDocumentation/user/manual/model/elements/FourNodeTetrahedron.html)
* [TenNodeTetrahedron](https://opensees.github.io/OpenSeesDocumentation/user/manual/model/elements/TenNodeTetrahedron.html)


Files:

* [example6.geo](https://www.dropbox.com/scl/fi/9pggxjkf2bsgu1ki2u6i5/example6.geo?rlkey=bcd9etrp99ngzszerk38tqkww&dl=1) - gmsh geometry file
* [example6.py](https://www.dropbox.com/scl/fi/phj2k6zh8qr61nbxnxlsx/example6.py?rlkey=hha1kkfjcjs29b2484wfdp6nf&dl=1) - model python script
* [view_results.py](https://www.dropbox.com/scl/fi/yqmjsy2xtm1ta6ye69yl0/view_results.py?rlkey=vz1nk1d4g4qxagi17jieo2uto&dl=1) - python script to view convergence study results