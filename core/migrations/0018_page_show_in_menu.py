# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_page_is_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_in_menu',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0432 \u043c\u0435\u043d\u044e'),
            preserve_default=True,
        ),
    ]
