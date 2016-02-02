#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Terrence'
SITENAME = u"小祈和小翼的空间站"
SITEURL = 'http://inority.com'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Github', 'https://github.com/stdrickforce'),
    ('微博', 'http://weibo.com/3752876962'),
    ('知乎', 'https://www.zhihu.com/people/fan-teng-yuan')
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extra']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {
        'path': 'CNAME',
    }
}

THEME = 'Flex'

MAIN_MENU = True

SITETITLE = 'Terrence'
SITESUBTITLE = 'Web Developer (范腾远)'
SITELOGO = SITEURL + '/extra/inori.jpeg'
