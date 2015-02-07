# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from core.models import Gallery, Page


class MarkupView(TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        self.template_name = kwargs['template_name']
        return super(MarkupView, self).get(request, *args, **kwargs)


class IndexView(ListView):
    template_name = 'index.html'
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        gallery_slug = self.request.GET.get('g')
        try:
            context['object'] = context['object_list'].get(slug=gallery_slug)
        except self.model.DoesNotExist:
            context['object'] = context['object_list'].first()
        context['page'] = Page.objects.first()
        return context


class GenericPageView(DetailView):
    template_name = 'generic_page.html'
    model = Page
    context_object_name = 'page'


