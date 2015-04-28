# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150330_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(unique=True, verbose_name='\u0421\u043b\u0430\u0433')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439',
            },
            bases=(models.Model,),
        ),
    ]
