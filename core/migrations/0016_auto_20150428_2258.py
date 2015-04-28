# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_gallery_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['main', 'order'], 'verbose_name': '\u0433\u0430\u043b\u0435\u0440\u0435\u044e', 'verbose_name_plural': '\u0413\u0430\u043b\u0435\u0440\u0435\u0438'},
        ),
        migrations.RemoveField(
            model_name='image',
            name='cat',
        ),
        migrations.DeleteModel(
            name='ImageCat',
        ),
    ]
