# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150208_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='main',
            field=models.BooleanField(default=False, verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u0433\u0430\u043b\u0435\u0440\u0435\u0438'),
            preserve_default=True,
        ),
    ]
