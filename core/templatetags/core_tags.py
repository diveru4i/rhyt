# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from core.models import Page


register = template.Library()


@register.assignment_tag
def get_menu_items():
    return Page.objects.all()