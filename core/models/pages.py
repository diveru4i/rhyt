# -*- coding: utf-8 -*-
import datetime

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase
from imperavi.blocks import RedactorFieldBlock
from imperavi.fields import RedactorField

from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel, TabbedInterface, ObjectList, PageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

from core.blocks import *


class DefaultPage(Page, Orderable):
    is_abstract = True

    banner = models.ForeignKey(Image, verbose_name=u'Баннер', null=True, blank=True, on_delete=models.SET_NULL, help_text=u'Также используется как изображение для шаринга страницы в соцсетях', related_name='+')
    keywords = models.TextField(u'Ключевики', blank=True, default=u'', help_text=u'Через запятую, без пробелов.')
    redirect_to = models.ForeignKey(Page, models.SET_NULL, blank=True, null=True, verbose_name=u'Перенаправить на страницу', related_name='+')
    # menu_settings
    menu_title = models.CharField(u'Название в меню', max_length=255, blank=True, null=True, help_text=u'если не указано – будет, как заголовок страницы')

    content_panels = [
        ImageChooserPanel('banner'),
    ] + Page.content_panels

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('search_description', classname='full'),
            FieldPanel('keywords'),
        ], heading=u'Настройки для поиска и отображения в соцсетях')
    ]

    settings_panels = [
        MultiFieldPanel([
            FieldPanel('show_in_menus'),
            FieldPanel('menu_title'),
        ], heading=u'Меню'),
        PageChooserPanel('redirect_to'),
    ] + Page.settings_panels

    search_fields = Page.search_fields + [
        index.SearchField('search_description'),
        index.SearchField('keywords'),
    ]

    class Meta:
        abstract = True
        ordering = ['sort_order']

    def serve(self, request, *args, **kwargs):
        if self.redirect_to:
            return HttpResponseRedirect(self.redirect_to.url)
        return super(DefaultPage, self).serve(request, *args, **kwargs)

    def get_title(self):
        return self.seo_title or self.title

    def get_banner(self):
        return self.banner

    def get_annotation(self):
        return getattr(self, 'annotation', '') or self.search_description

    def get_menu_title(self):
        return self.menu_title or self.title


class BlankPage(DefaultPage):
    template = 'base.html'

    class Meta:
        verbose_name = u'_Служебная – Пустая страница'
        verbose_name_plural = u'_Служебная – Пустая страница'

    def serve(self, request, *args, **kwargs):
        if self.redirect_to:
            return super(BlankPage, self).serve(request, *args, **kwargs)
        redirect_to = self.get_children().live().first() or self.get_parent()
        return HttpResponseRedirect(redirect_to.url if redirect_to else '/')

    def is_blank(self):
        return True



class IndexPage(DefaultPage):
    template = 'pages/index.html'

    class Meta:
        verbose_name = u'Главная страница'
        verbose_name_plural = u'Главные страницы'
