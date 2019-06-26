# -*- coding: utf-8 -*-
import re

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def get_2x_size(image_format_string):
    x2 = lambda format_string: re.sub(r'(\d+)', lambda x: str(int(x.group(0))*2), format_string)
    return x2(image_format_string)

@register.filter
def get_quarter_size(image_format_string):
    quarter = lambda format_string: re.sub(r'(\d+)', lambda x: str(round(int(x.group(0))*0.25)), format_string)
    return quarter(image_format_string)


@register.inclusion_tag('blocks/image.html')
def image2x(img, alias, alt='', classes='', extra=''):
    image_format_string = settings.IMAGE_FORMATS[alias]
    sizes = {
        'small': image_format_string,
        'big': get_2x_size(image_format_string)
    }
    return locals()

@register.inclusion_tag('blocks/image_lazy.html')
def imageLazy(img, alias, alt='', classes='', original=False, extra=''):
    image_format_string = settings.IMAGE_FORMATS[alias]
    sizes = {
        'normal': image_format_string,
        'retina': get_2x_size(image_format_string),
        'thumb': get_quarter_size(image_format_string)
    }
    return locals()


@register.simple_tag
def placeholder(width, height):
    return 'https://dummyimage.com/{0}x{1}/'.format(width, height)
