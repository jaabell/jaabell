Title: New cable element in OpenSees
Slug: new-cable-element-in-opensees
Date: 2017-09-07 20:13:57
Modified: 2017-09-07 20:13:57
Tags: OpenSees, Cable, Blender, 
Category: OpenSees
Author: jaabell
Lang: EN

We've implemented a new [catenary cable element](http://opensees.berkeley.edu/wiki/index.php/CatenaryCableElement). This element is based on the work by Salehi et al[1].

The stiffness of this element is obtained using a flexibility formulation. Basically the shape of the cable is determined by the integral:

$$
\begin{align*}
\mathbf{x}(s) = -\int_0^s 
\end{align*}
$$

HEllo


Reference

[1] Salehi Ahmad Abad, M., Shooshtari, A., Esmaeili, V., & Naghavi Riabi, A. (2013). *Nonlinear analysis of cable structures under general loadings.* Finite Elements in Analysis and Design, 73, 11–19. https://doi.org/10.1016/j.finel.2013.05.002