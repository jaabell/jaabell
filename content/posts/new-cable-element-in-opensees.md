Title: New cable element in OpenSees
Slug: new-cable-element-in-opensees
Date: 2017-09-07 20:13:57
Modified: 2017-09-07 20:13:57
Tags: OpenSees, Cable, Blender
Author: jaabell
Lang: EN

<div class="youtube" align="left">
<iframe width="640" height="480" src="https://www.youtube.com/embed/MX_--SI_vKg" frameborder="0" allowfullscreen></iframe>
</div>


With my student, Pablo Ibañez, we implemented a new [catenary cable element](http://opensees.berkeley.edu/wiki/index.php/CatenaryCableElement) in OpenSees. This element is based on the work by Salehi et al[1].

The stiffness of this element is obtained using a flexibility formulation. Basically the shape of the cable is determined by the integral:

$$
\begin{align*}
\vect{x}(s) = \vect{x}_1 - \int_0^s \dfrac{\vect{w}s + \vect{f}}{\Vert \vect{w}s + \vect{f} \Vert^2}\pare{\dfrac{\Vert \vect{w}s + \vect{f} \Vert}{EA} + \pare{1 + \alpha \Delta T}} \ud s \\
\vect{w} = \brak{w_1,\, w_2,\, w_3}^T \qquad
\vect{f} = \brak{f_1,\, f_2,\, f_3}^T 
\end{align*}
$$

Where $\vect{x_1}$ is the position of the first node of the cable, $\vect{w}$ is the weight vector in each direction, $EA$ is the stiffness, $\alpha \Delta T$ is the change in strain due to temperature and $\vect{f}$ is the force vector at the start node. This equation is iterated (with the forces as variable) upon until the the shape of the cable matches the nodal postiions imposed by the finite element program (trial displacements). Then it is used to derive a stiffness matrix. 

The element, as is, passes all our static verification tests. With the additional assumption of a lumped-mass matrix, we're currently working on a dynamic verification suite as well as some validation experiments. 

The animation above was created using [OpenSees](http://opensees.berkeley.edu/) to simulate the cable and [Blender](http://www.blender.org) to render it. 


Reference

[1] Salehi Ahmad Abad, M., Shooshtari, A., Esmaeili, V., & Naghavi Riabi, A. (2013). *Nonlinear analysis of cable structures under general loadings.* Finite Elements in Analysis and Design, 73, 11–19. https://doi.org/10.1016/j.finel.2013.05.002