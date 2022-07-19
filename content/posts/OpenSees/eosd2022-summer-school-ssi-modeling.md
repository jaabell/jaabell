Title: EOSD2022 Summer School SSI Modeling
Slug: eosd2022-summer-school-ssi-modeling
Date: 2022-07-06 09:46:19
Modified: 2022-07-06 09:46:19
Tags: opensees, conference, EOSD, python, gmsh
Author: jaabell
Lang: en 

<!-- PELICAN_BEGIN_SUMMARY -->

<div class="responsive-image">
<img src="https://www.dropbox.com/s/i31g9x7x1ku5yn7/figura.png?raw=1" / alt="Model">
</div>

Short applicative lecture given at Eurasian OpenSees Days 2022 in Turin, Italy on July 6th. 

Supplementary material:

* [Slides](https://www.dropbox.com/s/slnk9s1z9dips22/presentation1-workshop.pdf?dl=1)
* [mshopstools.py](https://www.dropbox.com/s/oaf5iiifizpc2k6/gmshopstools.py?dl=1) - A toy library to interface _gmsh_ with `openseespy`. 
* [workshop-ssi1.geo](https://www.dropbox.com/s/9sf8aox89wcxkxu/workshop-ssi1.geo?dl=1) - SSI _gmsh_ `.geo` (geometry) file for the application. 
* [workshop-ssi1.msh](https://www.dropbox.com/s/z50ujz48ukjlesd/workshop-ssi1.msh?dl=1) - SSI _gmsh_ `.msh` (mesh) file for the application, generated from the above file without any modifications. 
* [workshop-ssi1.py](https://www.dropbox.com/s/gjuswd4szpbr7we/workshop-ssi1.py?dl=1) - Python script that reads the `.msh` file and creates and runs the OpenSees model using `openseespy`. 



<!-- PELICAN_END_SUMMARY -->
