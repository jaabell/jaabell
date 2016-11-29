Title: Finite Elements for Shallow Water Equations
Slug: finite-elements-for-shallow-water-equations
Date: 2016-11-22 14:55:42
Tags: Finite Elements, Fluids, Shallow water equations, Tutorial
Category: Finite elements
Author: jaabell
Lang: en 

The linear [shallow water equations](https://en.wikipedia.org/wiki/Shallow_water_equations) (SWE) are used extensively to model propagation of waves in situations where lateral domain dimensions are much greater than fluid height and, at the same time, wave perturbation height are much smaller than the fluid height. This finds useful applications in the case of tsunami-wave propagation modeling in deep-sea. The equations, after heavy linearization, are given by:

$$\begin{aligned}
\pardiff{u}{t} -  f v = -g \pardiff{h}{x} \\ 
\pardiff{v}{t} +  f v = -g \pardiff{h}{y} \\
\pardiff{h}{t} = -H \pare{  \pardiff{u}{x} + \pardiff{v}{y}  }\end{aligned}$$

Where

-   $u$ is the speed in $x$ direction.

-   $v$ is the speed in $y$ direction.

-   $h$ wave perturbation height. (Free surface is at $h+H$)

-   $f$ Coriolis force, given by:

    $$\begin{aligned}
        f = 2 \Omega \sin \phi
        \end{aligned}$$

    where $\Omega$ is Earth's angular velocity ($\pi/12 \, \brak{\mathrm{rad/h}}$) and $\phi$ is latitude. 

-   $g$ acceleration due to gravity at given point in Earth.

-   $H$ fluid free surface height at repose. 

To complete the formulation, appropriate boundary conditions are needed. 

These equations will be discretized using Galerkin finite-element formulation. For this purpose we will be using the first order triangle finite element (see Felippa's chapter 15 [here](http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch15.d/IFEM.Ch15.index.html) for basic notation and details regarding triangular shape functions).

The SWE represent the space-time evolution of three scalar fields, namely $h$, $u$, and $v$. These three independent variables are the 3 degrees-of-freedom (DOF) of the problem. Therefore, each node will have information about these three DOFs. 

Using the basic 3-node triangle with interpolation functions given by the triangular coordinates (see Felippa IFEM Ch. 15 and [this](https://en.wikipedia.org/wiki/Barycentric_coordinate_system) for more info), these fields are interpolated as follows.

$$\begin{aligned}
h = \sum N_i h_i = \vect{N} \vect{h} = \matorvec{ccc}{ \zeta_1 & \zeta_2 & \zeta_3 } \matorvec{c}{h_1\\h_2\\h_3}  \\ 
u = \sum N_i u_i = \vect{N} \vect{u} = \matorvec{ccc}{ \zeta_1 & \zeta_2 & \zeta_3 } \matorvec{c}{u_1\\u_2\\u_3} \\
v = \sum N_i v_i = \vect{N} \vect{v} = \matorvec{ccc}{ \zeta_1 & \zeta_2 & \zeta_3 } \matorvec{c}{v_1\\v_2\\v_3} \end{aligned}$$

Where $\zeta_i$ are triangular coordinates and $u_i$, $v_i$, and
$h_i$ the nodal values of the scalar fields at node $i$.

As typical, we multiply the equations by a trial shape function $N_j$ and integrate over the domain of the element $\Omega^e$, carrying out integration by parts. We arrive at the weak form of the SWE. 

$$\begin{aligned}
\pare{ \int_{\Omega^e}  N_i N_j \ud \Omega^e} \dot{h}_j - 
\pare{ \int_{\Omega^e}  H \pardiff{N_i}{x} N_j \ud \Omega^e} u_j -
\pare{ \int_{\Omega^e}  H \pardiff{N_i}{y} N_j \ud \Omega^e} v_j = 0 \\
\pare{ \int_{\Omega^e}  N_i N_j \ud \Omega^e} \dot{u}_j -
\pare{ \int_{\Omega^e}  f N_i N_j \ud \Omega^e} v_j + 
\pare{ \int_{\Omega^e}  g N_i \pardiff{N_j}{x}  \ud \Omega^e} h_j = 0 \\
\pare{ \int_{\Omega^e}  N_i N_j \ud \Omega^e} \dot{v}_j +
\pare{ \int_{\Omega^e}  f N_i N_j \ud \Omega^e} u_j + 
\pare{ \int_{\Omega^e}  g N_i \pardiff{N_j}{y}  \ud \Omega^e} h_j = 0 \end{aligned}$$

Here, for the first order triangle, we simply have that 1 $N_i = \zeta_i$. Defining the vector of nodal freedoms $\vect{z}$ as:

$$\begin{aligned}
\vect{z}^T = \matorvec{ccccccccc}{h_1 & h_2 & h_3 & u_1 & u_2 & u_3 & v_1 & v_2 & v_3 }^T\end{aligned}$$

The above equations can be re-written as follows:

$$\begin{aligned}
\matorvec{ccc}
{
    \vect{M} & \vect{0} & \vect{0} \\
    \vect{0} & \vect{M} & \vect{0} \\
    \vect{0} & \vect{0} & \vect{M} 
} \dot{\vect{z}}  + 
\matorvec{ccc}
{
    \vect{0}        & -\vect{K}_{hu} & -\vect{K}_{hv} \\
    \vect{K}_{uh}   & \vect{0} & -\vect{K}_{uv} \\
    \vect{K}_{vh}   & \vect{K}_{vu} & \vect{0} 
} \vect{z}
=
\matorvec{c}
{
    \vect{0} \\ \vect{0} \\ \vect{0}
} \\ 
\vect{A} \dot{\vect{z}} + \vect{B}  \vect{z} = \vect{0}\end{aligned}$$

Where the involved sub-matrices are given by the following matrix integrals:

$$\begin{aligned}
     & \vect{M} = \int_{\Omega^e} \vect{N}^T \vect{N} \ud \Omega^e \\
     & \vect{K}_{hu} = \int_{\Omega^e} H \pare{\pardiff{\vect{N}}{x}}^T \vect{N}  \ud \Omega^e \\
     & \vect{K}_{hv} = \int_{\Omega^e} H \pare{\pardiff{\vect{N}}{y}}^T \vect{N}  \ud \Omega^e \\
     & \vect{K}_{uh} = \int_{\Omega^e} g \vect{N}^T \pardiff{\vect{N}}{x} \ud \Omega^e \\
     & \vect{K}_{vh} = \int_{\Omega^e} g \vect{N}^T \pardiff{\vect{N}}{y} \ud \Omega^e \\
     & \vect{K}_{uv} = \int_{\Omega^e} f \vect{N}^T \vect{N} \ud \Omega^e \\
     & \vect{K}_{vu} = \int_{\Omega^e} f \vect{N}^T \vect{N} \ud \Omega^e \end{aligned}$$

The derivatives $\pardiff{\vect{N}}{x}$ y $\pardiff{\vect{N}}{y}$ can be evaluated component-wise (again, see Felippa's work):

$$\begin{aligned}
\matorvec{c}
{
    \pardiff{N_i}{x} \\
    \pardiff{N_i}{y} 
} = 
\dfrac{1}{2A}
\matorvec{ccc}
{
    y_{23} & y_{31} & y_{12} \\
    x_{32} & x_{13} & x_{21} 
}
\matorvec{c}
{
    \pardiff{N_i}{\zeta_1} \\
    \pardiff{N_i}{\zeta_2} \\
    \pardiff{N_i}{\zeta_3}
}\end{aligned}$$

For example, for $N_1$:

$$\begin{aligned}
\matorvec{c}
{
    \pardiff{N_1}{x} \\
    \pardiff{N_1}{y} 
} = 
\matorvec{c}
{
    \pardiff{\zeta_1}{x} \\
    \pardiff{\zeta_1}{y} 
} = 
\dfrac{1}{2A}
\matorvec{ccc}
{
    y_{23} & y_{31} & y_{12} \\
    x_{32} & x_{13} & x_{21} 
}
\matorvec{c}
{
    \pardiff{\zeta_1}{\zeta_1} \\
    \pardiff{\zeta_1}{\zeta_2} \\
    \pardiff{\zeta_1}{\zeta_3}
}
=
\dfrac{1}{2A}
\matorvec{ccc}
{
    y_{23} & y_{31} & y_{12} \\
    x_{32} & x_{13} & x_{21} 
}
\matorvec{c}
{
    1 \\
    0 \\
    0
}
= 
\dfrac{1}{2A}
\matorvec{c}
{
    y_{23} \\
    x_{32} 
}\end{aligned}$$

It is clear that, therefore

$$\begin{aligned}
\pardiff{\vect{N}}{x} = \dfrac{1}{2A}
\matorvec{ccc}
{
    y_{23} & y_{31} & y_{12} 
} \\ 
\pardiff{\vect{N}}{y} = \dfrac{1}{2A}
\matorvec{ccc}
{
    x_{32} & x_{13} & x_{21} 
}\end{aligned}$$

Note that these derivatives are constant within each trinagle (hence the name, constant strain triangle although the interpretation is not strain in this case). In this context we have that $x_{ij} = x_i - x_j$ where  $x_i$ is the $x$ coordinate of the $i$-th element node. Similarly for $y_{ij} = y_i - y_j$.

If we further assume that the gravity field $g$, the local depth at the finite element and the Coriolis force $f$ are constant (probably a bad assumption for this variable for some applications which span the globe) *within an element* we can further reduce the discretized equations to:

$$\begin{aligned}
\vect{I}_{1} &= \int_{\Omega^e} \vect{N}^T \vect{N} \ud \Omega^e  \\
\vect{I}_{2} &= \int_{\Omega^e} \vect{N}^T \pardiff{\vect{N}}{x} \ud \Omega^e \\
\vect{I}_{3} &= \int_{\Omega^e} \vect{N}^T \pardiff{\vect{N}}{y} \ud \Omega^e\end{aligned}$$

Working on the first integral

$$\begin{aligned}
       \vect{I}_1 &= \int_{\Omega^e} \matorvec{c}{ \zeta_1 \\ \zeta_2 \\ \zeta_3 } \matorvec{ccc}{ \zeta_1 & \zeta_2 & \zeta_3 } \ud \Omega^e\\
       &=
       \int_{\Omega^e}  
        \matorvec{ccc}
        { 
            {\zeta_1}^2 & \zeta_2\zeta_1 & \zeta_3 \zeta_1 \\
            \zeta_1\zeta_2 & {\zeta_2}^2 & \zeta_3\zeta_2  \\
            \zeta_1\zeta_3 & \zeta_2\zeta_3 & {\zeta_3}^2  \\
        } 
        \ud \Omega^e \end{aligned}$$

We can use the following formula for the integration within a triangle of the monomials (again, from [here](feli))

$$\begin{aligned}
\int_{\Omega^e} {\zeta_1}^p{\zeta_2}^q{\zeta_2}^r \ud \Omega^e = \dfrac{2 A p!\, q!\, r!}{\pare{p+q+r+2}!}\end{aligned}$$

With this, the integral for $\vect{I}_1$ is evaluated to

$$\begin{aligned}
\vect{I}_1 = \dfrac{A}{12} \matorvec{ccc}
        { 
            2 & 1 & 1 \\
            1 & 2 & 1 \\
            1 & 1 & 2
        } \end{aligned}$$

Proceeding with the next integral:

$$\begin{aligned}
\vect{I}_{2} &= \int_{\Omega^e} \vect{N}^T \pardiff{\vect{N}}{x} \ud \Omega^e \\ 
 &= \int_{\Omega^e} \matorvec{c}{ \zeta_1 \\ \zeta_2 \\ \zeta_3 } 
\dfrac{1}{2A}
\matorvec{ccc}
{
    y_{23} & y_{31} & y_{12} 
}  \ud \Omega^e = 
\int_{\Omega^e} \matorvec{c}{ \zeta_1 \\ \zeta_2 \\ \zeta_3 }  \ud \Omega^e
\cdot 
\dfrac{1}{2A}
\matorvec{ccc}
{
    y_{23} & y_{31} & y_{12} 
}\\ \end{aligned}$$

Utilizing the same identity as before to evaluate the integrals we arrive at:

$$\begin{aligned}
\vect{I}_2 = \dfrac{A}{3} \matorvec{c}{ 1 \\ 1 \\ 1 }\dfrac{1}{2A}
\matorvec{ccc}
{
    y_{23} & y_{31} & y_{12} 
} = 
\dfrac{1}{6}
\matorvec{ccc}
{
    y_{23} & y_{31} & y_{12}  \\
    y_{23} & y_{31} & y_{12} \\
    y_{23} & y_{31} & y_{12} 
}\end{aligned}$$

Analogously for $\vect{I}_3$ we have:

$$\begin{aligned}
\vect{I}_{3} &= \int_{\Omega^e} \vect{N}^T \pardiff{\vect{N}}{y} \ud \Omega^e = \dfrac{1}{6}
\matorvec{ccc}
{
    x_{32} & x_{13} & x_{21} \\
    x_{32} & x_{13} & x_{21} \\
    x_{32} & x_{13} & x_{21} 
}\end{aligned}$$

And finally we can write the sub-matrices as follows. 

$$\begin{aligned}
 \vect{M} &= \vect{I}_1 \\
 \vect{K}_{hu} &=  H \cdot {\vect{I}_2}^T & \vect{K}_{hv} &=  H \cdot {\vect{I}_3}^T \\
 \vect{K}_{uh} &=  g \cdot \vect{I}_2 & \vect{K}_{vh} &=  g \cdot \vect{I}_3 \\
 \vect{K}_{uv} &=  f \cdot \vect{I}_1 & \vect{K}_{vu} &=  f \cdot \vect{I}_1 \end{aligned}$$

Which can be replaced into 
$$\begin{aligned}
\matorvec{ccc}
{
    \vect{M} & \vect{0} & \vect{0} \\
    \vect{0} & \vect{M} & \vect{0} \\
    \vect{0} & \vect{0} & \vect{M} 
} \dot{\vect{z}}  + 
\matorvec{ccc}
{
    \vect{0}        & -\vect{K}_{hu} & -\vect{K}_{hv} \\
    \vect{K}_{uh}   & \vect{0} & -\vect{K}_{uv} \\
    \vect{K}_{vh}   & \vect{K}_{vu} & \vect{0} 
} \vect{z}
=
\matorvec{c}
{
    \vect{0} \\ \vect{0} \\ \vect{0}
} \\ 
\vect{A} \dot{\vect{z}} + \vect{B}  \vect{z} = \vect{0}\end{aligned}$$
to generate the discretized SWE. 

A future post will discuss the python implementation of this finite element and its application to a basic problem. 


[feli]: [http://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.Ch15.d/IFEM.Ch15.pdf]
