from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from email_validation import valid_email_address
from tinymce.models import HTMLField

def email_valid(value: str):
    value = value.split(';')
    for i in value:
        if not valid_email_address(i):
            raise ValidationError(
                _('%(value)s is not even email RFC 2822'),
                params={'value': i}
            )

class MailSendler(models.Model):
    adress = models.CharField(max_length=400, validators=[email_valid], null=True, help_text='aaaaa@gmail.com;bbbb@gmail.com')
    subject = models.CharField(max_length=30, blank=True)
    sending = models.BooleanField(default=False)
    text = HTMLField()

    def __str__(self):
        return self.subject
