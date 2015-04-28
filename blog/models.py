# -*- coding: utf-8 -*-
import datetime

from filer.fields.image import FilerImageField

from django.core.urlresolvers import reverse
from django.db import models

from tinymce.models import HTMLField


class Entry(models.Model):
    banner = FilerImageField(verbose_name=u'Баннер', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(u'Название', max_length=255)
    slug = models.SlugField(u'Слаг', unique=True)
    text = HTMLField(u'Текст', blank=True, null=True)
    annotation = models.TextField(u'Аннотация', blank=True)
    datetime = models.DateTimeField(u'Время публикации', default=datetime.datetime.now())

    def get_absolute_url(self):
        return reverse('entry', args=[self.slug])

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-datetime']
        verbose_name = u'запись'
        verbose_name_plural = u'Записи'
