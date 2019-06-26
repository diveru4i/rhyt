# -*- coding: utf-8 -*-
import os
import re
import urllib

import requests
import isodate
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.exceptions import InvalidImageFormatError

from wagtail.core.models import Collection
from wagtail.images.models import Image

from django import template
from django.core.cache import caches
from django.conf import settings
from django.core.files import File


register = template.Library()


YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/videos?key={0}'.format(settings.YOUTUBE_API_KEY)
YOUTUBE_RE_PATTERN = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')


def norm_path(filepath):
    return filepath.replace(settings.MEDIA_ROOT + '/', '')


@register.filter
def get_youtube_id(value):
    try:
        return re.match(YOUTUBE_RE_PATTERN, value).groupdict()['id']
    except AttributeError:
        return ''


@register.filter
def youtube_duration(value, cache_name='redis'):
    def _get_duration(value):
        url = YOUTUBE_API_URL + '&part=contentDetails&id={0}'.format(get_youtube_id(value))
        data = requests.get(url).json()
        duration = isodate.parse_duration(data['items'][0]['contentDetails']['duration'])
        return re.sub(r'^0:', '', str(duration))
    if not value:
        return ''
    if cache_name:
        cache = caches[cache_name]
        key = 'duration:' + value
        duration = cache.get(key)
        if not duration:
            duration = _get_duration(value)
            cache.set(key, duration)
        return duration
    else:
        return _get_duration(value)



@register.filter
def youtube_embed_url(value):
    if not value:
        return ''
    return 'https://www.youtube.com/embed/%s' % get_youtube_id(value)


@register.simple_tag
def youtube_cover(value, rendition=None, url=False):
    if not value:
        return ''
    youtube_id = get_youtube_id(value)
    image = Image.objects.filter(title=youtube_id).first()
    if not image:
        data = requests.get(YOUTUBE_API_URL + '&part=snippet&id=' + youtube_id).json()
        thumbnails = data['items'][0]['snippet']['thumbnails']
        for quality in ['maxres', 'standard', 'high', 'medium', 'default']:
            try:
                thumbnail_url = thumbnails[quality]['url']
                break
            except KeyError:
                continue
        if not thumbnail_url:
            return None
        filepath = os.path.join(settings.YOUTUBE_COVERS_ROOT, u'%s.jpg' % youtube_id)
        urllib.request.urlretrieve(thumbnail_url, filepath)
        try:
            collection = Collection.objects.get(name='youtube')
        except Collection.DoesNotExist:
            collection = Collection(name='youtube')
            Collection.objects.first().add_child(instance=collection)
        image = Image(title=youtube_id, file=norm_path(filepath), collection=collection)
        image.save()
    if rendition:
        image = image.get_rendition(rendition)
    return image.url if url else image


@register.simple_tag
def youtube_data(value):
    '''returns:
        'publishedAt', 'channelId', 'title', 'description', 'thumbnails',
        'channelTitle', 'tags', 'categoryId', 'liveBroadcastContent', 'localized'
    '''
    if not value:
        return dict()
    data = requests.get(YOUTUBE_API_URL + '&part=snippet&id=' + get_youtube_id(value)).json()
    data = data['items'][0]['snippet']
    data['publishedAt'] = isodate.parse_datetime(data['publishedAt'])
    return data
