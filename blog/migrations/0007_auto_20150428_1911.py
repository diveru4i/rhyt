# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150401_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 19, 11, 53, 762478), verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
    ]
