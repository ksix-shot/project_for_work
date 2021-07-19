import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_life.settings')

app = Celery('new_life')
app.config_from_object('django.conf:settings', namespace='CELERY')
