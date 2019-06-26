# -*- coding: utf-8 -*-
import datetime
import importlib
import random
import re
import hashlib
import unidecode
import urllib

from typograf.views import typo

from wagtail.core.models import Page

from django import template
from django.conf import settings
try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse
from django.db.models import Q
from django.db.models.query import QuerySet
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from _melfi import morph_plural, morph_gender, morph_case, splitter, toint, get_admin_url, get_hashids


register = template.Library()


@register.simple_tag
def plural(word, count, only_word=False):
    word = morph_plural(word, count)
    if only_word:
        return word
    return u'{0} {1}'.format(count, word)


@register.simple_tag
def gender(word, base_word):
    return morph_gender(word, base_word)


@register.simple_tag
def case(word, case='gent', gender='masc'):
    return morph_case(word, case, gender)


@register.filter
def verbose_number(amount):
    if type(amount) != 'str':
        amount = str(amount)
    orig = amount
    new = re.sub("^(-?\d+)(\d{3})", '\g<1> \g<2>', amount)
    if orig == new:
        return new
    else:
        return verbose_number(new)


@register.simple_tag
def get_string(request, **kwargs):
    kwargs_string = u''.join([u'&{0}={1}'.format(key, value) for key, value in kwargs.items()])
    get_string = u'&'.join([u'{0}={1}'.format(key, urllib.request.quote(item.encode('utf8'))) for key in request.GET.keys() for item in request.GET.getlist(key) if key not in kwargs.keys()])
    get_string = '?{0}{1}'.format(get_string, kwargs_string) if get_string else '?%s' % kwargs_string[1:]
    return get_string


@register.filter
def getlist(request, param):
    return request.GET.getlist(param)


@register.simple_tag
def get_archive_size(files):
    return reduce(lambda size1, size2: size1 + size2, [f.file.size for f in files]) if files else 0


@register.filter
def parse_file_size(size):
    if not size:
        return '0 Kb'
    size = int(size)
    if size > 1024000:
        return u'%.2f Mb' % float(size/1024000)
    else:
        return u'%d Kb' % int(size/1024)


@register.filter
def file_extension(filename):
    if not filename:
        return '–'
    return filename.split('.')[-1].upper()


@register.filter
def strptime(value, pattern):
    return datetime.datetime.strptime(str(value), pattern)


@register.filter
def verbose_name(string):
    return string.split(' ')[-1]


@register.simple_tag
def is_new(obj, request, cookie_name):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=7)
    if obj.datetime < (now - delta):
        return False
    cookie = request.get_signed_cookie(cookie_name, default=None)
    if cookie:
        ids_from_cookie = [int(id) for id in cookie.split(',')]
    else:
        ids_from_cookie = list()
    if obj.id in ids_from_cookie:
        return False
    return True


@register.filter
def split(var, val='\r\n'):
    return var.split(val)


@register.simple_tag
def assign(val):
    return val


@register.filter
def to_str(val):
    return str(val)


@register.filter
def to_int(value):
    return toint(value)


@register.filter
def norm_phone(phone):
    if not phone:
        return ''
    norm = u''.join(re.findall('\d', phone))
    if not norm.startswith('7'):
        norm = '7' + norm.lstrip('8')
    if len(norm) > 11:
        norm = norm[:11]
    elif len(norm) < 11:
        norm = norm + '0' * (11 - len(norm))
    return '+' + norm[:11]


@register.filter
def phone_verbose(phone):
    phone = phone.strip()
    if phone.startswith('+'):
        return phone
    if not phone.startswith('7'):
        phone = '7' + phone.lstrip('8')
    return '+' + phone


@register.filter
def slug(val):
    slug = unidecode.unidecode(val)
    return slugify(slug)[:50]


@register.simple_tag
def pagination_is_last(pages):
    if pages and not pages.next():
        return 'is-last'
    return ''


@register.simple_tag
def split_array(arr, n=0):
    return splitter(arr, n)


@register.filter
def get_queryset(page, request, fieldname='queryset'):
    return getattr(page, 'get_' + fieldname)(request)


@register.simple_tag
def get_queryset_as_var(page, request, fieldname='queryset'):
    return get_queryset(page, request, fieldname)


@register.filter
def md5(value):
    return hashlib.md5(value.encode('utf8')).hexdigest()


@register.filter
def js_string(value):
    return value.replace('\r\n', ' ').replace("'", '"')


@register.simple_tag
def target_blank(request, value):
    if not value:
        return ''
    if re.findall(r'\.(pdf|docx?|xlsx?)$', value):
        return mark_safe('target="_blank"')
    valid_paths = [request.site.root_page.url, '/', '#']
    return '' if any([value.startswith(path) for path in valid_paths]) else mark_safe('target="_blank"')


@register.filter
def format_title(text):
    return mark_safe(typo(text))


@register.filter
def ft(text):
    return format_title(text)


@register.filter
def yes_no(value, lang='en'):
    return {
        True: 'yes' if lang == 'en' else 'да',
        False: 'no' if lang == 'en' else 'да',
    }[bool(value)]


@register.filter
def admin_url(obj):
    return get_admin_url(obj)


@register.inclusion_tag('parts/honeypot_field.html')
def honeypot(**kwargs):
    return kwargs


@register.simple_tag
def qs(module, modelname):
    module = importlib.import_module(module)
    model = getattr(module, modelname)
    return model.objects.all()


@register.simple_tag
def call_method(instance, method, **kwargs):
    if not instance:
        return None
    method = getattr(instance, method, lambda **kw: None)
    return method(**kwargs)

@register.simple_tag
def get_ids_string(queryset):
    if type(queryset) is QuerySet:
        ids = queryset.values_list('id', flat=True)
    else:
        ids = [getattr(i, 'id', None) or i.get('id') for i in queryset]
    return ','.join([str(i) for i in ids])


@register.filter
def sysid(value):
    return id(value)


@register.simple_tag
def random_item(arr, fake=False):
    return random.choice(arr) if not fake else arr[0]


@register.filter
def hids(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value
    return get_hashids().encode(value)


@register.filter
def arr(n):
    return range(n)
