# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('blog', '0004_auto_20150401_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='banner',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0411\u0430\u043d\u043d\u0435\u0440', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 9, 10, 5, 155424), verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
    ]
