# -*- coding: utf-8 -*-
from django import template
from django.db.models import Max
from django.utils import translation


register = template.Library()


@register.simple_tag
def is_active(page, item, html_classname='is-active'):
    try:
        url = item if type(item) is str else item.url
        res = page.url.startswith(url)
    except AttributeError:
        return False
    if html_classname:
        return html_classname if res else ''
    return res


@register.simple_tag
def get_section(page, depth):
    if not page:
        return
    if page.depth > depth:
        return page.get_ancestors().live().filter(depth=depth).first()
    if page.depth == depth:
        return page


@register.simple_tag
def get_menu_items(page, root, depth=2):
    if not page or getattr(page, 'is_fake', False):
        page = root
    section = get_section(page, depth)
    if not section:
        return dict()
    items = section.get_children().live().in_menu().specific()
    return items or list()


@register.inclusion_tag('parts/simple_menu.html')
def simple_menu(page, root, depth):
    items = get_menu_items(page, root, depth)
    return locals()


@register.filter
def has_grandchildren(page):
    depth = page.get_descendants().live().in_menu().filter(depth__gte=page.depth + 2).exists()
    return depth


@register.filter
def max_depth(page):
    return page.get_descendants().live().in_menu().aggregate(Max('depth')).get('depth__max') - page.depth


@register.inclusion_tag('parts/generate_menu.html', takes_context=True)
def generate_menu(context, page, depth=2):
    section = get_section(page, depth)
    if not section:
        return dict()
    items = section.get_children().live().in_menu().specific()
    if items:
        return {'items': items, 'self': context['self']}


@register.simple_tag
def queryset_not_empty(request, pages, wagtail=False):
    valid_pages = list()
    for page in pages:
        if wagtail:
            page = page.value
        page = page.specific
        if not hasattr(page, 'get_queryset') or page.get_queryset(request):
            valid_pages.append(page)
    return valid_pages

