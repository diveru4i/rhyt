# -*- coding: utf-8 -*-
from imperavi.fields import RedactorField

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image

from .pages import *
from .articles import *
from .lists import *
from .extra import *


@register_setting
class SiteConfiguration(BaseSetting):
    root_page = models.ForeignKey(Page, models.SET_NULL, verbose_name=u'Корневая страница', blank=True, null=True, related_name='+')
    title = models.CharField(u'Заголовок по-умолчанию', max_length=100, default=u'', blank=True)
    ## SEO
    description = models.TextField(u'Описание по-умолчанию', blank=True, null=True)
    keywords = models.TextField(u'Ключевики по-умолчанию', blank=True, null=True, help_text=u'через запятую, без пробелов')
    banner = models.ForeignKey(Image, models.SET_NULL, blank=True, null=True, related_name='+', verbose_name='Баннер по умолчанию')
    ##
    footer = RedactorField(u'Футер', blank=True, null=True)
    ##
    search_page = models.ForeignKey(Page, models.SET_NULL, verbose_name=u'Страницы поиска', blank=True, null=True, related_name='+')

    panels = [
        PageChooserPanel('root_page'),
        PageChooserPanel('search_page'),
        FieldPanel('title', classname='full title'),
        MultiFieldPanel([
            ImageChooserPanel('banner'),
            FieldRowPanel([
                FieldPanel('description', classname='col6'),
                FieldPanel('keywords', classname='col6'),
            ])
        ], heading=u'SEO'),
        FieldPanel('footer'),
    ]

    class Meta:
        verbose_name = u'Настройки сайта'
