#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dormouse.Young'
AUTHOR_EMAIL = 'dormouse.young@gmail.com'
SITENAME = 'Dormouse Hole'
SITEURL = 'https://dormouse.github.io'
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

SOCIAL = (('GitHub', 'http://github.com/username'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# All theme setting
PLUGIN_PATHS = ['pelican-plugins']

# pelican-bootstrap3 theme setting
# More setting see:
# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = 'pelican-themes/pelican-bootstrap3'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

PLUGINS = ['i18n_subsites', 'tag_cloud', 'tipue_search']
SHOW_DATE_MODIFIED = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
