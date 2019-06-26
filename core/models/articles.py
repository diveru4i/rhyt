# -*- coding: utf-8 -*-
import datetime

from modelcluster.fields import ParentalKey
from imperavi.blocks import RedactorFieldBlock
from imperavi.fields import RedactorField

from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel, TabbedInterface, ObjectList, PageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models

from .pages import DefaultPage


# class ArticlePage(DefaultPage):
#     template = 'pages/article.html'

#     datetime = models.DateTimeField(u'Дата и время', default=datetime.datetime.now)
#     annotation = models.TextField(u'Аннотация', blank=True, null=True)
#     content = StreamField([
#         ('text', RedactorFieldBlock()),
#     ], verbose_name=u'Текстовая часть')

#     content_panels = Page.content_panels + [
#         FieldPanel('datetime'),
#         FieldPanel('annotation'),
#         StreamFieldPanel('content'),
#     ]

#     class Meta:
#         verbose_name = u'Статья'
#         verbose_name_plural = u'Статьи'
#         ordering = ['-datetime']
