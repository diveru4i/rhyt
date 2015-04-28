# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_image_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='main',
            field=models.BooleanField(default=False, verbose_name='\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u044f'),
            preserve_default=True,
        ),
    ]
