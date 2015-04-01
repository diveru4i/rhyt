# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150216_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 30, 10, 57, 30, 834299), verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
    ]
