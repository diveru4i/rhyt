# -*- coding: utf-8 -*-
import mimetypes
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase

from django import forms
from django.conf import settings
from django.utils.encoding import smart_str

## email
from django.core.mail import EmailMultiAlternatives, SafeMIMEText, DEFAULT_ATTACHMENT_MIME_TYPE
from django.template.loader import get_template


class EmailMultiAlternativesWithEncoding(EmailMultiAlternatives):
    def _create_attachment(self, filename, content, mimetype=None):
        """
        Converts the filename, content, mimetype triple into a MIME attachment
        object. Use self.encoding when handling text attachments.

        Фикс позволяет прикреплять файлы с кириллицей в названии.
        """
        if mimetype is None:
            mimetype, _ = mimetypes.guess_type(filename)
            if mimetype is None:
                mimetype = DEFAULT_ATTACHMENT_MIME_TYPE
        basetype, subtype = mimetype.split('/', 1)
        if basetype == 'text':
            encoding = self.encoding or settings.DEFAULT_CHARSET
            attachment = SafeMIMEText(smart_str(content, settings.DEFAULT_CHARSET), subtype, encoding)
        else:
            # Encode non-text attachments with base64.
            attachment = MIMEBase(basetype, subtype)
            attachment.set_payload(content)
            encoders.encode_base64(attachment)
        if filename:
            try:
                filename = filename.encode('ascii')
            except UnicodeEncodeError:
                filename = Header(filename, 'utf-8').encode()
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        return attachment


class EmailFormMixin(object):
    template_name = 'email.html'
    subject = u'Обратная связь'

    def get_context_data(self, **kwargs):
        return {'data': self.cleaned_data}

    def get_message_text(self, **kwargs):
        html = get_template(self.template_name)
        html = html.render(self.get_context_data(**kwargs))
        return html

    def get_subject(self, **kwargs):
        return self.subject

    def get_to(self, **kwargs):
        return list()

    def get_attachments(self, **kwargs):
        return list()

    def send_email(self, **kwargs):
        html = self.get_message_text(**kwargs)
        subject = self.get_subject(**kwargs)
        to = self.get_to(**kwargs)
        for email in to:
            msg = EmailMultiAlternativesWithEncoding(subject, html, '', [email])
            msg.attach_alternative(html, "text/html")
            for filepath in self.get_attachments(**kwargs):
                msg.attach_file(filepath)
            msg.send()


class HoneypotForm(forms.Form):
    login = forms.CharField(required=True, widget=forms.TextInput(attrs={'style': 'position:absolute;left:-999em;'}))

    def clean_login(self):
        if self.cleaned_data.get('login') != 'login':
            raise forms.ValidationError('%s Snooping attempt' % str(datetime.datetime.now()))
