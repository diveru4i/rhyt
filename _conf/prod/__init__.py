# -*- coding: utf-8 -*-
from _conf.core import *


DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'opirogova',
        'TEST_CHARSET': "utf8mb4",
        'TEST_COLLATION': "utf8mb4_general_ci",
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11221',
        'TIMEOUT': 900,
    }
}


ALLOWED_HOSTS = [
    '127.0.0.1',
    '.localhost',
    '.opirogova.ru',
]
