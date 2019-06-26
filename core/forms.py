# -*- coding: utf-8 -*-
from captcha.fields import ReCaptchaField

from django import forms

from _melfi.forms import EmailFormMixin, HoneypotForm


class FeedbackForm(HoneypotForm, EmailFormMixin):
    template_name = 'emails/feedback.html'
    subject = u'Обратная связь | opirogova'

    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    captcha = ReCaptchaField(error_messages={'invalid': u'Код введен неверно', 'required': u'Обязательное поле'})
