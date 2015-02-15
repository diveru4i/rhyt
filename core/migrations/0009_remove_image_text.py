# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_image_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='text',
        ),
    ]
