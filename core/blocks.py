# -*- coding: utf-8 -*-
import datetime

from imperavi.blocks import RedactorFieldBlock

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.blocks import DocumentChooserBlock


class EditableBlock(RedactorFieldBlock):
    class Meta:
        template = 'blocks/editable.html'
        icon = 'pilcrow icon-redactor'
        label = u'Текст'


class YoutubeBlock(blocks.TextBlock):
    class Meta:
        template = 'blocks/youtube.html'
        icon = 'media'
        label = 'YouTube'


class SimpleImageBlock(ImageChooserBlock):
    class Meta:
        template = 'blocks/simple_image.html'
        icon = 'picture'
        label = u'Картинка'

    def get_context(self, value, **kwargs):
        context = super().get_context(value, **kwargs)
        context['image'] = value
        return context


class GalleryList(blocks.ListBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(blocks.PageChooserBlock('core.GalleryPage'), template='blocks/circle_list.html', icon='radio-empty', label=u'Галереи')

    def get_context(self, value, **kwargs):
        context = super().get_context(value, **kwargs)
        context['gallery_list'] = value
        return context
