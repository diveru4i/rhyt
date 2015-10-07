# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_page_show_in_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(related_name='children', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430', blank=True, to='core.Page', null=True),
            preserve_default=True,
        ),
    ]
