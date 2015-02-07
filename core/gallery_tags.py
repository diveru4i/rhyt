# -*- coding: utf-8 -*-
import os
import re
import urllib2
import hashlib

from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer

from django import template
from django.conf import settings
from django.template.loader import render_to_string


register = template.Library()


@register.filter
def get_youtube_id(value):
    q = re.match('.+watch\?v=(?P<id>[-_\w]+)', value)
    if q:
        return q.groupdict()['id']
    return ''


def create_default_video_preview(options):
    picture = open(os.path.join(settings.STATIC_ROOT, 'core', 'img', 'bgvideo.png'))
    thumbnailer = get_thumbnailer(picture, relative_name='default/bgvideo.png')
    return thumbnailer.get_thumbnail(options)

def get_video_cover(item, alias):
    if item.img_src:
        return item.img_src
    if item.img:
        return get_thumbnailer(item.img)[alias].url

@register.filter
def video_preview(item, alias='index_long_act'):
    if not item:
        return create_default_video_preview({'size': (370, 200), 'upscale': True, 'crop': True}).url
    ## если загружена обложка
    alias = 'index_long_act' if not alias else alias
    video_cover = get_video_cover(item, alias)
    if video_cover:
        return video_cover

    if item.video or item.get_ct() == 'external_video':
        return create_default_video_preview({'size': (370, 200), 'upscale': True, 'crop': True}).url
    if not hasattr(item, 'video'):
        thumb = create_default_video_preview({'size': (370, 200), 'upscale': True, 'crop': True})
        return thumb.url
    youtube_id = get_youtube_id(item.youtube)
    if not youtube_id:
        thumb = create_default_video_preview({'size': (720, 400), 'upscale': True, 'crop': True})
        return thumb.url
    try:
        preview_image_url = 'http://img.youtube.com/vi/{0}/{1}.jpg'.format(youtube_id, 'maxresdefault')
        urllib2.urlopen(preview_image_url)
        return preview_image_url
    except urllib2.HTTPError:
        return 'http://img.youtube.com/vi/{0}/{1}.jpg'.format(youtube_id, 'mqdefault')


def get_image_thumbnail(img, alias):
    options = settings.THUMBNAIL_ALIASES[''][alias]
    options.update({'subject_location': img.subject_location})
    return get_thumbnailer(img).get_thumbnail(options)


@register.simple_tag
def get_gallery_item(item, alias=None, width=None, height=None, classes=None):
    if not item:
        return ''
    try:
        return {
            'external_video': lambda: render_to_string('blocks/gallery/elements/video.html', {
                'video': item.youtube,
                'video_poster': video_preview(item, alias),
                'text': item.text,
                'width': width, 'height': height, 'classes': classes,
                'video_id': hashlib.md5(item.youtube).hexdigest(),
                'external': True,
                'mime': {
                    'mp4': 'video/mp4',
                    'ogg': 'video/ogg',
                    'flv': 'video/x-flv',
                }[item.youtube.split('.')[-1]]
            }),
            'video': lambda: render_to_string('blocks/gallery/elements/video.html', {
                'video': item.video,
                'video_poster': video_preview(item, alias),
                'text': item.text,
                'width': width, 'height': height, 'classes': classes,
                'video_id': item.video.id
            }),
            'youtube': lambda: render_to_string('blocks/gallery/elements/youtube.html', {
                'youtube_url': item.youtube,
                'youtube_poster': video_preview(item, alias),
                'text': item.text,
                'width': width, 'height': height, 'classes': classes
            }),
            'img': lambda: render_to_string('blocks/gallery/elements/img.html', {
                'image_url': get_image_thumbnail(item.img, alias).url,
                'text': item.text,
                'width': width, 'height': height, 'classes': classes
            }),
            'img_src': lambda: render_to_string('blocks/gallery/elements/img.html', {
                'image_url': item.img_src,
                'text': item.text,
                'width': width, 'height': height, 'classes': classes
            }),
        }[item.get_ct()]()
    except (InvalidImageFormatError, KeyError):
        return ''


@register.simple_tag
def get_gallery_item_url(item, alias=None):
    try:
        return {
            'video': lambda: '',
            'youtube': lambda: item.youtube,
            'img': lambda: get_image_thumbnail(item.img, alias).url,
            'img_src': lambda: item.img_src,
        }[item.get_ct()]()
    except InvalidImageFormatError:
        return item.img.url
    except KeyError:
        return ''
