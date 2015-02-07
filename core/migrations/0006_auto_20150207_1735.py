# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150207_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='keywords',
            field=models.TextField(null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u0438\u043a\u0438', blank=True),
            preserve_default=True,
        ),
    ]
