# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import tinymce.models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(unique=True, verbose_name='\u0421\u043b\u0430\u0433')),
                ('text', tinymce.models.HTMLField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442')),
                ('banner', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0411\u0430\u043d\u043d\u0435\u0440', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'verbose_name': '\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443',
                'verbose_name_plural': '\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0442\u0440\u0430\u043d\u0438\u0446',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(related_name='images', to='core.Gallery'),
            preserve_default=True,
        ),
    ]
