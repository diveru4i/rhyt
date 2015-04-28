# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from core.models import GalleryProxy, Gallery, Page, Image, ImageCat


class MarkupView(TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        self.template_name = kwargs['template_name']
        return super(MarkupView, self).get(request, *args, **kwargs)


class PortfolioView(ListView):
    template_name = 'index.html'
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        gallery_slug = self.request.GET.get('g')
        try:
            context['object'] = context['object_list'].get(slug=gallery_slug)
        except self.model.DoesNotExist:
            pass
        context['page'] = Page.objects.all()[1]
        return context


class CategoryView(TemplateView):
    template_name = 'index.html'
    model = Gallery

    def create_gallery_proxy(self, cat):
        images = Image.objects.filter(cat=cat)
        if not images.exists():
            return None
        gallery = GalleryProxy()
        gallery.images = images,
        gallery.name = cat.name,
        gallery.slug = cat.slug
        return gallery._remove_tuples()

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.first()
        context['index'] = True
        gallery_slug = self.request.GET.get('g')
        try:
            cat = ImageCat.objects.get(slug=gallery_slug)
        except ImageCat.DoesNotExist:
            cat = None
        if cat:
            context['object'] = self.create_gallery_proxy(cat)
        else:
            object_list = list()
            for cat in ImageCat.objects.all():
                gallery = self.create_gallery_proxy(cat)
                if gallery:
                    object_list.append(gallery._remove_tuples())
            context['object_list'] = object_list
        return context


class GenericPageView(DetailView):
    template_name = 'generic_page.html'
    model = Page
    context_object_name = 'page'
