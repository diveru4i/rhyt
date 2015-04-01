# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from core.models import Page
from blog.models import Entry


class BlogList(ListView):
    model = Entry
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['page'] = Page.objects.filter(slug='blog').first() or Page.objects.first()
        return context


class EntryDetail(DetailView):
    model = Entry
    template_name = 'entry.html'

    def get_context_data(self, **kwargs):
        context = super(EntryDetail, self).get_context_data(**kwargs)
        context['page'] = Page.objects.filter(slug='blog').first() or Page.objects.first()
        return context
