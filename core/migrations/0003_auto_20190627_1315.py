# Generated by Django 2.0.13 on 2019-06-27 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_gallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='name',
            new_name='title',
        ),
    ]
