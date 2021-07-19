from django.contrib import admin
from .models import MailSendler
from django.core.mail import send_mail
from .tasks import sending_mail_celery
from django_celery_monitor.models import TaskState

# Register your models here.


@admin.action(description='Отправить')
def sending_mail(modeladmin, request, queryset):
    listik = list(queryset)
    for i in listik:
        email_list = i.adress
        email_list = email_list.split(';')
        print(email_list)
        sending_mail_celery.delay(i.subject, i.text, 'django.testing.sultanov@gmail.com', email_list,
                                  fail_silently=False, html_message=i.text)
    queryset.update(sending=True)


class AdminSendMailer(admin.ModelAdmin):
    actions = [sending_mail]

    readonly_fields = ('sending',)

    def has_change_permission(self, request, obj=None):
        try:
            a = obj.sending
        except:
            pass
        else:
            if a:
                return False
        return True


admin.site.register(MailSendler, AdminSendMailer)
admin.site.register(TaskState)
