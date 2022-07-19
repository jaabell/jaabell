Title: Buidling a computer cluster for OpenSees 
Slug: buidling-a-computer-cluster-for-opensees
Date: 2022-06-07 16:46:49
Modified: 2022-06-07 16:46:49
Tags: opensees, hpc, cluster
Author: jaabell
Lang: en 

<!-- PELICAN_BEGIN_SUMMARY -->

<div class="responsive-image">
<img src="https://www.dropbox.com/s/vd3t55bh6ffxxj5/IMG-20220602-WA0013.jpeg?raw=1" / alt="Initial setup!">
</div>

As part of my recently-awarded research grant where I'll study the effects of near-field earthquakes in Santiago Chile (more on that in the future, maybe) I'm building a small cluster of computers (a [beowulf cluster](https://en.wikipedia.org/wiki/Beowulf_cluster)). 


<!-- PELICAN_END_SUMMARY -->

The main considerations were

* Maximum number of processores cores I can afford. 
* 3 to 4 Gb of RAM per core. 
* Setup with Ubuntu Linux (22.04) running ansible for software provisioning, SLURM, OpenMPI, and all of the OpenSees dependencies. 
* A network shared folder for home folders and results using something fast. 
* Connect to main node using a mixture of SSH and remote desktop software. 

Talking with Massimo Petarca of ASDEA, as well as based on my previous experience with running parallel OpenSees, it seems that OpenSees does not scale linearly with number of processors past 16 processes. This led me to hypothesize that we can get better performance from a distributed-memory system rather than one big server that fits all of the specs. 

So here is a bit of my reasoning for how I finally designed this system. 

Lets start with processors. Having had ample experience with Intel and knowing that they provide very fast linear algebra through the (now free to use) MLK library I initially quoted Intel-based systems. Xeons are one of the go-tos for the HPC industry. With Xeons you can get two or more sockets in the same motherboard and insane ammounts of ECC memory.  This is all fine for HPC servers (which require uptime and reliability) but I don't really care for the ECC and we also won't gain much in a single motherboard because of the afore-mentioned scaling issue. What I really need is OpenSees in scalar mode (as well as in parallel with low process counts) to run fast. FastFAST! Fast Xeon processors are incredibly expensive. I side-looked into AMD territory, I've been hearing that in the desktop market AMD has been giving Intel a whopping. I was impressed and tempted with AMD Threadrippers, but I really don't need 32 cores and if I get the 16 core I might as well go cheaper with Ryzen 9's 5950X with the same core count and higher clock speeds. I also looked into the new Intel i9's which are impressive, but, though the core count is the same, i9s actually have two types of cores: performance cores (clocks over 5.0GHz) and eficiency cores (around 4.0GHz)... I really want all performance cores. Also tempting is the new DDR5 memory, but its spanking new and bound to be yet technologically unstable as motherboard manufacturers learn the tricks to tap into DDR5 territory (which is somewhat significantly different and more expensive than previous generation DDR4 memory. ). Oh... AMD can handle ECC memory BTW. 

Coming back to that Intel MKL, I was under the impression that it only worked on Intel computers (duh)... but its turns out you can work around this and get some break-neck performance boosts with MKL on AMDs too! (see [this](https://www.pugetsystems.com/labs/hpc/How-To-Use-MKL-with-AMD-Ryzen-and-Threadripper-CPU-s-Effectively-for-Python-Numpy-And-Other-Applications-1637/) and [this too](https://www.reddit.com/r/matlab/comments/dxn38s/howto_force_matlab_to_use_a_fast_codepath_on_amd/)). So this removed the final barrier for me to opt for AMD for my cluster.  

So, based on all of this and my budget, for the compute nodes I'm getting 8 gaming computers outfitted with liquid cooled Ryzen 9 5950Xs (yes we will be overclocking these to get that performance boost and break into 5.0GHz territory), 64 Gb of DDR4 each, high-end Aorus motherboards, 2.5GbE network cards, and 500Gb M.2 NVMe PCIe x16 SSDs for OS and local (fast) storage options. The main (login) node will have a humbler Ryzen 9 5900X (12 cores instead of 16) and only 32 Gigs of RAM, because this is just used for login, compiling and maybe some pre/post-processing. Also it will be used for storage so its getting an extra 2Tb NVMe drive for the home folders, maybe I'll get some RAID SSDs next year. 

GPU you're asking? What GPU?

To finish the cluster, I need a fast switch. I started out with a 48-port gigabit switch I had lying around (the one you'll see in the pictures). This is totally incapable of writing to that SSD (which can theoretically write up to 7.2 GBit/s). So I bought a couple of [8port 2.5GbE QNAP managed switches](https://www.qnap.com/en/product/qsw-m2108-2c) that come with two 10GbE SFP+ ports. I also added a twin-port SFP+ capable ethernet card to the main node. I'll be doing some benchmarks of all this stuff shortly to see if I get the kind of write-performance that I want on this beast. 

To setup the software stack, I used the [BeowulfInstaller](https://github.com/jaabell/BeowulfInstaller) that my CS students developed last year. It installs smoothly over Ubuntu 22.04 so I'm really happy with that. We added a few extra things so I can share the large storage in the main node through NFS. 

I'm having lots of fun these days building, testing, benchmarking and improving this system. I'm developing and sharing all my custom benchmarks on [this GitHub repo](https://github.com/jaabell/ClusterBenchmarks). [ShakeMaker](https://github.com/jaabell/ShakerMaker) is running smoothly on the cluster and scaling linearly to all currently available 128 cores. Will be running OpenSees very soon. 

I want to finish with some special thanks to all that have contributed to this project over the years. 

* [Carlos Castex](https://www.uandes.cl/personas/carlos-castex/) (permanently on the team)
* José Luis Assadi (team v.1)
* Cristobal Griffero (team v.1)
* Sebastián Baixas (team v.2 and v.3)
* Joaquin Fernandez (team v.2)
* José Tomás Gutiérrez (team v.2)
* Omar Oyarce (team v.3)
* Alberto Hurtado (team v.3)
* José Luis Larenas (team v.3)

Here are some pics of us having fun configuring this thing in the civil engineering lab at UANDES.

<!-- <div class="responsive-image"><img src="" / alt="Initial setup day! Pizzas are a must!"></div> -->


<div class="responsive-image"><img src="https://www.dropbox.com/s/06s4s3l3mo02sfg/20220517_222312.jpg?raw=1" / alt="Initial setup!">Initial setup day! Pizzas are a must!
</div>

<div class="responsive-image"><img src="https://www.dropbox.com/s/k21v3x6p1tx907f/20220517_222342.jpg?raw=1" / alt="Initial setup!">
Omar (MS student), myself and Sebastián (former undergrad student, original creator of BeowulfInstaller) started working around 9PM
</div>
<div class="responsive-image"><img src="https://www.dropbox.com/s/nl2zxzig5sa4s2n/20220517_222349.jpg?raw=1" / alt="">Main node is up and running. Installing Ubuntu on a compute node. </div>



<div class="responsive-image"><img src="https://www.dropbox.com/s/1fg60l4nqbgygzl/20220517_230021.jpg?raw=1" / alt="">JL Larenas (future MS student) is also here for emotional support. </div>


<div class="responsive-image"><img src="https://www.dropbox.com/s/b6lrnnvv61it5cq/20220518_005352.jpg?raw=1" / alt="">Main node, two compute nodes and a switch. The basic setup to start testing and setting up with BeowulfInstaller</div>


<div class="responsive-image"><img src="https://www.dropbox.com/s/m9o6jus4dczpk9y/20220525_134638.jpg?raw=1" / alt="">The next day I added two more nodes. Some gibberish on-screen. Nice RGB lights on the RAM, I did not ask for those! </div>


<div class="responsive-image"><img src="https://www.dropbox.com/s/mcd4o2r4w2n649o/20220602_095204.jpg?raw=1" / alt="Initial setup!">Setting up more nodes and an old-fashioned rack to get everything tidy. </div>


<div class="responsive-image"><img src="https://www.dropbox.com/s/2dai1gnampzs1ab/20220602_102809.jpg?raw=1" / alt="Initial setup!">Special visit by Rodrigo who is a EE student taking my undergrad statics class that wanted to take a look. </div>


<div class="responsive-image"><img src="https://www.dropbox.com/s/vd3t55bh6ffxxj5/IMG-20220602-WA0013.jpeg?raw=1" / alt="Initial setup!">The current setup. All my 8 nodes are up. I need to configure the QNAP switch and see what kind of performance gains I get with that. The campus electrician will help me tidy up the cables and get more power for 4 more nodes (next year we'll duplicate the ammount of nodes!)</div>

<div class="responsive-image"><img src="https://www.dropbox.com/s/jjxwa9twob6b878/20201209_152907.jpg?raw=1" / alt="Initial setup!">v.2 of the Cluster was using these computer labs. On the picure Joaco Fernandez and JT Gutierrez.  Picture is from summer (january) 2021. </div>

<div class="responsive-image"><img src="https://www.dropbox.com/s/o3zl3i8yemdn70a/20210129_151546.jpg?raw=1" / alt="Initial setup!">Joaco, me, JT and Sebastián Baixas. The birth of BeowulfInstaller. What a team!  </div>

<div class="responsive-image"><img src="https://www.dropbox.com/s/avvnlv50ro44ihw/DZThqffVMAA8rJU.jpeg?raw=1" / alt="Initial setup!">  </div>
José Luis Assadi, Cristoba Griffero, Carlos Castex and me. The original cluster team!! Photo is from March 2018.
