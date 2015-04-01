# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150227_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='keywords',
            field=models.TextField(help_text='\u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e, \u0431\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u0432', null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u0438\u043a\u0438', blank=True),
            preserve_default=True,
        ),
    ]
