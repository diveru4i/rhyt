# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_gallery_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(unique=True, verbose_name='\u0421\u043b\u0430\u0433')),
                ('text', tinymce.models.HTMLField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('gallery', models.ForeignKey(verbose_name='\u0413\u0430\u043b\u0435\u0440\u0435\u044f', blank=True, to='core.Gallery', null=True)),
            ],
            options={
                'ordering': ['-datetime'],
            },
            bases=(models.Model,),
        ),
    ]
