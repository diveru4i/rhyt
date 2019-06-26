# -*- coding: utf-8 -*-
import hashlib
import locale
import random
import string
import sys
import threading
from contextlib import contextmanager
from uuid import uuid4

try:
    import pymorphy2
except ImportError:
    pass
from hashids import Hashids

from wagtail.core.models import Page

from django.conf import settings
from django.core.cache import cache
from django.urls import reverse


class FakePage:
    is_fake = True

    def __init__(self, title, url='/', depth=1, **kwargs):
        self.title = title
        self.url = url
        self.depth = 1
        self.queryset = Page.objects.none()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_title(self):
        return self.title

    def get_children(self):
        return self.queryset

    def get_ancestors(self):
        return self.queryset


def flatter(arr, distinct=False):
    arr = [item for sublist in arr for item in sublist]
    return list(set(arr)) if distinct else arr


def splitter(arr, n=0):
    arr = list(arr)
    if not n:
        n = len(arr) // 2
        if len(arr) % 2:
            n += 1
    return [arr[i:i+n] for i in range(0, len(arr), n)]


def morph_plural(word, number):
    if sys.version_info[0] == 3 and sys.version_info[1] == 7:
        return word
    morph = pymorphy2.MorphAnalyzer()
    w = morph.parse(word.lower())[0]
    try:
        return w.make_agree_with_number(number).word
    except AttributeError:
        return word


def morph_case(word, case='gent', gender='masc'):
    '''
    nomn    именительный    Кто? Что?
    gent    родительный     Кого? Чего?
    datv    дательный       Кому? Чему?
    accs    винительный     Кого? Что?
    ablt    творительный    Кем? Чем?
    loct    предложный      О ком? О чём?
    '''
    if sys.version_info[0] == 3 and sys.version_info[1] == 7:
        return word
    morph = pymorphy2.MorphAnalyzer()
    w = morph.parse(word.lower())[0]
    try:
        return w.inflect({case, gender}).word
    except AttributeError:
        return word


def morph_gender(word, base_word):
    morph = pymorphy2.MorphAnalyzer()
    gender = morph.parse(base_word.lower())[0].tag.gender
    w = morph.parse(word.lower())[0]
    try:
        return w.inflect({gender}).word
    except AttributeError:
        return word


def cache_data(funct, cache_time=60*60, cache_key=None):
    if not cache_key:
        cache_key = str(funct.__hash__())
    cache_lock_key = 'lock::%s' % cache_key
    while cache.get(cache_lock_key):
        time.sleep(0.314)
    data = cache.get(cache_key) or None
    if not data:
        cache.set(cache_lock_key, True)
        data = funct()
        if cache.get(cache_lock_key):
            cache.set(cache_key, data, cache_time)
            cache.delete(cache_lock_key)
    return data


def toint(item):
    try:
        return int(item)
    except (TypeError, ValueError):
        return 0


def gen_random_string(n=10, symbols='all'):
    # if symbols not in ['all', 'digits', 'letters']
    try:
        symbols = {
            'all': lambda: string.ascii_lowercase + string.digits,
            'digits': lambda: string.digits,
            'letters': lambda: string.ascii_lowercase
        }[symbols]()
    except KeyError:
        raise AttributeError(u'The "symbols" param can be: ("all", "digits", "letters") ')
    arr = [random.SystemRandom().choice(symbols) for _ in range(n)]
    return ''.join(arr)


def get_uuid():
    return str(uuid4()).replace('-', '')


def get_admin_url(obj):
    return reverse('admin:{0}_{1}_change'.format(obj._meta.app_label, type(obj).__name__.lower()), args=[obj.id])


def get_wagtailadmin_url(obj):
    return '{3}{0}/{1}/edit/{2}/'.format(obj._meta.app_label, type(obj).__name__.lower(), obj.id, reverse('wagtailadmin_home'))


def get_hashids(min_length=5):
    return Hashids(salt=settings.SECRET_KEY, min_length=min_length)


LOCALE_LOCK = threading.Lock()


@contextmanager
def setlocale(name='ru_RU.UTF-8'):
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)
