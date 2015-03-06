# -*- coding: utf-8 -*-
from django.conf import settings


def if_debug(request):
    return {'DEBUG': settings.DEBUG}