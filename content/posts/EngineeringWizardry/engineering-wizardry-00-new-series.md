Title: #EngineeringWizardry | 00 | new series
Slug: engineeringwizardry-00-new-series
Date: 2020-06-12 18:03:54
Modified: 2020-06-12 18:03:54
Tags: video EngineeringWizardry youtube teaching opensource programming geogebra
Author: jaabell
Lang: en
Status: 

<!-- PELICAN_BEGIN_SUMMARY -->


<div class="videoWrapper" align="left">
<iframe width="640" height="480" src="https://www.youtube.com/embed/F5xoTIT2uW4" frameborder="0"  allowfullscreen></iframe>
</div>

Stuck teaching during COVID-19 lockdowns in Chile has reminded me one crucial thing 
about statics (the class I'm teaching this first semester in the southern hemisphere): **it can be very frustrating for students**. This frustriation comes from unmet expectations. They're just finishing their early maths and physics formation (Calculus, Linear Algebra, Differential Equations, physics etc. ), an ideal world where problems have nice answers such as $\sqrt{2}  \pi$ or no answer at all. Then, along comes statics, and the world seems upside down. 

<!-- PELICAN_BEGIN_SUMMARY -->

Not only are the contents of statics deceptively simple ($\sum F=0$ pretty much sums it up... get it?... sums?... ok), the only way through is through exercising... a lot. This cannot be over-emphasized. 

The biggest hurdle through this is, ironically, maths. Yes! The very thing they've been becoming experts at. Take this example:

<!-- ![problem1](/images/engineering-wizardry/engineering-wizardry-00-new-series-fig00.svg) -->
<div class="responsive-image" align="left">
<img src="/images/engineering-wizardry/engineering-wizardry-00-new-series-fig00.svg">
</div>

The problem comes in two flavors depending what you ask for: 

1. Given how much you want the vertex node to move (that is, give values to $u_x$ and $u_y$), find the forces $F_x$ and $F_y$ that need to be applied. 

1. Given the forces $F_x$ and $F_y$ find out the displacement of the vertex node ($u_x$ and $u_y$).

One of this forms is easier thant the other. Which one? Think about it... take your time.

<details markdown="1">
<summary>Click to know the answer...</summary>

**NUMBER 2**

Why? Glad you asked!  In #2 you *fix the geometry* of the problem. Finding the change in length of the springs is trivial.From that you can find the forces carried by each spring and from that the force applied comes from stating a simple particle force equilibrium at the vertex. 


Form #1 fixes the applied forces. This means that the geometry is unknown, which leads to a *nonlinear system of equations* that needs to be solved so that the displacements $u_x$ and $u_y$ result in spring stretches such that the equilibrium is satisfied. 

</details>

<br>
The form of the problem notwidthstanding, to me as a teacher what's important about this problem is:

1. Stating the single-particle equilibrium where the springs meet. 
    * *Drawing* a free body diagram. 
    * This is the same for both forms.
    * Expressing the forces of the springs as a function of the stretch. 
    * Expressing the direction of the forces as a function of the point displacements. 
    * Writing down equilibrium
1. Getting an answer and *check whether it makes sense*. 

Part 1 can be done, with experience, in under 5 minutes. Part 2, on the other hand, can take about 10 to 15 minutes if form 1 is used. If form 2 is used all bets are off, the students can't be expected to solve those equations in a quiz/midterm/exam setting. (This is another subtle issue, that easy-to-state problems can easily derail into a mathematical nightmare if one is not careful).

The main problem, then, is that students spend *a lot of time* doing maths instead of statics. Since answers are important, to check whether the results make sense, gain experience and because otherwise nothing would make sense; the effort of solving problems must be addressed. If the way to study statics is solving as many problems as one can, but the math/geometry is what takes up all the time and is least important to becoming a good engineering modeler, how to avoid this?

Programming is a way to go. But, as much as I regret it, that does not come easy to all students at this point of their formation: would result in two problems instead of one. 

But there is hope: behold [geogebra](geogebra.org)!

It's a powerful and intuitive set of apps for the PC, cellphone, through the browser, etc. I'm planning on using this to bridge the math gap and accelerate student learning. 

After this long roundabout, I can finally state that this is my motivation behind the #EngineeringWizardry youtube series I intent to develop in the next months. I hope it helps you and my students. 




