``ShakerMaker`` is an open-source python framework which simplifies the
generation of synthetic broad-band seismograms, produced by finite-fault
kinematic representations of earthquake ruptures, using a 1-D layered model
of the crust and the frequency-wavenumber ($f$–$k$) method. It is designed to
bring closer the engineering seismology and earthquake engineering communi-
ties, by catering to the earthquake simulation needs of both disciplines. One
particular goal of this framework is to provide a simple way to produce high-
fidelity earthquake motions for use with the domain-reduction method, sim-
plifying the setup of physically accurate finite-element simulations of multi-
scale seismological and earthquake engineering problems through the use of
a new specialized file format.
``ShakerMaker``’s core is composed of a high-performance Fortran imple-
mentation of the $f$-$k$ method, that is exposed to the user as a python frame-
work. Its software architecture emphasizes simplicity, extensibility, and per-
formance, allowing users to specify complex simulation scenarios with short
scripts. The message passing interface is used to achieve scalability from
simple single-processor machines to HPC clusters.