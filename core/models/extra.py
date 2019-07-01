# -*- coding: utf-8 -*-
import datetime

from wagtail.core.fields import StreamField
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.models import Image
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel, TabbedInterface, ObjectList, PageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from django.db import models


@register_snippet
class Gallery(index.Indexed, models.Model):
    title = models.CharField(u'Название', max_length=255)
    images = StreamField([
        ('image', ImageChooserBlock(icon='image', label=u'Картинка'))
    ], verbose_name=u'Картинки')

    panels = [
        FieldPanel('title'),
        StreamFieldPanel('images')
    ]

    search_fields = [
        index.FilterField('id'),
        index.SearchField('title'),
    ]

    class Meta:
        verbose_name = u'гелерею'
        verbose_name_plural = u'Галереи'

    def __str__(self):
        return self.title

    def banner(self):
        return self.images[0].value


@register_snippet
class Review(index.Indexed, models.Model):
    name = models.CharField(u'Заголовок', max_length=255)
    image = models.ForeignKey(Image, models.SET_NULL, blank=True, null=True, related_name='reviews', verbose_name=u'Фото')
    message = models.TextField(u'Текст')
    email = models.EmailField(u'Email', blank=True, null=True)
    ##
    created = models.DateTimeField(u'Создано', default=datetime.datetime.now)
    ip = models.CharField('IP', max_length=25, blank=True, null=True)
    user_agent = models.TextField(u'HTTP_USER_AGENT', blank=True, null=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            ImageChooserPanel('image'),
            FieldPanel('message'),
            FieldPanel('email'),
        ], heading=u'Отзыв'),
        MultiFieldPanel([
            FieldPanel('created'),
            FieldPanel('ip'),
            FieldPanel('user_agent'),
        ], heading=u'META'),
    ]

    search_fields = [
        index.FilterField('id'),
        index.SearchField('name'),
        index.SearchField('message'),
        index.SearchField('email'),
    ]

    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'Отзывы'
        ordering = ['-created']

    def __str__(self):
        return self.name
