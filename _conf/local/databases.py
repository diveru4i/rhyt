# -*- coding: utf-8 -*-
from core import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'rhyt',                      # Or path to database file if using sqlite3.
            'TEST_CHARSET': "utf8",
            'TEST_COLLATION': "utf8_general_ci",
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
            # 'OPTIONS': {
            #     'init_command': 'SET storage_engine=MyISAM',
            #  }
    }
}

CACHES = {
    'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT': 900,
    }
}
