# -*- coding: utf-8 -*-
import re

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.models import File
from tinymce.models import HTMLField

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db import models



class OrderedModel(models.Model):
    order = models.PositiveSmallIntegerField(u'Приоритет', default=1)

    class Meta:
        abstract = True


class Gallery(OrderedModel):
    name = models.CharField(u'Название', max_length=255)
    slug = models.SlugField(u'Слаг', unique=True)
    text = HTMLField(u'Описание', blank=True, null=True)

    def get_cover(self):
        return self.images.filter(main=True).first() or self.images.first()

    def get_absolute_url(self):
        return u'{0}?g={1}'.format(reverse('index'), self.slug)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'галерею'
        verbose_name_plural = u'Галереи'
        ordering = ['order']


class Image(OrderedModel):
    gallery = models.ForeignKey(Gallery, related_name='images')
    img = FilerImageField(verbose_name=u'Изображение', blank=True, null=True, related_name=u'image_img')
    main = models.BooleanField(u'Обложка галереи', default=False)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.gallery.name, self.order)

    class Meta:
        verbose_name = u'изображение'
        verbose_name_plural = u'Изображения'
        ordering = ['order']


class Page(OrderedModel):
    name = models.CharField(u'Название', max_length=255)
    slug = models.SlugField(u'Слаг', unique=True)
    text = HTMLField(u'Контент')
    banner = FilerImageField(verbose_name=u'Баннер', blank=True, null=True, on_delete=models.SET_NULL)
    redirect_url = models.CharField(u'редирект', max_length=100, blank=True, null=True)
    description = models.TextField(u'Описание', blank=True, null=True)
    keywords = models.TextField(u'Ключевики', blank=True, null=True, help_text=u'через запятую, без пробелов')

    def get_absolute_url(self):
        return self.redirect_url or reverse('page', args=[self.slug])

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'страницу'
        verbose_name_plural = u'Настройки страниц'
        ordering = ['order']



