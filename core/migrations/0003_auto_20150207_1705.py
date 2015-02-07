# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150207_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order'], 'verbose_name': '\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443', 'verbose_name_plural': '\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0442\u0440\u0430\u043d\u0438\u0446'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442'),
            preserve_default=True,
        ),
    ]
