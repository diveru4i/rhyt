# -*- coding: utf-8 -*-
from suit.widgets import AutosizedTextarea, SuitSplitDateTimeWidget

from django.forms import ModelForm
from django.contrib import admin

from blog.models import Entry


class EntryAdminForm(ModelForm):
    class Meta:
        model = Entry
        widgets = {
            'datetime': SuitSplitDateTimeWidget,
            'annotation': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
    list_display = ['__unicode__', 'datetime']
    prepopulated_fields = {'slug': ['name']}
    fieldsets = [
        (None, {
            'fields': [('name', 'slug'), 'banner', 'datetime', 'annotation', 'text']
        })
    ]


admin.site.register(Entry, EntryAdmin)

