# -*- coding: utf-8 -*-
from wagtail.admin.edit_handlers import PageChooserPanel

from django.db import models
from django.utils import translation


class I18NMixin(models.Model):
    i18n_page = models.ForeignKey('self', verbose_name=u'Версия страницы на другом языке', blank=True, null=True, on_delete=models.SET_NULL, related_name=u'translations')

    settings_panels = [
        PageChooserPanel('i18n_page'),
    ]

    class Meta:
        abstract = True

    def get_i18n_page(self):
        return self.i18n_page or type(self).objects.filter(i18n_page=self).first()

    def get_i18n_url(self):
        page = self.get_i18n_page()
        if page:
            return page.url
        return '/' if translation.get_language() == 'en' else '/en/'
