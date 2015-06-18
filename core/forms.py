# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField, CaptchaTextInput

from django import forms

## email
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template


class FeedbackForm(forms.Form):
    template_name = 'email.html'
    subject = u'Отзывы'
    FORM_ERRORS = {
        'required': u'Обязательное поле',
        'invalid': u'Недопустимое значение',
        'captcha': {
            'invalid': u'Код введен неверно',
            'required': u'Обязательное поле',
        }
    }
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': u'is-required is-name'}), error_messages=FORM_ERRORS)
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': u'is-required is-email'}), error_messages=FORM_ERRORS)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': u'is-required is-message'}), error_messages=FORM_ERRORS)
    captcha = CaptchaField(label='Текст на картинке', widget=CaptchaTextInput(attrs={'class': u'is-required is-captcha'}), error_messages=FORM_ERRORS['captcha'])

    def get_context_data(self):
        return {'data': self.cleaned_data}

    def get_message_text(self):
        html = get_template(self.template_name)
        html = html.render(Context(self.get_context_data()))
        return html

    def send_email(self):
        connection = get_connection()
        html = self.get_message_text()
        msg = EmailMultiAlternatives(self.subject, html, '', ['s.pirogov@designdepot.ru'], connection=connection)
        msg.attach_alternative(html, "text/html")
        msg.content_subtype = "html"
        msg.send()
