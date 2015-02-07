# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def clear_cache(request):
    if request.user.is_authenticated():
        cache.clear()
        messages.add_message(request, messages.SUCCESS, u'Кеш очистен')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(reverse('index'))