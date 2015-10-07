# -*- coding: utf-8 -*-
from draggable_sorting import DraggableMixin
from suit.admin import SortableModelAdmin, SortableStackedInline, SortableGenericStackedInline, SortableGenericTabularInline
from suit.widgets import AutosizedTextarea

from django.contrib import admin
from django.forms import ModelForm

from core.models import Gallery, Image, Page
from utils.admin import OpenMultiButtonMixin


class ImageInlineForm(ModelForm):
    model = Image

    class Meta:
        widgets = {
            'text': AutosizedTextarea(attrs={'rows': 5, 'class': 'input-xlarge'}),
        }


class PageAdminForm(ModelForm):
    model = Page

    class Meta:
        widgets = {
            'keywords': AutosizedTextarea(attrs={'rows': 5, 'class': 'input-xlarge'}),
            'description': AutosizedTextarea(attrs={'rows': 5, 'class': 'input-xlarge'}),
        }


class ImageInline(DraggableMixin, SortableStackedInline):
    model = Image
    extra = 0
    form = ImageInlineForm
    suit_classes = 'suit-tab suit-tab-gallery'
    fieldsets = [
        (None, {
            'fields': [('main', 'img')],
        })
    ]


class GalleryAdmin(OpenMultiButtonMixin, SortableModelAdmin):
    list_display = ['__unicode__', 'main']
    list_editable = ['main']
    prepopulated_fields = {'slug': ['name']}
    inlines = [ImageInline]
    fieldsets = [
        (None, {
            'fields': ['main', ('name', 'slug'), 'text'],
            'classes': ['suit-tab', 'suit-tab-core']
        }),
    ]
    suit_form_tabs = [
        ('core', u'Название'),
        ('gallery', u'Галерея'),
    ]


class PageAdmin(SortableModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['__unicode__', 'slug']
    form = PageAdminForm
    fieldsets = [
        (None, {
            'fields': ['show_in_menu', ('name', 'slug'), 'banner', 'text', 'redirect_url', 'is_feedback'],
            'classes': ['suit-tab', 'suit-tab-core']
        }),
        (None, {
            'fields': ['keywords', 'description'],
            'classes': ['suit-tab', 'suit-tab-seo']
        }),
    ]
    suit_form_tabs = [
        ('core', u'Название'),
        ('seo', u'Seo'),
    ]


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Page, PageAdmin)


###################### signals
from filer.models import Image as filerImage
from django.db.models.signals import post_save
from core.signals import MultiGalleryUploader

post_save.connect(MultiGalleryUploader.create_gallery_image_on_upload, sender=filerImage, dispatch_uid='multi_gallery_uploader')
