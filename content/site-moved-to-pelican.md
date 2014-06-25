Title: Site now powered by pelican!
Slug: site-moved-to-pelican
Date: 2014-06-24 10:48:59
Tags: pelican, blog, hacker
Category: Tools
Author: jaabell
Lang: en

I finally completed the transition from WordPress to [Pelican][]. The moment was right. Pelican is more
appropriate for me as it is much simpler to manage (I host my own webpage), more flexible in terms
of what I can do with the blog, requires no php or database knowledge. 

Pelican is a python powered static HTML generator. I set-up a heierarchy of folders where I store
my content. Web content is generated using the Markdown text syntax. Pelican uses these [markdown][]
files and the folder structure to generate the website HTML. 

Static HTML has some advantages over a database with server-side logic based website. The most
important for me is speed and low memory usage, because I want to host my own website. 

Also, it makes it easier to share code as I can include code snippets directly in the markdown text
file and it gets highlighted using pygments (python module).

Thanks to [this][http://danielfrg.com/blog/2013/02/16/blogging-pelican-ipython-notebook/] I can
also now (to do) use python notebooks to blog directly. This is a nice feature as I will be
blogging mainly about scientific computing, showing some example here and there and such.

Finally, I can version control the website using [git][http://git-scm.com/] and automate site
updating using a git-hook on the server (thank [this post][http://www.textandhubris.com/automate-pelican-with-git.html]).
This means I can clone my git repo, make changes and push them and the server will automatically
generate the website and deploy it!

I love pelican!



  [pelican]: www.getpelican.com
  [markdown]: http://daringfireball.net/projects/markdown/
