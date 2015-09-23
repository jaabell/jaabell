Title: Useful Commands
Slug: useful-commands
Date: 2014-06-25 15:10:25
Tags: 
Category: 
Author: jaabell
Lang: 
Summary: 
status: hidden




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







Other cool stuff
---------------------------------------------------------------------------------------------------

### Making videos of stuff

#### Screen capture / streaming / making desktop videos with audio

 - on bin/recordscreen (python script)

     see recordscreen --help

 - kazam (sudo apt-get install kazam)


#### Making a movie from separate png images.

 (From [here](http://www.miscdebris.net/blog/2008/04/28/create-a-movie-file-from-single-image-files-png-jpegs/))

	ffmpeg -qscale 5 -r 20 -b 9600 -i img%04d.png movie.mp4

The options are

* `qscale 5`...  define fixed video quantizer scale (VBR) where 1 is the best and 31 the worst. Since mpeg/jpeg has problems to compress line graphics it’s a good idea to set this variable close to 1. You get a big movie file, but otherwise the movie doesn’t look, well, that good.
* `r`: framerate
* `b`: video bitrate
* `i`: input files, `%04d` says that we have four numbers in the filename where the number is filled with zeros left of it.

`movie.mp4` is the filename, the extension says that it is a quicktime movie. You can also create a Macromedia Flash movie by using the .flv extension.



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

	sudo apt-get install pandoc pandoc-cite



Apache management
---------------------------------------------------------------------------------------------------

Once apache is running

To create a new website

* Create a new virtual host inside `sites-available`. Here is the code for my website:

	<VirtualHost *>
	      ServerAdmin ja.abell@gmail.co,
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

