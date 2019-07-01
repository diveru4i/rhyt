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
    title = models.CharField(u'Заголовок по-умолчанию', max_length=100, default=u'', blank=True)
    ## SEO
    description = models.TextField(u'Описание по-умолчанию', blank=True, null=True)
    keywords = models.TextField(u'Ключевики по-умолчанию', blank=True, null=True, help_text=u'через запятую, без пробелов')
    banner = models.ForeignKey(Image, models.SET_NULL, blank=True, null=True, related_name='+', verbose_name='Баннер по умолчанию')
    ##
    fb = models.URLField(u'Facebook', blank=True, null=True, default='https://web.facebook.com/groups/opirogova/')
    vk = models.URLField(u'VK', blank=True, null=True, default='http://vk.com/o_pirogova')
    ig = models.URLField(u'Instagram', blank=True, null=True, default='https://instagram.com/olesyapirogova/')
    disfo = models.URLField(u'Disfo', blank=True, null=True, default='http://disfo.ru/profile/Axlnick/')
    ##
    ##
    verification = models.TextField(u'Код верификации', blank=True, null=True)
    anal = models.TextField(u'Код аналитики', blank=True, null=True)

    panels = [
        FieldPanel('title', classname='full title'),
        MultiFieldPanel([
            ImageChooserPanel('banner'),
            FieldRowPanel([
                FieldPanel('description', classname='col6'),
                FieldPanel('keywords', classname='col6'),
            ])
        ], heading=u'SEO'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('fb', classname='col6'),
                FieldPanel('vk', classname='col6'),
            ]),
            FieldRowPanel([
                FieldPanel('ig', classname='col6'),
                FieldPanel('disfo', classname='col6'),
            ]),
        ], heading=u'Соцсети'),
        MultiFieldPanel([
            FieldPanel('verification'),
            FieldPanel('anal'),
        ], heading=u'Аналитика', classname='collapsible collapsed'),
    ]

    class Meta:
        verbose_name = u'Настройки сайта'
