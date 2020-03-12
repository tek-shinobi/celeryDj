from __future__ import absolute_import
import os
from django.conf import settings
from celery import Celery

# set default Django settings module for celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryDj.settings')

app = Celery('celeryDj_tasks', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)