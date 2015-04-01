# -*- coding: utf-8 -*-
import os

from core import PROJECT_ROOT, INSTALLED_APPS


THUMBNAIL_ALIASES = {
    '': {
        'admin': {'size': (100, 100), 'crop': True},
        'gallery_image': {'size': (900, 0), 'crop': True, 'upscale': True},
        'gallery_image_sqr': {'size': (300, 300), 'crop': True, 'upscale': True},
        'side_page_banner': {'size': (252, 0), 'crop': True, 'upscale': True},
        'meta_page_banner': {'size': (300, 300), 'crop': True, 'upscale': True},
        'blog_banner': {'size': (940, 250), 'crop': True, 'upscale': True},
    },
}

THUMBNAIL_HIGH_RESOLUTION = True
FILER_IS_PUBLIC_DEFAULT = True

MIGRATION_MODULES = {
    'filer': 'filer.migrations_django',
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

INSTALLED_APPS += [
    'filer',
    'mptt',
    'easy_thumbnails',
]


FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'django.core.files.storage.FileSystemStorage',
            'OPTIONS': {},
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'melfi',
        },
        'thumbnails': {
            'ENGINE': 'django.core.files.storage.FileSystemStorage',
            'OPTIONS': {},
            'THUMBNAIL_OPTIONS': {
                'base_dir': 'thumbs',
            },
        },
    },
}
