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
    * [Libro de Felippa. Chapter 2. Direct Stiffness Method I](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch02.d/IFEM.Ch02.pdf).


Tareas 
============



**Instrucciones generales:** las tareas se entregan en grupos de máximo 2 integrantes a través del sistema SAF. Debe entregar dos archivos: un *.pdf* con el informe y un *.zip* con todo el código fuente que reproduce sus resultados (archvios de geometría, malla, código de elementos finitos, resultados intermedios e imágenes incluidas en su informe deben estar en una estructura de carpetas coherente). Si el código no corre correctamente se considerará tarea no realizada.

- ** Tarea 1 ** (17 Agosto)      - Método de rigidez directa. [[Enunciado](https://www.dropbox.com/s/vquzh1qhfhoz9a0/t1.pdf?dl=1)]
- ** Tarea 2 ** (31 Agosto)      - Teoría de elementos finitos.
- ** Tarea 3 ** (14 Septiembre)  - Elementos Finitos 1D
- ** Tarea 4 ** (28 Septiembre)  - Elementos Finitos 2D 
- ** Tarea 5 ** (12 Octubre)     - Elementos Finitos 3D
- ** Tarea 6 ** (26 Octubre)     - Propagación de Ondas
- ** Tarea 7 ** (9 Noviembre)    - Fluidos   


Proyecto de Modelamiento
============

**Presentación (23 Noviembre)**



* *Formato 1* Consiste en modelar mediante elementos finitos, usando el código generado durante el semestre (u opcionalmente algún otro *código de fuente abierta* ), algun objecto dentro del campus de la universidad. Debe realizar alguna medición y usar su modelo matemático para hacer una preddición de esa medición. Se deberá presentar un breve informe y realizar una presentación describiendo el modelo y las técnicas usadas para su resolución, así como también un análisis crítico de la incerteza dentro de su modelo y las limitaciones que este tiene. 

* *Formato 2* Implementar alguna técnica que no se haya visto en el curso. Para esto ud. deberá referirse a la bibliografía del curso o a la investigación científica (con ayuda del profesor) para escoger la técnica a implementar. Se entregará un breve informe y una presentación describiendo la técnica, comentando sobre su uso, ventajas y desventajas y mostrando su implementación y correcto funcionamiento.




Links
============

- Un buen tutorial de python científico: [http://www.scipy-lectures.org/](http://www.scipy-lectures.org/).
- [python(x,y)](https://python-xy.github.io/) Distribución de python para windows orientada para el cálculo científico (usuarios de Mac deben instalar componentes por separado). 
- [gmsh](http://gmsh.info/) Mallador de código abierto que será usado en este curso. 
- [Finite Elements at University of Colorado, Boulder](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/Home.html).  (Prof. Carlos Felippa). Este curso está fuertemente basado en este. 