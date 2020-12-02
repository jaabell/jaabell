Title: Parallel load balancing in OpenSees
Slug: parallel-load-balancing-in-opensees
Date: 2020-09-12 08:09:28
Modified: 2020-09-12 08:09:28
Tags: HPC, FEM, opensees
Category: Blog
Author: jaabell
Lang: en
Status: draft

10 years ago, I set out to pursue a PhD in civil engineering. Back then I was a Matlab programmer who got python and linux-pilled and was in the process of fully transitioning into the bliss that is opensource. I had just finished my MS, was hired at Universidad de los Andes, PhD pending, and got into OpenSees for consulting (because it was free and I can program so why not... it also had a good user base and a responsive forum thanks to both Frank McKenna and Silvia Mazzoni). Doing that, it was frustrating to see that I had multiple processors but OpenSees was only using one! How come? Webpage says they have parallel! I chose UCDavis because of Boris Jeremic. He ticked all the checkboxes I thought of: parallel? check! linux? check! version control? check! nerdy mid 90s looking personal website? check! (God I love that aesthetic!). Opensees? check... kinda, but that's a story for another lifetime. 

So I learned C++, Makefiles, multiple compilers, profiling, debugging, compiler flags, took that awesome class on HPC at UC Berkeley (with Jim Demmel no less!) and got to work hard on making stuff run fast in parallel. Which brings me to this post on the need to do parallel load-balancing on OpenSees.

OpenSees in parallel comes in two flavors: OpenSeesSP and OpenSeesMP, and I never know which is which. (checks https://opensees.berkeley.edu/OpenSees/parallel/parallel.php for the ten-hundredth time).

+ OpenSeesSP: For Performing analysis of very large models.
+ OpenSeesMP: For Performing parameter studies or analysis of large models with user defined partitions

For the uninitiated, when you want to analyze large FEM models in parallel you distribute the "load" between processors by partitioning the analysis domain into sub-domains consisting of neighboring elements. Its pretty straightforward really. The difference between SP and MP in the OpenSees name depends on when the partitioning is done. SP does the partitioning for you, which is nice because you dont need to worry about it. MP requires you to do it manually, which can be a hassle if you don't know upfront how many processors you want to use. So I used SP (but will probably change over to MP soon) for simplicity. 

Whichever way you do it the problem of load-balancing comes up. 

