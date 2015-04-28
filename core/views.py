# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from core.models import Gallery, Page, Image


class MarkupView(TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        self.template_name = kwargs['template_name']
        return super(MarkupView, self).get(request, *args, **kwargs)


class PortfolioView(ListView):
    template_name = 'index.html'
    queryset = Gallery.objects.filter(main=False)
    page = Page.objects.all()[1]
    index = False

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        gallery_slug = self.request.GET.get('g')
        try:
            context['object'] = context['object_list'].get(slug=gallery_slug)
        except Gallery.DoesNotExist:
            pass
        context['page'] = self.page
        context['index'] = self.index
        return context

class CategoryView(PortfolioView):
    page = Page.objects.first()
    queryset = Gallery.objects.filter(main=True)
    index = True


class GenericPageView(DetailView):
    template_name = 'generic_page.html'
    model = Page
    context_object_name = 'page'
