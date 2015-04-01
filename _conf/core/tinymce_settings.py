# -*- coding: utf-8 -*-
import os

from core import STATIC_URL, INSTALLED_APPS

INSTALLED_APPS += [
    'tinymce',
]

TINYMCE_DEFAULT_CONFIG = {
#    'mode': 'textareas',
    'force_br_newlines' : True,
    'force_p_newlines' : False,
    'forced_root_block' : '',
    'content_css': "/static/core/css/redactor.css",
    'language' : "ru",
    'plugins' : "autolink,lists,spellchecker,pagebreak,style,layer,table,save,advhr,advimage,advlink,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    'inline_styles': True,

    # Theme options
    'theme_advanced_buttons1' : "image,code,undo,redo,|,justifyleft,justifycenter,justifyright,justifyfull,blockquote,|,bold,italic,|,styleselect,formatselect,fontsizeselect,|,bullist,numlist,|,link,unlink",
    'theme_advanced_buttons2' : "removeformat,cleanup,|,search,replace,|,tablecontrols,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,pastetext,|,indent,outdent,",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : 'true',
    'fix_list_elements': 'true',
    'style_formats': [
        {'title': 'Заголовок с отступом', 'inline': 'h3', 'classes': 'w-padding'},
        {'title': 'Заголовок без отступа', 'inline': 'h3', 'classes': 'wo-padding'},
    ],

    # Skin options
    # 'skin' : "o2k7",
    'skin' : "default",
    # 'theme': "advanced",
    'width': '100%',
    'height': 300,


    # 'plugins': "paste",

    'paste_auto_cleanup_on_paste': True,
    'paste_text_sticky': True,
    'paste_remove_spans': True,
    'paste_remove_styles': True,
    'paste_remove_styles_if_webkit': True,
    'paste_strip_class_attributes': 'all',
    'paste_text_linebreaktype': 'br',
}

TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False
TINYMCE_FILEBROWSER = False