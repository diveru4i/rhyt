# -*- coding: utf-8 -*-
from django.core.cache import caches
from django.core.cache.backends.base import InvalidCacheBackendError
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-c', type=str, default='default')

    def handle(self, *args, **kwargs):
        try:
            cache = caches[kwargs['c']]
            cache.clear()
            print('Cache has been cleared: %s' % kwargs['c'])
        except InvalidCacheBackendError:
            print("There's no such cache: %s" % kwargs['c'])


