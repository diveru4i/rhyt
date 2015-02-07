# -*- coding: utf-8 -*-

class MultiGalleryUploader(object):
    '''
        Если в файлере заливается картинка по адресу
            multi/<app_label>/<model_name>/<object_slug>/ ,
        то создается core.models.Image в галерее соответствующего объекта.

        Поддерживаются:
            press.models.News
            events.models.Event
            pa.models.Act
    '''

    @classmethod
    def _create_data_structure(self, folder_name):
        '''
            Создает базовую структуру данных
            с динамическим импортом нужных моделей
        '''
        from django.contrib.contenttypes.models import ContentType
        if folder_name == 'press':
            from press.models import News
            return {
                'model': News,
                'ctype': ContentType.objects.get_for_model(News)
            }
        elif folder_name == 'projects':
            from services.models import Project
            return {
                'model': Project,
                'ctype': ContentType.objects.get_for_model(Project)
            }
        elif folder_name == 'satelites':
            from infra.models import Satelite
            return {
                'model': Satelite,
                'ctype': ContentType.objects.get_for_model(Satelite)
            }
        return None

    @classmethod
    def _create_image(self, gallery, instance):
        '''
            Создает core.models.Image
            с привязкой к нужному объекту
        '''
        from core.models import Image
        image = Image(
            img = instance,
            gallery = gallery
        )
        image.save()
        return image

    @classmethod
    def create_gallery_image_on_upload(self, sender, **kwargs):
        ''' Точка входа
        '''
        from core.models import Gallery, Image
        print 'GOGOGO'
        instance = kwargs.get('instance')
        accepted_folder_names = [u'Галереи']
        if Image.objects.filter(img=instance):
            print 1
            return
        try:
            if not instance.folder or \
                    not instance.polymorphic_ctype.name == 'image' or \
                    not instance.folder.parent.name in accepted_folder_names:
                print 2
                return
        except AttributeError:
            print 3
            return
        try:
            gallery = Gallery.objects.get(slug=instance.folder.name.strip())
        except Gallery.DoesNotExist:
            print 5
            return
        self._create_image(gallery, instance)
