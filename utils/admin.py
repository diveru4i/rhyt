# -*- coding: utf-8 -*-
from filer.models import Folder

from django.contrib import admin


class OpenMultiButtonMixin(admin.ModelAdmin):
    '''
        Добавляет кнопку перехода в папку мультизагрузки на вкладку "Галерея"
    '''

    def __init__(self, *args, **kwargs):
        self.fieldsets = [
            (None, {
                'fields': ['create_or_open_multi'],
                'classes': ['suit-tab', 'suit-tab-gallery']
            }),
        ] + self.fieldsets
        self.readonly_fields = ['create_or_open_multi'] + list(self.readonly_fields)
        super(OpenMultiButtonMixin, self).__init__(*args, **kwargs)

    def get_app_label(self, obj):
        try:
            return {
                'core': u'Галереи',
            }[obj._meta.app_label]
        except KeyError:
            raise KeyError(u'Для этой модели не поддерживается мультизагрузка')

    def create_or_open_multi(self, obj):
        if not obj.id:
            return '<div class="alert alert-warning">Сначала сохраните объект</div>'
        try:
            parent = Folder.objects.get(name=self.get_app_label(obj))
        except Folder.DoesNotExist:
            return u'<div class="alert alert-error">Создайте папку "%s"</div>' % self.get_app_label(obj)
        folder = Folder.objects.get_or_create(parent=parent, name=obj.slug)
        return '<a href="%s" type="button" class="btn btn-success" target="_blank">Открыть папку</a>' % folder[0].get_admin_directory_listing_url_path()
    create_or_open_multi.allow_tags = True
    create_or_open_multi.short_description = u'Массовая загрузка'