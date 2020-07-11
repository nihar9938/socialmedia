#Used for Celery


from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialmedia.settings")
app1 = Celery("socialmedia")

app1.config_from_object("django.conf:settings", namespace="CELERY")


app1.autodiscover_tasks()