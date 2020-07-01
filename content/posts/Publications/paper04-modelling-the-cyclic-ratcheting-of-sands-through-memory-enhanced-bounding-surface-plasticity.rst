Paper04 - Modelling the cyclic ratcheting of sands through memory-enhanced bounding surface plasticity.
#######################################################################################################

:Slug: paper04-modelling-the-cyclic-ratcheting-of-sands-through-memory-enhanced-bounding-surface-plasticity
:Date: 2020-06-30 23:33:09
:Modified: 2020-06-30 23:33:09
:Tags: Papers, Constitutive Modeling
:Author: jaabell 
:Image: https://www.dropbox.com/s/sqc6efifafocw2c/fig1-deviatoric.png?raw=1


.. highlights::

	**Abstract**

    .. include:: ../../abstracts/paper04-abstract.md


.. PELICAN_BEGIN_SUMMARY

This is the first paper fruit of the on-going collaboration with `Federico Pisanò <https://online-learning.tudelft.nl/instructors/federico-pisano/>`_ at TU Delft. Here we tackle the problem of formulating a constitutive model, derived from the SAniSand framework by Yannis Dafalias, which can replicate the *ratcheting* phenomenon on sands. 

What is ratcheting?

.. PELICAN_END_SUMMARY

This is a ratchet! Ratchetin' is what it do.

.. figure:: https://www.dropbox.com/s/ksbd0a86m4728wk/ratchet-2.png?raw=1
    :width: 40%

    *This is a ratchet. It ratechets.*

In all seriousness, when soils are subjected to asymmetrical loading, for example because there may be a static shear load acting on it and then it gets shaken, the soil accumulates irrecoverable strain as it cycles. Typical constitutive models predict a constant rate of strain accumulation for this type of loading, and that is what needs to be fixed. Only *drained* ratcheting response is pursued here, the *undrained* behavior is get its own (already accepted) article (see `this <https://en.wikipedia.org/wiki/Least_publishable_unit>`_ for more info on this publishing strategy. *(joke Fede)*). 

So, Federico and his great PhD student Haoyuan Liu together with Andrea Diambra at Bristol University integrated the idea of *memory surface* (which was applied to granular soils by `Corti and Diambra in 2016 <https://research-information.bris.ac.uk/en/publications/memory-surface-hardening-model-for-granular-soils-under-repeated->`_) to extend the SAniSand constitutive and fix this. We affectionately baptized this model `RatchySand`... a play on the SAniSand origins of the model and ratchyness. We've recently received the blessing of Yannis Dafalias himself to name the model `SAniSand-MS`, in line with other models that have been developed. 


.. figure:: https://www.dropbox.com/s/xis1190jcxkv410/ratchy_team.png?raw=1
    :width: 100%

    ...


The concept of memory surface (MS) is a way to keep track of stress states that the soil has *visited* previously, a type of soil fabric effect. When the soil re-visits this area then it should *remember* and respond with higher stiffness. Its explained in greater depth in the article, `go read it to get the best experience <https://www.researchgate.net/publication/328211282_Modelling_the_cyclic_ratcheting_of_sands_through_memory-enhanced_bounding_surface_plasticity>`_. The main point is that SAniSand's fabric tensor gets replaced with a new formulation based on the MS.


.. figure:: https://www.dropbox.com/s/sqc6efifafocw2c/fig1-deviatoric.png?raw=1
    :width: 60%
    :alt: The memory surface
    
    *The memory surface remains within the yield surface which remains within the bounding surface throughout material response. The more surfaces the better.*
    

The model adds a few extra parameters to the original formulation, these parameters control the way the memory surface *hardens* and expands or contracts, all while ensuring that the yield surface stays within the MS.


.. figure:: https://www.dropbox.com/s/rb6adj20w3qhl1c/fig3-calibration.png?raw=1
    :width: 100%
    :alt: Calibration

    *Calibration of the new model parameters requires cyclic asymmetric DSS or Drained Triaxial data... for a lot of cycles... many. (Calibration data comes from* `Wichtman et. al. 2005 <https://www.researchgate.net/publication/282252289_Explicit_Accumulation_Model_for_Non-cohesive_Soils_under_Cyclic_Loading>`_ *).*

In this :math:`q-\epsilon_a` plot the constitutive response is shown to reach a limiting value for increasing number of cycles. 

.. figure:: https://www.dropbox.com/s/clz3s9odnbze3xg/fig2-response.png?raw=1
    :width: 100%
    :alt: Response
    
    Response
    

You might be askin: *but what did* **you** *do José*. My humble contribution was to implement this constitutive model for general states of stress in `OpenSees <https://opensees.berkeley.edu/>`_. For some time I've been in the developer team for OpenSees... which means my portrait appears on the `OpenSees Project github page <https://github.com/OpenSees>`_ (which is nice).  Anyway, the process of implementing and testing the model on OpenSees gave some nice insights into the model and allowed testing in some uncharted territory of the deviatoric plane. The idea, obviously, is to follow-up with some FEM applications using the power of this new tool. We already have some things to show for this, which are coming up. 


Just would like to close thanking my collaborators: Federico, Andrea and most especially he who did the hard work Haoyuan. Y'all rock. 