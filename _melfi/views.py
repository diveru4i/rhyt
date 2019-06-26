# -*- coding: utf-8 -*-
import json

from django.contrib import messages
from django.core.cache import caches
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import View, TemplateView, FormView
from django.utils import translation
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


class NeverCacheMixin(object):
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(NeverCacheMixin, self).dispatch(*args, **kwargs)


def clear_cache(request, *args, **kwargs):
    cache = caches[kwargs['cache']]
    if request.user.is_authenticated:
        cache.clear()
        messages.add_message(request, messages.SUCCESS, u'Кеш очистен')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect('/')


class MarkupView(TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        self.template_name = kwargs.get('template_name') or 'index.html'
        return super(MarkupView, self).get(request, *args, **kwargs)


class EmailFormView(FormView):
    pass_config = True
    http_method_names = ['post']

    def get_config(self, request):
        if translation.get_language() == 'ru':
            from core.models import SiteConfiguration
            return SiteConfiguration.objects.first()
        elif translation.get_language() == 'en':
            try:
                from core.models import EnglishSiteConfiguration
                return EnglishSiteConfiguration.objects.first()
            except ImportError:
                return
            return SiteConfiguration.for_site(request.site)

    def form_valid(self, form):
        config = self.get_config(self.request) if self.pass_config else None
        form.send_email(config=config, request=self.request)
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({'success': False, 'errors': form.errors})

