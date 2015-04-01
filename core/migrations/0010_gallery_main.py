# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_image_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='main',
            field=models.BooleanField(default=True, help_text='\u0411\u0443\u0434\u0435\u0442 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u0432 \u043f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e', verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u044f'),
            preserve_default=True,
        ),
    ]
