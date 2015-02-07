# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_page_redirect_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='keywords',
            field=models.CharField(max_length=255, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u0438\u043a\u0438', blank=True),
            preserve_default=True,
        ),
    ]
