# Generated by Django 2.0.13 on 2019-06-27 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
        ('core', '0006_indexpage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('keywords', models.TextField(blank=True, default='', help_text='Через запятую, без пробелов.', verbose_name='Ключевики')),
                ('menu_title', models.CharField(blank=True, help_text='если не указано – будет, как заголовок страницы', max_length=255, null=True, verbose_name='Название в меню')),
                ('banner', models.ForeignKey(blank=True, help_text='Также используется как изображение для шаринга страницы в соцсетях', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Баннер')),
                ('redirect_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Перенаправить на страницу')),
            ],
            options={
                'verbose_name': 'Галереи – список',
                'verbose_name_plural': 'Галереи – список',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AlterModelOptions(
            name='gallerypage',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галерея'},
        ),
    ]
