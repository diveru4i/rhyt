# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from django.views.decorators.cache import never_cache, cache_page

from wagtail.contrib.sitemaps.views import sitemap
from wagtail.admin import urls as admin_urls
from wagtail.documents import urls as documents_urls
from wagtail.core import urls as wagtail_urls

from _melfi.views import clear_cache, MarkupView, EmailFormView


admin.autodiscover()

urlpatterns = [
    path('admin/clear_cache/<str:cache>/', never_cache(clear_cache), name='clear_cache'),
    path('admin/imperavi/', include('imperavi.urls')),
    path('admin/old/', admin.site.urls),
    path('admin/', include(admin_urls)),

    path('documents/', include(documents_urls)),

    path('sitemap.xml', cache_page(15*60)(sitemap), name='sitemap'),

    path('', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [re_path(r'^markup/(?P<template_name>.*)$', never_cache(MarkupView.as_view()), name='markup'),] + urlpatterns
