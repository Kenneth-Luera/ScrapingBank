import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Api_banco.settings")

app = Celery("Api_banco")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()