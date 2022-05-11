Title: Temas de Magister/Memoria 2022
Slug: temas-de-magistermemoria-2022
Date: 2021-11-24 18:05:09
Modified: 2021-11-24 18:05:09
Tags: teaching, temas de memoria, alumnos
Author: jaabell 
Lang: ES
 
<!-- PELICAN_BEGIN_SUMMARY -->

Al final de la licenciatura (terminando "Métodos Computacionales en Obras Civiles") el alumno UANDES de la especialidad de Obras Civiles debe considerar si se va por la mención de "Estructuras" o por la de "Diseño de Proyecto de Infraestructuras". Además, si extenderá su carrera con un magister de continuidad o cerrará con un proyecto de título (memorias en la jerga antigua).

Esta es mi oferta de temas de magister o proyecto de título:

<!-- ![Modelo FEM de un puente](https://www.dropbox.com/s/yk1b6j9ylfnfy54/Bridge_FEM.png?raw=1) -->
<div class="responsive-image">
<img src="https://www.dropbox.com/s/mq6z1x7yg9nysbx/tema-ms-1.png?raw=1" />
</div>


##Magister

Se busca alumno de Magister para el siguiente tema:

*"Modelación de alta-fidelidad para análisis de estructuras sometidas a sismos de campo cercano "*

<!-- PELICAN_END_SUMMARY -->





La idea es modelar en detalle el proceso completo de un evento sísmic: desde la ruptura (la falla sísmica), pasando por la propagación de ondas por la corteza terrestre, incluyendo posiblemente efectos no-lineales de respuesta de sitio, y finalmente las estructuras.

Usaremos computación de alto desempeño en todas las etapas, es decir, el problema es tan grande y complejo que requiere el uso de más de un computador para resolverlo! Se modelará en [OpenSees](https://opensees.berkeley.edu/) usando la herramienta [STKO](https://asdeasoft.net/?product-stko). Se usará harto python o incluso C++ si le interesa al estudiante. 

Para más detalles y/o ayuda a discernir esta etapa, no dudes en contactarme directamente para conversar y aclarar dudas. 

##Proyectos de título

Se ofrecen los siguientes temas:


###TEMA02: Modelación y simulación de colapso de represas por desbordamiento. 

<div class="videoWrapper" align="left">
<iframe width="640" height="480" src="https://www.youtube.com/embed/V71YppdE0eE" frameborder="0"  allowfullscreen></iframe>
</div>


En un estudio anterior (Magister Nicolás Galano), se desarrolló una extensión al programa de elementos finitos OpenSees que permite simular explícitamente el proceso de socavación. Ahora, se busca aplicar este programa en la simulación del colapso de represas por desbordamiento. 


###TEMA03: Análisis de agrietamiento térmico de hormigones masivos

<div class="responsive-image">
<img src="https://www.dropbox.com/s/arm8eh21g74eypx/tema3.png?raw=1" />
</div>

Este tema mezcla adquisición de datos experimentales usando sensores y placas Raspberri Pi y simulación numérica para estudiar el tema de agrietamiento térmico en hormigones. Se continúa el trabajo de Álvaro Contreras y José Tomás Arteaga, extendiendolo al problema de predicción de agrietamiento.

###TEMA04: Desarrollo y simulación de un sistema avanzado de fundaciones para edificios




En este trabajo se trabajará en conjunto con la empresa geotécnica [R&V](https://www.ryv.cl/) en el desarrollo de un diseño innovador de fundaciones profundas optimizadas para edificioes en Chile. 

###TEMA05: Benchmarking del clúster de supercómputo de la facultad de ingeniería

<div class="responsive-image">
<img src="https://www.dropbox.com/s/0nxgad06vxxznzy/tema5.jpeg?raw=1" />
</div>


Este tema está orientado a alumnos de ingeniería de computación (aunque también para un ingeniero eléctrico que sea buen programador) con ganas de trabajar más a bajo nivel. Durante el 2020 y el verano del 2021 se reconfiguró a sala de computación de ingeniería (100 computadores) para trabajar como un clúster de supercómputo. Esto significa que se puede coordinar la ejecución de tareas utilizando los recursos de los 100 computadores de manera simultánea (600 cores, 1.6Tb de memoria RAM distribuída, 10Tb de almacenamiento) para resolver problemas de mayor envergadura (por complejidad computacional y/o cantidad). 

La idea es desarrollar una serie de benchmarkas (problemas tipo) a resolver que permita entender el desempeño de este sistema en términos de su capacidad computacional e identificar el tipo de problemas para el que resulte más eficiente. 