# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_gallery_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='main',
        ),
        migrations.AlterField(
            model_name='page',
            name='keywords',
            field=models.TextField(default='\u0434\u0435\u0442\u0441\u043a\u0430\u044f \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f, \u0441\u0435\u043c\u0435\u0439\u043d\u0430\u044f \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f, \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444, \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444 \u0432 \u041c\u043e\u0441\u043a\u0432\u0435, \u0441\u0435\u043c\u0435\u0439\u043d\u044b\u0439 \u0430\u043b\u044c\u0431\u043e\u043c', help_text='\u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e, \u0431\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u0432', null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u0438\u043a\u0438', blank=True),
            preserve_default=True,
        ),
    ]
