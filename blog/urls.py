# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from blog.views import BlogList, EntryDetail


urlpatterns = patterns('',
    url(r'^$', BlogList.as_view(), name='blog'),
    url(r'^(?P<slug>[-_\w]+)/$', EntryDetail.as_view(), name='entry'),
)

