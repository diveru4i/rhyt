# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_imagecat'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cat',
            field=models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', blank=True, to='core.ImageCat', null=True),
            preserve_default=True,
        ),
    ]
