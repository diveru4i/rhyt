# -*- coding: utf-8 -*-
import datetime

from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.blocks import DocumentChooserBlock


class GalleryBlock(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock(), label=u'Изображения', required=False)
    videos = blocks.ListBlock(blocks.URLBlock(), label=u'Youtube', required=False)

    class Meta:
        icon = 'image'
        template = 'blocks/gallery.html'
