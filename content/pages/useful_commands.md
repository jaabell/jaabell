Title: Useful Commands
Slug: useful-commands
Date: 2014-06-25 15:10:25
Tags: 
Category: 
Author: jaabell
Lang: 
Summary: 
status: hidden

Useful Commands for everyday tasks
---------------------------------------------------------------------------------------------------



##Table of Contents

[TOC]

Linux Management
---------------------------------------------------------------------------------------------------

To use find to remove files

	find . -name "*.o" -exec rm {} \;

To find and delete files matching a criteria but not another

	find . -depth -name "*.pdf" -prune -not -name "*graded.pdf" -delete


From: [rushi.wordpress.com/2008/08/05/find-replace-across-multiple-files-in-linux/](http://rushi.wordpress.com/2008/08/05/find-replace-across-multiple-files-in-linux/))

	find . -name "*.cpp" -print | xargs sed -i 's/jose/jaabell/g'


Find recently changed files

 	find -mtime 0 -type f -print

Find where apt-get installs things

	sudo dpkg -L packagename

Killing a screen session

	screen -X -S [session # you want to kill] quit


Deleting lines from file matching a criteria
	
	sed '/pattern to match/d' ./infile

Control volume from command line

	amixer -D pulse sset Master 100%

Find and delete all broken symlinks in a folder

	find . -xtype l -delete

List folders by space utilized

    du -hs * | sort -h


Networking
---------------------------------------------------------------------------------------------------

Setting IP address from Command Line:

	
	sudo ifconfig eth0   192.168.0.1 netmask 255.255.255.0



Linux system setup
---------------------------------------------------------------------------------------------------

###Printer

Don't use gnome app, simply use

	system-config-printer

View printing queue from command line

	lpq

Cancel a job

	lprm


Encrypt and decrypt files

    Encrypt
      openssl enc -aes-256-cbc -e > out.tar.gz.enc
    Decrypt
      openssl enc aes-256-cbc -d -in out.tar.gz.enc | tar xz



Git Management
---------------------------------------------------------------------------------------------------


Create and checkout a local branch and set it up to track a remote branch

	git checkout -b master -t origin/master
	
Where `origin/master` is a remote branch.


Git history cleanup:

	git gc --aggressive
	
Adding a branch

	git push <remote-name> <branch-name>

Formally git push <remote-name> <local-branch-name>:<remote-branch-name>
But when you omit one, it assumes both names are the same. Do:
	
	git push -u <remote-name> <branch-name> 

 So that a subsequent git pull will know what to do (set upstream tracking)


Setting up a non-empty folder to be a git repo

	cd <localdir>
	git init
	git add .
	git commit -m 'message'
	git remote add origin <url>
	git push -u origin master

Setting up upstream in GitHub

	git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY

Verify

	git remote -v


SSH Tricks
---------------------------------------------------------------------------------------------------

###Shutdown a frozen SSH session. Press :

    [Enter]
    ~
    .

Proceed to resume happyness.

###Tunnelling all traffic through SSH tunnel

Use `sshuttle`. 

	sshuttle -r essi 0/0 -vv


Managing gitolite
---------------------------------------------------------------------------------------------------

Checkout the gitolite admin repo:

	git clone git@powa:gitolite-admin gadmin

To add a user SSH key do the following:

- Add it to the keydir
- Multiple keys for same user either in subfolders or using @ ie. equivalently
	+ `jose@home.pub`
	+ `home/jose.pub`

- Stage it and commit it

		git add . 
		git commit -m "message"

- Push to the gitolite repo
	
		git push

Changing admin settings

- Open the file `gitolite-admin/cong/gitolite.conf`

- Make changes, commit and push

		git commit -am "message"
		git push

If directly changing stuff in the gitolite server (ie. logging in through ssh into the git user)

- Remember to use:

		ssh (myusername)@powa.engr.ucdavis.edu
		su git  [input the typical CompGeoMech password]
	 
- Make some changes and then 

		gl-setup
		gl-admin-push

To add a new repo:

- Add a new line into  the `conf/gitolite.conf` file
- Push changes into gitolite
- Pull the new (empty) repo
- Add stuff to it and push
- Good to go!

	



Python cool stuff
---------------------------------------------------------------------------------------------------

### Iteration awesomeness.

Define,

	a = ['a1', 'a2', 'a3']
	b = ['b1', 'b2']

will iterate 3 times, the last iteration, b will be None.

	print "Map:"
	for x, y in map(None, a, b):
	  print x, y

will iterate 2 times,
the third value of a will not be used

	print "Zip:"
	for x, y in zip(a, b):
	  print x, y

will iterate 6 times,
it will iterate over each b, for each a
producing a slightly different output

	print "List:"
	for x, y in [(x,y) for x in a for y in b]:
	    print x, y


### IPython Notebook

Install pip
	
	sudo apt-get install python-pip
	sudo pip install ipython --upgrade
	sudo pip install ipython[notebook]


### IPython Notebook server

#### Installation 

	sudo apt-get install ipython-notebook

#### Setup

	ipython
	from IPython.lib import passwd
	passwd()

	#Enter passwd
	#u'sha1:e6356b6e0ee8:1906d7f56995bc18925c4af976ac3a588bc10913'

Create an SSL certificate to encrypt session
	openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem

Edit `ipython_notebook_config.py` to look something like this

	c = get_config()
	c.NotebookApp.open_browser = False
	c.NotebookApp.port = 16562
	c.NotebookApp.certfile = u'/home/jaabell/ipython_notebook_ssl_certificate.pem'
	c.NotebookApp.password = u'sha1:e6356b6e0ee8:1906d7f56995bc18925c4af976ac3a588bc10913'
	c.IPKernelApp.ip = u'*'
	c.IPKernelApp.pylab = 'inline'
	c.FileNotebookManager.notebook_dir = u'/home/jaabell/www/blog/content/ipython_notebooks'

Create a profile for the server

	ipython profile create nbserver

Edit `~/.config/ipython/profile_nbserver/ipython_notebook_config.py`

Run the server 

	 ipython notebook --profile=nbserver

Keep the server alive with `supervisor`

	sudo apt-get install supervisor





C++ 
---------------------------------------------------------------------------------------------------


To view contents of a static library (*.a) 

	nm -C <PATH_TO_LIB>.a > contents.txt

The `-C` flag is for C++.

To search a bunch of libraries for a specific function:

	for lib in $(find $PATH -name \*.a) ; do echo $lib ; nm $lib | grep "specific_function" | grep -v " U "   ; done


Profiling....

After running a program compile with -g -pg the call graph can be visualized with gprof2dot.py and
xdot (or dot).

	gprof ~/bin/essi_semidebug | gprof2dot.py | dot -Tdot -o output.dot
	xdot output.dot

or just create a png

	gprof ~/bin/essi_semidebug | gprof2dot.py | dot -Tpng -o output.png


MVAPICH stuff
---------------------------------------------------------------------------------------------------


Compile MVAPICH2 with message queue debugging.

	./configure --prefix=".." --enable-debuginfo --disable-mcast

Get `libnuma` to do optimization for NUMA architechtures.

	sudo apt-get install libnuma-dev

OpenMPI
---------------------------------------------------------------------------------------------------

To use a different compiler with mpicc and mpic++
    export OMPI_CC=clang
    export OMPI_CPP=clang++



MPI Performance
---------------------------------------------------------------------------------------------------


### VampirTrace

Need to try this out. Its supposed to be good. 


###mpiP

Get from http://mpip.sourceforge.net/

Requires libunwind, binutils and libiberty

	sudo apt-get install libunwind8 libunwind8-dev binutils-dev libiberty-dev

Configure

	./configure --enable-collective-report-default --enable-demangling=GNU --with-cc=mpicc --with-cxx=mpic++ --with-f77=mpif77 --prefix=/usr/local 
	make -j 24
	sudo make install

If all good 
	ll /usr/local/lib/libmp* 
should return 
	/usr/local/lib/libmpiP.a

Append to code at linktime the following flags

	-lmpiP -lbfd -liberty -lunwind

Possibly also the place where libmpiP.a is available throught the -L option. Ie. for above `-L/usr/local`... unnecesarry. 



###HPCToolkit

Monitor and profile performance counters through PAPI interaface. 
Has nice viewer, apparently. 

####Building and installation
From http://hpctoolkit.org/. Checkout both hpctoolkit and hpctoolkit-externalsL:

	svn co http://hpctoolkit.googlecode.com/svn/trunk hpctoolkit
	svn co http://hpctoolkit.googlecode.com/svn/externals hpctoolkit-externals

Build externals (prefix set to a local dir):

	cd hpctoolkit-externals
	mkdir BUILD && cd BUILD
	../configure CC=gcc CXX=g++ --prefix=/home/jaabell/Programs/local/
	make -j 8
	make install
	make clean

Build the toolkit. On ubuntu 14.04 libpapi is located on /usr/lib/x86_64-linux-gnu, make links into /usr/lib for this to work. 

	cd hpctoolkit
	mkdir BUILD && cd BUILD
	../configure CC=gcc CXX=g++ MPICXX=mpic++ --prefix=/usr/local --with-externals=/home/jaabell/Programs/local --with-papi=/usr/
	make -j 8
	sudo make install -j 8

####Usage

Figure out list of PAPI events:

	papi_avail 

Some interesting ones for me, that were available on my laptop

	PAPI_L1_DCM  : Level 1 data cache misses
	PAPI_L2_DCM  : Level 2 data cache misses
	PAPI_L3_DCM  : Level 3 data cache misses
	PAPI_TLB_DM  : Data translation lookaside buffer misses
	PAPI_FP_INS  : Floating point instructions
	PAPI_TOT_CYC : Total cycles
	PAPI_FP_OPS  : Floating point operations
	PAPI_VEC_DP  : Double precision vector/SIMD instructions

Can also get a list of events (PAPI and native) using -L option

	hpcrun -L essi > HPCeventlist.txt


Run application through `hpcrun` (this worked on nagoy)

	hpcrun \
    -e PAPI_L1_DCM@5300013 \
    -e PAPI_L2_DCM@5300013 \
    -e PAPI_TOT_CYC@5300013 \
    -e PAPI_FP_OPS@5300013 \
    essi -nf <file>


###Perfsuite

Provides a simple command-line interface into performance counters.

Get from 

http://perfsuite.ncsa.illinois.edu/

#### Build

Requires PAPI library libpapi.a to be in a reasonable locations. See HPCToolkit.

	./configure --prefix=/usr/local/ --with-papi=/usr
	make -j 16
	sudo make install



HPC
---------------------------------------------------------------------------------------------------

###Tuning BLAS and LAPACK with ATLAS

### Pre-steps

TURN OFF AUTO CPU SCALING!!


Install cpufrequtils:

	sudo apt-get install cpufrequtils

Then edit the following file (if it doesn't exist, create it):

	sudo nano /etc/default/cpufrequtils

And add the following line to it:

	GOVERNOR="performance"

Save and exit.

If you need performance, do:

	sudo /etc/init.d/cpufrequtils restart

###Finding out "real" CPUS from hyperthreading ones


On my laptop Intel(R) Core(TM) i7-2630QM CPU @ 2.00GHz

Look at `cat /proc/cpuinfo` and look at the core ids. Pick processors which are on different cores.

	--force-tids="4 0 1 2 3"

### Using ATLAS


Now to tune BLAS and LAPACK with ATLAS....

	mv ATLAS ATLAS3.10.x
	cd ATLAS3.10.x
	mkdir linux_x86_64_intel_i7_laptop
	cd linux_x86_64_intel_i7_laptop
	../configure -b 64 -D c -DPentiumCPS=2000 --prefix=/home/jaabell/Programs/lib  --with-netlib-lapack-tarfile=/home/jaabell/Programs/lapack-3.5.0.tgz --force-tids="4 0 1 2 3"

Explanation `-b` is the pointer bitwidth, `-D c -DPentiumCPS=2000` sets the CPU clock rate so that
ATLAS can use CPU cycles for timing, `--prefix` where to install, `-with-netlib-lapack-tarfile=` where is the lapack tarball, and `--force-tids="4 0 1 2 3"` tells
ATLAS to only use those core ids given (first number is the number of cores to use).

	make build   # tune & build lib
	make check   # sanity check correct answer
	make ptcheck # sanity check parallel
	make time    # check if lib is fast
	make install # copy libs to install dir



### SparseSuite

FOr UMFPACK

Edit SuiteSparse_config.mk. I added:

Compilers...
	CC = gcc
	CXX = g++
	TARGET_ARCH = -march=native
	AR = gcc-ar

Installation...
	INSTALL_LIB = /home/jaabell/Programs/lib
	INSTALL_INCLUDE = /home/jaabell/Programs/include

BLAS and LAPACK come from ATLAS...
	ESSI_DEPEND_DIR = /home/jaabell/Repositories/essi_dependencies
	BLAS = $(ESSI_DEPEND_DIR)/lib/libcblas.a $(ESSI_DEPEND_DIR)/lib/libf77blas.a $(ESSI_DEPEND_DIR)/lib/libatlas.a -lgfortran
	LAPACK = $(ESSI_DEPEND_DIR)/lib/liblapack.a




Other cool stuff
---------------------------------------------------------------------------------------------------

### Making videos of stuff

#### Screen capture / streaming / making desktop videos with audio

 - on bin/recordscreen (python script)

     see recordscreen --help

 - kazam (sudo apt-get install kazam)


#### Making a movie from separate png images.

Avconv:
	
	avconv -r 60 -i movie%04d.png  movie.mp4

The options are

* `qscale 5`...  **seems to be deprecated** define fixed video quantizer scale (VBR) where 1 is the best and 31 the worst. Since mpeg/jpeg has problems to compress line graphics it’s a good idea to set this variable close to 1. You get a big movie file, but otherwise the movie doesn’t look, well, that good. 
* `r`: framerate
* `b`: video bitrate
* `i`: input files, `%04d` says that we have four numbers in the filename where the number is filled with zeros left of it.
`movie.mp4` is the filename, the extension says that it is a quicktime movie. You can also create a Macromedia Flash movie by using the .flv extension.

to get higher quality (play with `crf parameter` = 1 (best) = 31 (worst))

 	avconv -r 60 -i movie%04d.png -c:v libx264 -crf 2 ../../movie_2_npps.mp4

for non-even sized movies a little trick should be played:

	avconv -r 60 -i movie%04d.png  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" movie.mp4

Explanation for `-vf` parameter, from StackOverflow

Basically the issue stems from a bug(?) in libx264 where it complains if the width or height is not an even number. This is weird in the case where I don't want to perform any scaling at all. So the command above will:

* Divide the original height and width by 2
* Round it down to the nearest pixel
* Multiply it by 2 again, thus making it an even number 

To get it to work on adobe reader use h264 encoder!

	avconv -i source -c:v h264 -c:a copy out.mkv
	avconv -i source -c:v libx264 -c:a copy out.mkv

To stick together two videos side by side

	avconv -i movie_left.mp4 -vf "[in] scale=trunc(iw/2)*2:trunc(ih/2)*2, pad=2*iw:ih [left];     movie=movie_right.mp4, scale=trunc(iw/2)*2:trunc(ih/2)*2 [right];     [left][right] overlay=main_w/2:0 [out]"  Output.mp4





Debugging!
---------------------------------------------------------------------------------------------------
On Ubuntu `gdb` attaching to processes is forbidden... because hackers. To allow:

	echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope

To permanently allow it edit `/etc/sysctl.d/10-ptrace.conf` and change the line:

	kernel.yama.ptrace_scope = 1

To read

	kernel.yama.ptrace_scope = 0





Website Management (with pelican)
---------------------------------------------------------------------------------------------------

Install pelican using tutorials in website.

Setup:
	sudo apt-get install python-pip 
	sudo pip install pelican fabric
	sudo pip install pelican markdown typogrify pelican_youtube ipython

Use fabric or make to build

Using vitualenv

	virtualenv ~/virtualenvs/pelican
	cd ~/virtualenvs/pelican
	. bin/activate


Download the [ipythonnb plugin][https://github.com/danielfrg/pelican-ipythonnb]

	git clone https://github.com/danielfrg/pelican-ipythonnb.git

Will need [pandoc](http://johnmacfarlane.net/pandoc/) 

	sudo apt-get install pandoc pandoc-citeproc



Apache management
---------------------------------------------------------------------------------------------------

Once apache is running

To create a new website

* Create a new virtual host inside `sites-available`. Here is the code for my website:

	<VirtualHost *>
	      ServerAdmin ja.abell@gmail.com
	      ServerName www.joseabell.com
	      DocumentRoot /var/www/joseabell.com/
	      <Directory />
	              Options FollowSymLinks
	              AllowOverride None
	      </Directory>
	      <Directory /var/www/joseabell.com/>
	              Options Indexes FollowSymLinks MultiViews
	              AllowOverride None
	              Order allow,deny
	              allow from all
	      </Directory>
	</VirtualHost>

* Link from `sites-available` to `sites-enabled`

* Restart Apache

	/etc/init.d/apache2 restart




Tweaks to .bashrc 
---------------------------------------------------------------------------------------------------

Add screen name to prompt

	#For screen
	if [ "$TERM" = screen ]; then
	    PS1="(screen,$STY)\n$PS1"
	fi



Make terminals solarized
---------------------------------------------------------------------------------------------------
	cd
	wget --no-check-certificate https://raw.github.com/seebi/dircolors-solarized/master/dircolors.ansi-	dark
	mv dircolors.ansi-dark .dircolors
	eval `dircolors ~/.dircolors`
	
	cd
	wget --no-check-certificate https://raw.github.com/seebi/dircolors-solarized/master/dircolors.ansi-	light
	mv dircolors.ansi-light .dircolors
	eval `dircolors ~/.dircolors`
	
	sudo apt-get install git-core
	git clone https://github.com/sigurdga/gnome-terminal-colors-solarized.git
	cd gnome-terminal-colors-solarized
	
	./set_dark.sh
	./set_light.sh




VisIt tricks
---------------------------------------------------------------------------------------------------

### Make window a given size

Save a session file, and edit these lines to achieve desired res:

    <Field name="windowSize" type="intArray" length="2">1024 828 </Field>
    <Field name="windowImageSize" type="intArray" length="2">1024 768 </Field>
    <Field name="windowLocation" type="intArray" length="2">719 133 </Field>




HDF5 Tricks
---------------------------------------------------------------------------------------------------

### Dump part of an array 

`h5dump` can be used to output portions of an HDF5 file into text, binary or other HDF5 files. 

**Example 1** Dump 1000 timesteps of the first row of generalized displacements in FILENAME.h5.feioutput. 

    h5dump -d "/Model/Nodes/Generalized_Displacements" --start="0,0" --count="1,1000" FILENAME.h5.feioutput

### Repacking an HDF5 file

Repacking is useful to change chunking layout or add filters (such as compression) after the file
has been created.

**Example 1**  Change the chunking for the generalized displacements dataset to be 10x20. Do:

	h5repack -v -l "/Model/Nodes/Generalized_Displacements":CHUNK=10x20 FILENAME_IN.h5.feioutput FILENAME_OUT.h5.feioutput

**Example 2** Apply the best compression (GZIP) to all arrays in a file:

	h5repack -v -f GZIP=9 FILENAME_IN.h5.feioutput  FILENAME_IN.h5.gzip.feioutput 
