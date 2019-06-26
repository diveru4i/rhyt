# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import translation


def set_stuff(request):
    try:
        root = request.site.root_page
    except AttributeError:
        root = None
    return {
        'DEBUG': settings.DEBUG,
        'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY,
        'config': request.config,
        'root': root,
    }
