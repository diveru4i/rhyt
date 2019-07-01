# -*- coding: utf-8 -*-
import datetime

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase
from imperavi.blocks import RedactorFieldBlock
from imperavi.fields import RedactorField
from ipware import get_client_ip

from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel, TabbedInterface, ObjectList, PageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.search import index

from django.db import models
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse

from core.blocks import *
from core.forms import ReviewForm


class DefaultPage(Page, Orderable):
    is_abstract = True

    banner = models.ForeignKey(Image, verbose_name=u'Баннер', null=True, blank=True, on_delete=models.SET_NULL, help_text=u'Также используется как изображение для шаринга страницы в соцсетях', related_name='+')
    keywords = models.TextField(u'Ключевики', blank=True, default=u'', help_text=u'Через запятую, без пробелов.')
    redirect_to = models.ForeignKey(Page, models.SET_NULL, blank=True, null=True, verbose_name=u'Перенаправить на страницу', related_name='+')
    # menu_settings
    menu_title = models.CharField(u'Название в меню', max_length=255, blank=True, null=True, help_text=u'если не указано – будет, как заголовок страницы')

    content_panels = [
        ImageChooserPanel('banner'),
    ] + Page.content_panels

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('search_description', classname='full'),
            FieldPanel('keywords'),
        ], heading=u'Настройки для поиска и отображения в соцсетях')
    ]

    settings_panels = [
        MultiFieldPanel([
            FieldPanel('show_in_menus'),
            FieldPanel('menu_title'),
        ], heading=u'Меню'),
        PageChooserPanel('redirect_to'),
    ] + Page.settings_panels

    search_fields = Page.search_fields + [
        index.SearchField('search_description'),
        index.SearchField('keywords'),
    ]

    class Meta:
        abstract = True
        ordering = ['sort_order']

    def serve(self, request, *args, **kwargs):
        if self.redirect_to:
            return HttpResponseRedirect(self.redirect_to.url)
        return super(DefaultPage, self).serve(request, *args, **kwargs)

    def get_title(self):
        return self.seo_title or self.title

    def get_banner(self):
        return self.banner

    def get_annotation(self):
        return getattr(self, 'annotation', '') or self.search_description

    def get_menu_title(self):
        return self.menu_title or self.title


class BlankPage(DefaultPage):
    template = 'base.html'

    class Meta:
        verbose_name = u'_Служебная – Пустая страница'
        verbose_name_plural = u'_Служебная – Пустая страница'

    def serve(self, request, *args, **kwargs):
        if self.redirect_to:
            return super(BlankPage, self).serve(request, *args, **kwargs)
        redirect_to = self.get_children().live().first() or self.get_parent()
        return HttpResponseRedirect(redirect_to.url if redirect_to else '/')

    def is_blank(self):
        return True



class IndexPage(DefaultPage):
    template = 'pages/index.html'

    content = StreamField([
        ('text', EditableBlock()),
        ('youtube', YoutubeBlock()),
        ('image', SimpleImageBlock()),
        ('gallery_list', GalleryList()),
    ], blank=True, null=True, verbose_name=u'Контент')

    content_panels = DefaultPage.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = u'Главная страница'
        verbose_name_plural = u'Главные страницы'


class GalleryPage(DefaultPage):
    template = 'pages/gallery.html'

    annotation = RedactorField(u'Аннотация', blank=True, null=True)
    gallery = models.ForeignKey('core.Gallery', models.SET_NULL, blank=True, null=True, verbose_name=u'Галерея', related_name='pages')

    content_panels = Page.content_panels + [
        FieldPanel('annotation'),
        SnippetChooserPanel('gallery'),
    ]

    class Meta:
        verbose_name = u'Галерея'
        verbose_name_plural = u'Галерея'

    def get_banner(self):
        return self.gallery.banner()


class GalleryListPage(DefaultPage):
    template = 'pages/gallery_list.html'

    class Meta:
        verbose_name = u'Галереи – список'
        verbose_name_plural = u'Галереи – список'


class ArticlePage(DefaultPage):
    template = 'pages/article.html'

    content = StreamField([
        ('text', EditableBlock()),
        ('youtube', YoutubeBlock()),
        ('image', SimpleImageBlock()),
        ('gallery_list', GalleryList()),
    ], blank=True, null=True, verbose_name=u'Контент')

    content_panels = DefaultPage.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статья'


class BlogArticle(ArticlePage):
    template = 'pages/blog_article.html'

    date = models.DateField(u'Дата публикации', default=datetime.date.today)

    content_panels = DefaultPage.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = u'Блог –  Запись'
        verbose_name_plural = u'Блог – Запись'
        ordering = ['-date']


class BlogListPage(DefaultPage):
    template = 'pages/blog.html'

    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блог'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['queryset'] = self.get_children().filter(articlepage__blogarticle__isnull=False).live().order_by('articlepage__blogarticle').specific()
        return context


class ReviewsList(DefaultPage):
    template = 'pages/reviews.html'

    reviews = StreamField([
        ('review', SnippetChooserBlock('core.Review', icon='plus', label=u'Отзыв')),
    ], blank=True, null=True, verbose_name=u'Отзывы')

    content_panels = DefaultPage.content_panels + [
        StreamFieldPanel('reviews'),
    ]

    class Meta:
        verbose_name = u'Отзывы'
        verbose_name_plural = u'Отзывы'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['reviews'] = [r.value for r in self.reviews]
        return context

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.ip, is_routable = get_client_ip(request)
                instance.user_agent = request.META.get('HTTP_USER_AGENT')
                instance.save()
                response = JsonResponse({'success': True, 'title': u'Спасибо за отзыв!', 'message': u'Для меня он правда очень важен =)'})
            else:
                print(form.errors)
                response = JsonResponse({'success': False, 'title': u'Что-то пошло не так...', 'message': u'Пардоньте, у нас возникла ошибка =(. Перезагрузите страницу и попробуйте еще раз, пожалуйста!'})
        else:
            response = super().serve(request, *args, **kwargs)
        return response
