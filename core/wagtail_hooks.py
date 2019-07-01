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


class GalleryAdmin(ModelAdmin):
    model = Gallery
    menu_icon = 'pick'
    list_display = ['title', 'admin_banner']
    search_fields = ['title']
    menu_order = 600

    def admin_banner(self, obj):
        return '<img src="%s"/>' % obj.banner().get_rendition('max-165x165').file.url
    admin_banner.allow_tags = True
    admin_banner.short_description = u'Баннер'


class ReviewAdmin(ModelAdmin):
    model = Review
    menu_icon = 'openquote'
    list_display = ['name', 'message', 'created', 'ip']
    menu_order = 700


modeladmin_register(GalleryAdmin)
modeladmin_register(ReviewAdmin)
