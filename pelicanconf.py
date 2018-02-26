#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jose Abell'
SITENAME = u'Jose Abell\'s Research Blog'
SITEURL = 'http://www.joseabell.com'
SITEURL_ABS = SITEURL

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# THEME = "../pelican-themes/svbtle"
THEME = "../blogtheme"

DISQUS_USERNAME = "joseabell"
DISQUS_SITENAME = "www.joseabell.com"
DISQUSURL = 'http://www.joseabell.com'

GITHUB_URL = "https://github.com/jaabell"

DEFAULT_HEADER_BG = "/images/header.png"

STATIC_PATHS = [
    'images', 'pdfs', 'extra/CNAME'
    ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Fonts look nicer?
TYPOGRIFY = True
# TYPOGRIFY = False

#Plugins 
PLUGIN_PATHS = ['/home/jaabell/www/pelican-plugins']
PLUGINS = ["pelican_youtube", "ipythonnb.markup", "render_math", "representative_image"]
MARKUP = ('md', 'ipynb')
IGNORE_FILES = ['*checkpoint.ipynb']


#Enable TOC generation in markdown
# MD_EXTENSIONS =  [ 'toc'] #, 'codehilite','extra']
# MARKDOWN =  ['toc'] #, 'codehilite','extra']
# MD_EXTENSIONS = MARKDOWN
MARKDOWN = {}

#Tweak maths
macros = ['/home/jaabell/www/blog/latex-macros.tex']
MATH_JAX = {'color': 'gray', 'align': 'left', 'macros': macros, 'process_summary': True}


SUMMARY_MAX_LENGTH = 100
