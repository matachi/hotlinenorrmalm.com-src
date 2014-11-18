#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'Hotline Norrmalm'
SITEURL = 'http://hotlinenorrmalm.com'
# Use an empty string when running it locally
#SITEURL = ''
PATH = 'content'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10

ARTICLE_URL      = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS  = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL         = '{slug}/'
PAGE_SAVE_AS     = '{slug}/index.html'
DRAFT_URL        = 'drafts/{slug}/'
DRAFT_SAVE_AS    = 'drafts/{slug}/index.html'
CATEGORY_URL     = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL          = 'tag/{slug}/'
TAG_SAVE_AS      = 'tag/{slug}/index.html'
AUTHOR_URL       = 'author/{slug}/'
AUTHOR_SAVE_AS   = 'author/{slug}/index.html'

CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

THEME = 'themes/norrmalm'

FOOTER_CONTENT = '''
Copyright © 2014 Daniel Jonsson.<br>
All content is licensend under <a hreft="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International</a>.

'''
