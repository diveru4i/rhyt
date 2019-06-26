# -*- coding: utf-8 -*-
import re
import urllib
import json
from http.client import BadStatusLine

from django import template

from _melfi import toint


register = template.Library()


@register.simple_tag
def share_url(request, anchor=None):
    uri = request.build_absolute_uri()
    if anchor:
        uri += '%23' + anchor
    return uri


@register.simple_tag
def social_counter(request, network):
    url = share_url(request)
    url = {
        'vk': lambda: 'http://vk.com/share.php?act=count&index=1&url=' + url,
        'fb': lambda: 'http://graph.facebook.com/' + url,
        'tw': lambda: 'http://urls.api.twitter.com/1/urls/count.json?url=' + url,
        'ok': lambda: 'https://connect.ok.ru/dk?st.cmd=extLike&uid=odklcnt0&ref=' + url
    }[network]()
    try:
        data = urllib.request.urlopen(url).read()
    except (urllib.request.HTTPError, BadStatusLine, urllib.request.URLError):
        return 0
    try:
        counter = {
            'vk': lambda: re.match('VK\.Share\.count\(\d, (?P<counter>\d{1,5})\)', data).groupdict().get('counter') or 0,
            'fb': lambda: json.loads(data).get('shares') or 0,
            'tw': lambda: json.loads(data).get('count') or 0,
            'ok': lambda: re.match("ODKL\.updateCount\('odklcnt0','(?P<counter>\d{1,5})'\);", data).groupdict().get('counter') or 0
        }[network]()
        return toint(counter)
    except (ValueError, AttributeError):
        return 0


@register.inclusion_tag('social/fb.html')
def fb_button(request, classes, counter=False, anchor=None, show_link_text=True):
    return {
        'classes': classes,
        'url': share_url(request, anchor),
        'counter': social_counter(request, 'fb') if counter else None,
        'show_link_text': show_link_text,
    }


@register.inclusion_tag('social/vk.html')
def vk_button(request, classes, counter=False, anchor=None, show_link_text=True):
    return {
        'classes': classes,
        'url': share_url(request, anchor),
        'counter': social_counter(request, 'vk') if counter else None,
        'show_link_text': show_link_text,
    }


@register.inclusion_tag('social/tw.html')
def tw_button(request, classes, text='', anchor=None, show_link_text=True):
    return {
        'classes': classes,
        'url': share_url(request, anchor),
        'text': text,
        'show_link_text': show_link_text,
    }


@register.inclusion_tag('social/ok.html')
def ok_button(request, classes, counter=False, anchor=None, show_link_text=True):
    return {
        'classes': classes,
        'url': share_url(request, anchor),
        'counter': social_counter(request, 'ok') if counter else None,
        'show_link_text': show_link_text,
    }


@register.inclusion_tag('social/linkedin.html')
def linkedin_button(request, classes, anchor=None, show_link_text=True):
    return {
        'classes': classes,
        'url': share_url(request, anchor),
        'show_link_text': show_link_text,
    }


@register.simple_tag
def page_title(self, root, config):
    title = config.title
    if not title:
        return ''
    if self == root.specific or not self:
        return title
    return u'{0} | {1}'.format(self.get('title') if type(self) == dict else self.get_title(), config.title)


@register.simple_tag
def page_description(page, default=''):
    try:
        page = page.specific
    except AttributeError:
        return default
    text = getattr(page, 'search_description', u'') or getattr(page, 'annotation', u'')
    return text or default


@register.simple_tag
def og_locale(language_code):
    try:
        return {
            'en': 'en_US',
            'ru': 'ru_RU'
        }[language_code]
    except KeyError:
        return 'ru_RU'


@register.simple_tag
def get_protocol(request):
    if request.is_secure():
        return 'https'
    return 'http'


@register.inclusion_tag('social/fb_sdk.html')
def facebook_sdk(app_id):
    return {'app_id': app_id}
