Title: Finite Elements - 2nd. Sem. 2017
Date: 2017-08-05 16:18:41
Author: jaabell
Slug: finite-elements
status: hidden

## Description

This is a graduate level course in the Finite Element Method. The course is practically focused, with some important mathematical insights, oriented to the modeling of physical systems. The student will learn the typical work-flow of finite element software by implementing his/her own linear solver including several typical elements. Aspects of meshing and post-processing are also thoroughly discussed and practiced. Special attention is given to mechanics oriented problems (linear elasto-statics and elasto-dynamics) as well as some other problems such as incompressible laminar flow, flow nets, shallow-wave equations, coupled elements, to name a few. 

A critical view is encouraged, whereby the student is able to identify main modeling assumption and understand the limitations of his/her results and the overall range of applicability of linear FEM methods. 


## General information 

- Credits: 6 CDT ($ \frac{6 \text{credits} \cdot 30 \text{hours/credit} }{ 18 \text{weeks}} \\approx 10 $ hours a week of dedication are required)
- Clases meetings: M-J 13:30-15:20 (M: C-215 J: H-219)
- Instructor: José Abell (jaabell@miuandes.cl)
- Office Hours: Monday 14:30 to 16:30 (at my office)
- 29 - 31 lessons.

## Developed competencies

- Completes and puts into practice the student's modeling skills. 
- To understand theory of the linear finite element method. 
- To develop simple (classical) finite elements applied to diverse PDEs.
- Gain practical meshing and post-processing skills for FEM model development. 

## Grading

- ** (50%) ** Group Homework Assignments (2 persons per group).
- ** (20%) ** 2 Midterms
- ** (10%) ** Weekly reading assignments.
- ** (20%) ** Term FEM modeling project. 
- ** Homework grade must be > 4.0 for course approval. Homeworks are regraded for partial credit. 

<!-- 
Calendario 
============

<iframe src="https://calendar.google.com/calendar/embed?src=68hj1a9pjm988hq9avip7ggus0%40group.calendar.google.com&ctz=America/Santiago" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

 -->

Contents
============

- **Introduction**. Finite element Discretization: nodes and degrees of freedom, the direct stiffness method.

- **Linear FEM Theory**. Weak and variational form of partial differential equations. Linear FEM theory. Convergence and consistency. Error bounds. Examples from 1-D elliptic problems. 1-D Quadrature. 

- **The Iso-parametric Finite Element Family **. A gallery of finite elements ( 2D and 3D) applied to different elliptic (static) problems. Multidimensional quadrature. 

- **Dynamic and transient problems**. Parabolic PDEs: diffusion (heat, transient Darcy flow, chemical diffusion, Ricci flow).  Hyperbolic PDEs: wave propagation (elasticity and shallow-wave equation)

- **Advanced topics**. One or two of these topics will be seen. 
    - Shell elements.
    - Enhanced elements (B-Bar, Selective single point integration).
    - Coupled problems (poroelasticity, thermoelasticity, fluid-solid interaction, etc). 
    - Unbounded domains: infinite-element method, Lysmer-Kuhlemeyer (aka silent) boundaries, domain reduction method.


Readings
============

1. 8  August:
    * [Felippa's lecture notes. Chapter 2. Direct Stiffness Method I](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch02.d/IFEM.Ch02.pdf).
    * [Felippa's lecture notes. Chapter 6. FEM Modeling: Introduction](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch06.d/IFEM.Ch06.pdf).
    * [Felippa's lecture notes. Chapter 7. FEM Modeling: Mesh, Loads and BCs](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch07.d/IFEM.Ch07.pdf) Sections 7.1, 7.2 y 7.3
    * [Wikipedia: Types of mesh](https://en.wikipedia.org/wiki/Types_of_mesh)

1. Optional but recommended reading. 
    * [Libro de Felippa. Chapter 7. FEM Modeling: Mesh, Loads and BCs](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch07.d/IFEM.Ch07.pdf) Secciones 7.4 en adelante. 

1. 21 August.
    * [Felippa's lecture notes. Chapter 1: Introduction](http://www.colorado.edu/engineering/CAS/courses.d/AFEM.d/AFEM.Ch01.d/AFEM.Ch01.pdf) Capitulo introductorio de interés general. Fijarse especialmente en el ejemplo del final. 
    * [Felippa's lecture notes. Chapter 6: Decomposition of Poisson Problems](http://www.colorado.edu/engineering/CAS/courses.d/AVMM.d/AVMM.Ch06.d/AVMM.Ch06.pdf) hasta seccion 6.4. 
    * Adicional útil (no evaluado en SAF) [Curso de FEM Avanzado de Felippa. Chapter 7: Weak and variational form of the Poisson Equation](http://www.colorado.edu/engineering/CAS/courses.d/AVMM.d/AVMM.Ch07.d/AVMM.Ch07.pdf)

1. 4 Sept.
    * [Felippa's lecture notes. Chapter 11: Variational Formulation of Bar Element](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch11.d/IFEM.Ch11.pdf)
    * [Felippa's lecture notes. Chapter 12: Variational Formulation of Plane Beam Element.](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch12.d/IFEM.Ch12.pdf)

1. 12 de Septiembre
    * [Libro de Felippa. Chapter 16: The Iso-Parametric Representation](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch16.d/IFEM.Ch16.pdf)
    * [Libro de Felippa. Chapter 18: Shape Function Magic](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch18.d/IFEM.Ch18.pdf)

<!--
1. 12 de Septiembre.
    * [Libro de Felippa. Chapter 14: The Plane Stress Problem](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch14.d/IFEM.Ch14.pdf)

1. 26 de Septiembre
    * [Libro de Felippa. Chapter 16: The Iso'Parametric Representation](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch16.d/IFEM.Ch16.pdf)
    * [Libro de Felippa. Chapter 18: Shape Function Magic](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch18.d/IFEM.Ch18.pdf)

1. 3 de Octubre
    * [Curso de FEM Avanzado de Felippa. Kirchoff Plates: Field Equations](http://www.colorado.edu/engineering/CAS/courses.d/AFEM.d/AFEM.Ch20.d/AFEM.Ch20.pdf)

1. 24 de Octubre 
    * [Paper 1977: Método de Integración Numérica HHT - Hilber-Hughes-Taylor](https://www.dropbox.com/s/h8gch2n30jxergt/Hilber_et_al-1977-Earthquake_Engineering_%26_Structural_Dynamics.pdf?dl=0) Esta es una extensión del método de Newmark para mayor control del la disipación numérica. 

1. 4 de Noviembre
    * [Paper 2003: Método de descomposición de dominio - Bielak et. al](https://www.dropbox.com/s/14eikhimtgn9h82/Bielak%20et%20al.%20-%202003%20-%20Domain%20Reduction%20Method%20for%20ThreeDimensional%20Earthquake%20Modeling%20in%20Localized%20Regions.%20Part%20%7BI%7D%20Theory.pdf?dl=0) 
-->

Examples
============

- [Un ambiente de trabajo efectivo para desarrollar en gmsh](https://youtu.be/Lhgw4dSEJbQ).
- [Como generar mallas con gmsh y sublime text ](https://youtu.be/LsL39CuPFx0).
- Particion de un sistema de rigidez [resolverMDF.py](https://www.dropbox.com/s/ob0zf265mso44wh/resolverMDF.py?dl=0)

<!-- 
- Introduccion: Ejemplo sobre MRD con la funcion de la tarea 1. Ejemplo completo con solucion del
sistema y graficos. [ejemplo.py](https://www.dropbox.com/s/vt2cazdop2ioqm4/ejemplo.py?dl=0)
- Introducción. Hint para leer archivos *.msh* en python. 
[ejemplo_leer_archivo.py](https://www.dropbox.com/s/q00xvko2zeoa4lq/ejemplo_leer_archivo.py?dl=0)
- Graficando polinomios de Hermite en python. [hermite.py](https://www.dropbox.com/s/j3eqr09wnqz2osk/hermite.py?dl=0)
- Para graficar resultados en gmsh. [export_to_gmsh.py](https://www.dropbox.com/s/hytpc5btq8fvjhl/export_to_gmsh.py?dl=0)
- Ejemplo de uso de las funciones de export_to_gmsh.
    - [ejemplo_write.py](https://www.dropbox.com/s/py7xjug1jcvt28q/ejemplo_write.py?dl=0).
    - [viga.msh](https://www.dropbox.com/s/ipou1eqkq3i45lx/viga.msh?dl=0).
    - [Video tutorial](https://youtu.be/NYo4txhAmgI). 
- Comparacion metodo de Newmark y Metodo de Variables de Estado
    - [metodo_de_estado.py](https://www.dropbox.com/s/0mmkq0cnt1y3e18/metodo_de_estado.py?dl=0).
    - [ejemplo_dinamica.py](https://www.dropbox.com/s/kqhq7q19j6tex2i/ejemplo_dinamica.py?dl=0).
- Viga-columna 3D (cortesía de Nicole Andrea y Francisco Hillman) [viga_columna.py](https://www.dropbox.com/s/nj0bc2vfkujgji2/viga_columna_3d.py?dl=0).
 -->

Homeworks 
============


**General instructions:** 

* Homeworks are the most important part of this course. 
* Homeworks are solved pairs (of two of course). Exceptionally, in the case of an odd enrollment, there may exist one group of 3 people, first come first served, from which more will be expected. 
* All homeworks are typewritten and handed in on the due date at the beginning of the lesson. 
* All source code (which replicates plots on the main text) is handed in via the SAF virtual learning environment (zip file). Non running code is exposed to minimum grade no matter what the report says. 
* Additionally, on the due date each group may have to present a one PPT slide summary of their work to be presented within 2 minutes. This must be submitted to the instructor before the days lesson. 
* Late work is accepted within 24 hours of due date with maximum grade of 4.0 and not eligible for re-grading.
* Re-grading of homework is expected. An extra week of time will be given after homeworks are handed back for homework re-submission.

- ** Homework 1 ** (17 Aug.) - Direct stiffness method.  [[Statement]](https://www.dropbox.com/s/jk8qh96z73c1wlw/t1.pdf?dl=0)

- ** Homework 2 ** (7 Sept.) - Weak form and 1-D finite elements.  [[Statement]](https://www.dropbox.com/s/b8qtgobvny2ubsk/t2.pdf?dl=0)

- ** Homework 3 ** (26 Sept.) - 2-D finite elements. Shear locking, selective integration, high-order elements.   [[Statement]](https://www.dropbox.com/s/ym46c7k3dy9269r/t3.pdf?dl=0)

<!-- - ** Tarea 1 ** (17 Agosto)      - Método de rigidez directa. [[Enunciado](https://www.dropbox.com/s/vquzh1qhfhoz9a0/t1.pdf?dl=0)]
- ** Tarea 2 ** (31 Agosto)      - Teoría de Elementos Finitos y Más Método de Rigidez Directa. [[Enunciado](https://www.dropbox.com/s/bmonzrj9tyk6fgn/t2.pdf?dl=0)]
- ** Tarea 3 ** (14 Septiembre)  - Elementos Finitos 1D [[Enunciado](https://www.dropbox.com/s/1vidv6lzhr6ahby/t3.pdf?dl=0)] 
- ** Tarea 4 ** (12 Octubre)  - Elementos Finitos 2D [[Enunciado](https://www.dropbox.com/s/2cvpnxgvsqvmze1/t4.pdf?dl=0 )]
- ** Tarea 5 ** (2 Octubre)     - Propagación de Ondas [[Enunciado](https://www.dropbox.com/s/9zj8dj4x4olnmd0/t5.pdf?dl=0)]
- ** Tarea 6 ** (9 Noviembre)    - Problemas de fluidos   
 -->

Modeling project
============

Posters! Due date TBA.

There are two possible formats 

* *Format 1* Use FEM tools developed during the course to model some object within the campus grounds. 

    * Option 1.1 - Compare two or more modeling strategies for the same problem to evaluate modeling uncertainty. May use third-party software as an option.
    * Option 1.2 - Model an object and do some measurement of the object response to assess model suitability or to infer model parameters (inverse modeling). If the modeling task is complex enough, may use a licensed or open source third party software (e.g. OpenSees).

* *Format 2*  Implement some strategy that has not been covered it full or at all during classes. s. Talk to instructor about possible alternatives. Should present main implementation (make it available to everyone) as well as a set of examples to verify i


**Ideas**

 - Improve one of the [previous semester posters](https://www.dropbox.com/sh/xklao0w07vh1fks/AADkFGeHOxXF7iwNRsNkraBda?dl=0). 
 - Implement and test:
     * uPU element for coupled poro-elasticity problems (consolidation, seepage, liquefaction, etc.). 
     * Optimized DOF numberer.
     * A shell element.
 - Build, model and analyze a demonstration of water seepage in an earth dam [video](https://www.youtube.com/watch?v=Xz2hfdiBOZM)
 - Model and analyze one of the structures (maquetas) at the structures lab. 

 - More ideas




Links
============

- A good tutorial for scientific python [http://www.scipy-lectures.org/](http://www.scipy-lectures.org/).
- [python(x,y)](https://python-xy.github.io/) The de-facto (scientific) python distribution for windows. 
- [Python para usuaros de Matlab](http://bfy.tw/DBWA). Several python tutorials for users migrating from Matlab to python.
- [gmsh](http://gmsh.info/) The meshing software we will use in this class.
- [Finite Elements at University of Colorado, Boulder](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/Home.html).  The main text of this class. 
- Resources for making graphs which don't hurt your eyes and kill brain cells
    - [This](http://flowingdata.com/2010/07/22/7-basic-rules-for-making-charts-and-graphs/)
    - also [this](http://hackerspace.kinja.com/5-rules-for-making-graphs-1605706367)
    - and [this](https://visage.co/peoples-charts-graphs-look-like-crap/)
    - please, oh, please [this one](http://fosslien.com/rules/)
