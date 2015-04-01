# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-datetime'], 'verbose_name': '\u0437\u0430\u043f\u0438\u0441\u044c', 'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 16, 18, 13, 54, 595240), verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True),
            preserve_default=True,
        ),
    ]
