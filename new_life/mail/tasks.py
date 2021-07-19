from new_life.celery import app
from django.core.mail import send_mail
from celery.exceptions import MaxRetriesExceededError


@app.task(bind=True, default_retry_delay=10 * 60, max_retries=3)
def sending_mail_celery(self, subject, message, from_email, recipient_list,
                        fail_silently=False, auth_user=None, auth_password=None,
                        connection=None, html_message=None):
    try:
        send_mail(subject, message, from_email, recipient_list,
                  fail_silently=fail_silently, auth_user=auth_user, auth_password=auth_password,
                  connection=connection, html_message=html_message)
    except Exception as ex:
        if ex != MaxRetriesExceededError:
            raise self.retry(exc=ex)
