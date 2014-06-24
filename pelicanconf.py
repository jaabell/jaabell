#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jose Abell'
SITENAME = u'Jose Abell\'s Research Blog'
# SITEURL = 'www.joseabell.com'

TIMEZONE = 'CA'

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

DISQUS_SITENAME = "joseabell"
DISQUS_SITENAME = "www.joseabell.com"

GITHUB_URL = "https://github.com/jaabell"

DEFAULT_HEADER_BG = "/images/header.png"

STATIC_PATHS = [
    'images', 'pdfs'
    ]

DISPLAY_PAGES_ON_MENU = True

 # My blue 
# ABOUT_PAGE = "/pages/welcome.html"
# RESEARCH_PAGE = "/pages/research.html"
# TEACHING_PAGE = "/pages/teaching.html"
# TOOLS_PAGE = "/pages/tools.html"
# CV_PAGE = "/pages/cv.html"
# PUBS_PAGE = "/pages/publications.html"
# LINKS_PAGE = "/pages/links.html"



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


TYPOGRIFY = True

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ["latex", "pelican_youtube"]