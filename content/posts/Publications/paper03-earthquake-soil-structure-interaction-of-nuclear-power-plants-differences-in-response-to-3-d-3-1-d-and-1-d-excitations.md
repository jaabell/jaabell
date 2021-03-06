Title:Paper03 - Earthquake Soil Structure Interaction of Nuclear Power Plants, differences in response to 3-D, 3 × 1-D, and 1-D excitations
Slug: paper03-earthquake-soil-structure-interaction-of-nuclear-power-plants-differences-in-response-to-3-d-3-1-d-and-1-d-excitations
Date: 2018-02-20 10:50:00
Modified: 2018-02-20 10:50:00
Tags: Papers, DRM, ESSI
Author: jaabell 
Image: https://www.dropbox.com/s/dj6ruypv0722qh2/fem_mesh.png?raw=1


Summary: **Finally!** First paper since PhD was accepted for publication. I'll take this opportunity to start a tradition and review my own papers here. I think its important that I do this for several reasons. First, there are discussions that come up during peer review that are important but don't make it into the paper. Misconceptions about the presented work can be clarified to a broader audience here. Also, I can say whatever I want, specially opinions and thoughts that come from intuition and might not make it through peer-review, I'll be as critical as possible about these too and hope that my readers can discuss with me. I can post videos...


**Finally!** First paper since PhD was accepted for publication. I'll take this opportunity to start a tradition and review my own papers here. I think its important that I do this for several reasons. First, there are discussions that come up during peer review that are important but don't make it into the paper. Misconceptions about the presented work can be clarified to a broader audience here. Also, I can say whatever I want, specially opinions and thoughts that come from intuition and might not make it through peer-review, I'll be as critical as possible about these too and hope that my readers can discuss with me. I can post videos and other additional content here and make them available to everyone for free. And, finally, this post will have a Disqus thread 

Lets get to it! Here is the citation so far (I still don't have an issue assign, going through editorial process): **Abell Mena J A**, Orbović N, McCallen D B, Jeremic B. *Earthquake soil-structure interaction of nuclear power plants, differences in response to 3-D, 3×1-D, and 1-D excitations.* Earthquake Engng Struct Dyn. 2018;1–18. [https://doi.org/10.1002/eqe.3026].

 The idea is simple: to show that the 3-D character of seismic motions has an impact on the structural response of a nuclear power-plant by comparing the response to 3-D motions with the one produced by an equivalent 1-D (1 component: horizontal) or 3×1-D (3 components) motion. Here is the NPP model used in the article:


And its fixed-base eigenmodes:



I was required by the peer-reviewers to include these fixed-base modes in the article. These are interesting, but they're not too relevant to the SSI system. SSI significantly changes the participation of the modes. I've found it useful to stop thinking in terms of eigen modes for these kind of problems, it is better to think in terms of the requirements of wave-propagation. 

In the paper, I use the domain reduction method (DRM) to couple a 3-D seismic simulation of the wave propagation from source to site with a local site and structure model. This *domain split* allows the fully 3-D modeling of the motions into the structure, accurately. Also, importantly, it allows the separation of the seismic and NPP simulation, using separate dedicated programs for each task as opposed to one big complex simulation. This reduces the computational cost dramatically and allows more modeling freedom. From the *free-field* response of the site (e.g. with no NPP on top) equivalent 1-D and 3×1-D motions were developed using 1-D site deconvolutions in Shake and input into the model for comparison. Here's a plot of what the differences look like for the top of the containment building. 

<img width="30%" src="https://www.dropbox.com/s/zl0nuu76pfhbcr3/positions_top_of_containment.png?raw=1" alt="Top of containment" />
<img width="30%" src="https://www.dropbox.com/s/18y3foxfrxcw1mq/node_733_disp.png?raw=1" alt="Displacement response" />
<img width="30%" src="https://www.dropbox.com/s/aahcmkkr8zvzhf9/node_733_acce.png?raw=1" alt="Acceleration response" />

1-D or 3×1-D waves deliver energy in-phase to the foundation of the structure, resulting in enhanced response when compared to a full 3-D response.  In this particular case, it would be *conservative* (looking at response accelerations and displacements) to use 1-D modeling of the seismic input. But, here is a point that couldn't be made in the article, **this depends on the system** and I have [found cases](http://sokocalo.engr.ucdavis.edu/~jeremic/6D_vs_1D_ESSI_for_NPPs/) where the results are opposite: it is **nonconservative** to ignore 3-D ground motions effects. This point needs to be made more clearly (future work), for different seismic settings and structures. 


I also ran this model using a non-linear constitutive model for the soil. Check out what the energy dissipation looks like under the NPP (not part of the paper).
<div class="videoWrapper" align="left">
<iframe width="640" height="480"
 src="https://www.youtube.com/embed/Kjwi_pmLgdI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

This was submitted for review Jan 6 2017, it took over a year to get acceptance! Three iterations of peer-review were done. Admittedly, I did take too much time to answer. Tough year was 2017. Although the reviewers were very picky, which led to article improvement--especially the introduction--, the main content of the article changed little. We have the same results and conclusions. 

Where from here?

It think DRM-based SSI analysis is *the* methodology to produce the highest-possible fidelity modeling of SSI. But generating these DRM motions is costly, we need supercomputers for that. Highly-detailed modeling of seismic motions is currently underway, it would be rather cheap for the researchers doing these simulations to also generate DRM-compatible motions for future exploration, making these simulations even more relevant. There needs to be an agreed format for the distribution of DRM motions, and a repository of validated motions to be used for modeling. 

Is it worthwhile? That's a research question in of itself. Clearly we can build to withstand earthquakes, so its not a safety-critical issue to use advanced SSI modeling. Might be an economic one. Maybe some case-studies can be reinterpreted in the light of 3-D motions to suggest that they were to blame in unexpected performance of existing infrastructure. Some structures will be more sensitive to these effects than others, which? how much so? under what conditions? is it necessary to model them in this way? There is great value in high-fidelity SSI modeling, is there a way to bring this into practice? All questions I want to answer in the years to come. 



