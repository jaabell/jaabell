Title: Elementos Finitos - 2nd. Sem. 2016
Date: 2016-08-04 11:10:40
Author: jaabell
Slug: finite-elements
status: hidden

## Descripción

Curso introductorio al método de elementos finítos. El enfoque del curso es práctico orientado al modelamiento de sistemas físicos, con énfasis de que el alumno aprenda a *implementar* programas de elementos finitos con especial atención a problemas de sólidos y, en menor medida, fluídos. Se le entregará al alumno una mirada crítica, con base en teoría de elementos finitos lineales, que le permitirá conocer las fortalezas y limitaciones de las técnicas aprendidas. 

Requiere aptitud o disposición para programar, solo y en equipo. 

## Generalidades

- Creditos: 6 ($ \frac{6 \text{creditos} \cdot 30 \text{horas/credito} }{ 18 \text{semanas}} \\approx 10 $ horas semanales)
- Clases: L-W 10:30-12:20 (L: C-13 W:H-03)
- Profesor: José Abell (jaabell@miuandes.cl)
- Horario de oficina: L-W (15:30 - 17:30)
- 29 - 31 clases expositivas.

## Competencias desarrolladas

- Entender la teoría del método de elementos finitos.
- Desarrollar elementos finitos simples para problemas de elasticidad.
- Aprender técnicas de mallado para problemas de elementos finitos.
- Resolver problemas de propagación de ondas en elementos finitos.

## Evaluación

- ** (60%) ** 7 Tareas grupales (dos personas) Tareas son cada dos semanas, se entregan los Miércoles. 
- ** (30%) ** Un proyecto de modelamiento con presentaciones. 
- ** (10%) ** Lectura semanal (control online en sistema SAF) 


Calendario 
============

<iframe src="https://calendar.google.com/calendar/embed?src=68hj1a9pjm988hq9avip7ggus0%40group.calendar.google.com&ctz=America/Santiago" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>


Contenidos
============

29 clases.

- Introducción: Discretización de elementos finitos: nodos y grados de libertad.                    **(1 clase)**
- Método de rigidez directa (repaso).                                                               **(2 clases)**
- Forma débil y formulación variacional (teoría de elementos finitos).                              **(4 clases)**
- Elementos finitos para problemas sólidos                                                          **(8 clases)**
    + Reticulado y viga de Bernoulli como elementos finitos (2d y 3d)                                 **[2 clases]**
    + Elementos para análisis 2-D (triángulos y cuadriláteros de primer y segundo órden)              **[2 clases]**
    + Elementos para análisis 3-D (tetrahedros y hexaédros de primer y segundo órden)                 **[2 clases]**
    + Elementos para flexión bidimensional (plate theory)                                             **[2 Clases]**
- Propagación de ondas con elementos finitos (elementos finitos dinámicos).                         **(6 clases)**
- Problemas de fluídos.                                                                             **(3 clases)**
- Elementos para análisis acoplado (fase fluída y fase sólida) de medios porosos.                   **(2 clases)**


Lectura Personal
============

1. 8 de Agosto:
    * [Libro de Felippa. Chapter 2. Direct Stiffness Method I](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch02.d/IFEM.Ch02.pdf).
    * [Libro de Felippa. Chapter 6. FEM Modeling: Introduction](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch06.d/IFEM.Ch06.pdf).
    * [Libro de Felippa. Chapter 7. FEM Modeling: Mesh, Loads and BCs](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch07.d/IFEM.Ch07.pdf) Solo Secciones 7.1, 7.2 y 7.3
    * [Wikipedia: Types of mesh](https://en.wikipedia.org/wiki/Types_of_mesh)

1. 15 de Agosto:
    * [Libro de Felippa. Chapter 7. FEM Modeling: Mesh, Loads and BCs](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch07.d/IFEM.Ch07.pdf) Secciones 7.4 en adelante. 

1. 22 de Agosto.
    * [Curso de FEM Avanzado de Felippa. Chapter 1: Introduction](http://www.colorado.edu/engineering/CAS/courses.d/AFEM.d/AFEM.Ch01.d/AFEM.Ch01.pdf) Capitulo introductorio de interés general. Fijarse especialmente en el ejemplo del final. 
    * [Curso de FEM Avanzado de Felippa. Chapter 6: Decomposition of Poisson Problems](http://www.colorado.edu/engineering/CAS/courses.d/AVMM.d/AVMM.Ch06.d/AVMM.Ch06.pdf) hasta seccion 6.4. 

1. <s>29 de Agosto.</s> 31 de Agosto
    * [Libro de Felippa. Chapter 11: Variational Formulation of Bar Element](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch11.d/IFEM.Ch11.pdf)

1. 5 de Septiembre.
    * [Libro de Felippa. Chapter 12: Variational Formulation of Plane Beam Element.](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch12.d/IFEM.Ch12.pdf)

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
    * [Paper 2003: Método de descomposición de dominio - Bielak et. al](https://www.dropbox.com/s/14eikhimtgn9h82/Bielak%20et%20al.%20-%202003%20-%20Domain%20Reduction%20Method%20for%20Three--Dimensional%20Earthquake%20Modeling%20in%20Localized%20Regions.%20Part%20%7BI%7D%20Theory.pdf?dl=0)

Ejemplos
============
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

Tareas 
============



**Instrucciones generales:** las tareas se entregan en grupos de máximo 2 integrantes a través del sistema SAF. Debe entregar dos archivos: un *.pdf* con el informe y un *.zip* con todo el código fuente que reproduce sus resultados (archvios de geometría, malla, código de elementos finitos, resultados intermedios e imágenes incluidas en su informe deben estar en una estructura de carpetas coherente). Si el código no corre correctamente se considerará tarea no realizada.

- ** Tarea 1 ** (17 Agosto)      - Método de rigidez directa. [[Enunciado](https://www.dropbox.com/s/vquzh1qhfhoz9a0/t1.pdf?dl=0)]
- ** Tarea 2 ** (31 Agosto)      - Teoría de Elementos Finitos y Más Método de Rigidez Directa. [[Enunciado](https://www.dropbox.com/s/bmonzrj9tyk6fgn/t2.pdf?dl=0)]
- ** Tarea 3 ** (14 Septiembre)  - Elementos Finitos 1D [[Enunciado](https://www.dropbox.com/s/1vidv6lzhr6ahby/t3.pdf?dl=0)] 
- ** Tarea 4 ** (12 Octubre)  - Elementos Finitos 2D [[Enunciado](https://www.dropbox.com/s/2cvpnxgvsqvmze1/t4.pdf?dl=0 )]
- ** Tarea 5 ** (2 Octubre)     - Propagación de Ondas [[Enunciado](https://www.dropbox.com/s/9zj8dj4x4olnmd0/t5.pdf?dl=0)]
- ** Tarea 6 ** (9 Noviembre)    - Problemas de fluidos   


Proyecto de Modelamiento
============

**Presentación (23 Noviembre)** Posters!



* *Formato 1* Consiste en modelar mediante elementos finitos, usando el código generado durante el semestre (u opcionalmente algún otro *código de fuente abierta* ), algun objecto dentro del campus de la universidad. 

    * Opción 1.1 - Comparar dos estrategias de modelamiento para el mismo problema. Una debe ser
    más detallada o precisa que la otra (incerteza en el modelamiento).
    * Opción 1.2 - Hacer alguna medición de la respuesta del objeto y tratar de modelarla lo más
    preciso posible. 

* *Formato 2* Implementar alguna técnica que no se haya visto en el curso. Para esto ud. deberá
referirse a la bibliografía del curso o a la investigación científica (con ayuda del profesor) para
escoger la técnica a implementar. Se deberá presentar la implementaciómn y verificación de la
técnica. 


**Ideas para proyecto**

*Entre corchetes [] el tipo de trabajo*

 - [1.2] Propagación de ondas en la fuente del edificio central. (ver [Ecuaciones de aguas someras](https://en.wikipedia.org/wiki/Shallow_water_equations)) 
 - [1.2] Notas producidas por una copa o vaso (ver [Coffee Cup Vibrations](https://www.youtube.com/watch?v=MfzNJE4CK_s)).
 - [1.2] Vibraciones en el puente del edificio central. (Usar acelerómetro del celular).
 - [1.2] Deformación de alguna baranda o posamanos al apoyarse en el. 
 - [1.2] Vibraciones libres y amortiguamiento en un arco de futbol (sometido a un pelozato). 
 - [ 2 ] Implementar elementos acoplados u-p-U. Modelar ensayos de consolidación. 
 - [ 2 ] Implementar elementos acoplados u-p-U. Modelar ensayos de consolidación. 
 - [ 2 ] Implementar elemento termoelástico. (Resolver problema de calor acoplado con elasticidad).



Links
============

- Un buen tutorial de python científico: [http://www.scipy-lectures.org/](http://www.scipy-lectures.org/).
- [python(x,y)](https://python-xy.github.io/) Distribución de python para windows orientada para el cálculo científico (usuarios de Mac deben instalar componentes por separado). 
- [gmsh](http://gmsh.info/) Mallador de código abierto que será usado en este curso. 
- [Finite Elements at University of Colorado, Boulder](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/Home.html).  (Prof. Carlos Felippa). Este curso está fuertemente basado en este otro. 
- Recursos para hacer gráficos bien
    - [Esto](http://flowingdata.com/2010/07/22/7-basic-rules-for-making-charts-and-graphs/)
    - [y esto](http://hackerspace.kinja.com/5-rules-for-making-graphs-1605706367)
    - [tambien esto](https://visage.co/peoples-charts-graphs-look-like-crap/)
    - [porfavor esto](http://fosslien.com/rules/)
