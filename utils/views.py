# -*- coding: utf-8 -*-
import json

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from django.contrib import messages
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


def clear_cache(request):
    if request.user.is_authenticated():
        cache.clear()
        messages.add_message(request, messages.SUCCESS, u'Кеш очистен')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(reverse('index'))


class NeverCacheMixin(object):
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(NeverCacheMixin, self).dispatch(*args, **kwargs)


class CaptchaMixin(NeverCacheMixin, View):

    def refresh_captcha(self, request):
        if self.request.is_ajax():
            to_json_response = dict()
            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])
            return HttpResponse(json.dumps(to_json_response), content_type='application/json')
        return None

    def get(self, request, *args, **kwargs):
        captcha_response = self.refresh_captcha(request)
        if captcha_response:
            return captcha_response
        return super(CaptchaMixin, self).get(request, *args, **kwargs)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return HttpResponse(json.dumps({'success': False}), content_type='application/json')
        return super(CaptchaMixin, self).form_invalid(form)

    def form_valid(self, form):
        form.send_email()
        if self.request.is_ajax():
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        return super(CaptchaMixin, self).form_valid(form)
