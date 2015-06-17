# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20150428_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_feedback',
            field=models.BooleanField(default=False, verbose_name='\u0424\u043e\u0440\u043c\u0430 \u043e\u0442\u0437\u044b\u0432\u043e\u0432'),
            preserve_default=True,
        ),
    ]
