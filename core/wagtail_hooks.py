# -*- coding: utf-8 -*-
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from wagtail.core import hooks
from wagtail.core.whitelist import attribute_rule, check_url, allow_without_attributes
from wagtail.admin.menu import MenuItem
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from core.models.extra import *


@hooks.register('register_admin_menu_item')
def register_clear_cache():
    return MenuItem(mark_safe(u'Очистить кеш'), reverse('clear_cache', kwargs={'cache': 'default'}), classnames='icon icon-undo', order=100000)


@hooks.register('insert_editor_css')
def editor_css():
    files = [
        '/static/admin/css/melfi_admin.css',
    ]

    includes = '\n'.join(['<link rel="stylesheet" href="%s">' % filename for filename in files])

    return includes


# class NewsCatAdmin(ModelAdmin):
#     model = NewsCat
#     menu_icon = 'pick'
#     search_fields = ['title']
#     menu_order = 600


# modeladmin_register(NewsCatAdmin)
