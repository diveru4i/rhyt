# -*- coding: utf-8 -*-
from captcha.fields import ReCaptchaField

from django import forms

from core.models.extra import Review
from _melfi.forms import EmailFormMixin, HoneypotForm


class ReviewForm(EmailFormMixin, forms.ModelForm):
    template_name = 'emails/feedback.html'
    subject = u'Обратная связь | opirogova'

    captcha = ReCaptchaField(error_messages={'invalid': u'Код введен неверно', 'required': u'Обязательное поле'})

    class Meta:
        model = Review
        fields = ['name', 'email', 'message']
