# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.cache import never_cache

from core.views import IndexView, PortfolioView, GenericPageView, MarkupView
from utils.views import clear_cache


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/clear_cache/', never_cache(clear_cache), name='clear_cache'),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^portfolio/$', PortfolioView.as_view(), name='portfolio'),
    url(r'^(?P<slug>[-_\w]+)/$', GenericPageView.as_view(), name='page'),

    url(r'^markup/(?P<template_name>([-_\w]+\/?)+\.html)$', MarkupView.as_view(), name='markup'),

)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)