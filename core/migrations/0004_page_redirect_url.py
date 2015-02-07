# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150207_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='redirect_url',
            field=models.CharField(max_length=100, null=True, verbose_name='\u0440\u0435\u0434\u0438\u0440\u0435\u043a\u0442', blank=True),
            preserve_default=True,
        ),
    ]
