#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jose Abell'
SITENAME = u'Jose Abells Reasearch Blog'
SITEURL = ''
# SITEURL_ABS = SITEURL


PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
ARTICLE_URL = 'posts/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}.html'
TIMEZONE = 'US/Pacific'


GITHUB_URL = "https://github.com/jaabell"

USE_FOLDER_AS_CATEGORY = True


ABOUT = {}

STATIC_PATHS = [
    'images', 'pdfs', 'extra/CNAME', 'favicon.ico'
    ]

#Enable TOC generation in markdown
# MD_EXTENSIONS =  [ 'toc'] #, 'codehilite','extra']
# MARKDOWN =  ['toc'] #, 'codehilite','extra']
# MD_EXTENSIONS = MARKDOWN
# MARKDOWN = {}
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # 'markdown.extensions.mdx_include': {},
    },
    'extensions':['mdx_include'],
    'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
  ('Github', 'https://www.github.com/jaabell'),
  # ('Twitter', 'https://www.twitter.com/RealJoseAbell'),
  # ('Instagram', 'https://www.instagram.com/ja.abell'),
  ('Youtube', 'https://www.youtube.com/c/JoseAAbellM'),
  ('researchgate', 'https://www.researchgate.net/profile/Jose_Abell/'),
  ('linkedin', 'linkedin.com/in/josé-abell-93194129')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ("rst", "md", "ipynb")

from pelican_jupyter import markup as nb_markup

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = [
  'i18n_subsites', 
  'tipue_search', 
  'render_math', 
  'summary', 
  'representative_image', 
  'pelican_fontawesome',
  nb_markup]#, 'better_figures_and_images']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}



# IPYNB_MARKUP_USE_FIRST_CELL = False

IGNORE_FILES = [".ipynb_checkpoints"]



I18N_GETTEXT_LOCALEDIR = '../blog2theme/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US.utf8'
DEFAULT_LANG = u'en'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.utf8'

LOGO = "/images/sitelogo.svg"



DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
# PAGE_ORDER_BY = 'order'

MENUITEMS = [
  # ('Archive', 'archives.html'),
  # ('Contact', 'contact.html')
]



THEME = "../blog2theme"

MATH_JAX = {
	'color': 'gray',
	'align': 'left', 
	'process_summary': True, 
	'tex_extensions': ['color.js','mhchem.js']
	}

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]


# i18n
I18N_SUBSITES = {
  # 'es': {
  #   'PAGE_PATHS': ['pages/es'],
  #   'ARTICLE_PATHS': ['blog/es'],
  #   'LOCALE': 'es_CL'
  # }
}


# special content
HERO = [
  {
    'image': '/images/hero/uandes-fm-above.jpg',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'José Abell\'s Research Blog',
      # 'es': 'Contenido especial'
    },
    'text': {
      'en': 'Numerical modeling in engineering | Earthquakes | HPC | OpenSource',
      # 'es': 'Esto es para sacar pica'
    },
    # 'links': [
    #   {
    #     'icon': 'icon-code',
    #     'url': 'https://github.com/claudio-walser/pelican-fh5co-marble',
    #     'text': 'Github'
    #   },
    #   {
    #     'icon': 'icon-code',
    #     'url': 'https://github.com/claudio-walser/pelican-fh5co-marble',
    #     'text': 'Github'
    #   }
    # ]
  }, {
    'image': '/images/hero/playa.jpg',
    'title': {
      'en':'José Abell\'s Research Blog',
    },
    'text': {
      'en': 'Numerical modeling in engineering | Earthquakes | HPC | OpenSource',
      }
  }, {
    'image': '/images/hero/chilly1.jpg',
    'title': {
      'en':'José Abell\'s Research Blog',
    },
    'text': {
      'en': 'Numerical modeling in engineering | Earthquakes | HPC | OpenSource',
      }
  }, {
    'image': '/images/hero/chilly2.jpg',
    'title': {
      'en':'José Abell\'s Research Blog',
    },
    'text': {
      'en': 'Numerical modeling in engineering | Earthquakes | HPC | OpenSource',
      }
  }
  # , {
  #   'image': '/images/hero/background-3.jpg',
  #   'title': 'No Blogroll yet',
  #   'text': 'Because of space issues in the man-nav, i didnt implemented Blogroll links yet.',
  #   'links': []
  # }, {
  #   'image': '/images/hero/background-4.jpg',
  #   'title': 'Ads missing as well',
  #   'text': 'And since i hate any ads, this is not implemented as well',
  #   'links': []
  # }
]


# SUMMARY_BEGIN_MARKER = "<!-- SUMMARY BEGIN -->"
# SUMMARY_END_MARKER = "<!-- SUMMARY END -->"
# SUMMARY_USE_FIRST_PARAGRAPH  = True
SUMMARY_MAX_LENGTH = 10

OUTPUT_PATH = "output"

# DISQUS_USERNAME = "joseabell"
DISQUS_SITENAME = "joseabell"
# DISQUSURL = 'http://www.joseabell.com'

RESPONSIVE_IMAGES = True