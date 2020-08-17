# Standard Libraries
import os

# Thirdparty Libraries
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "presupuesto.settings")

app = Celery("presupuesto")
app.config_from_object("django.conf:settings", namespace="CELERY"),
app.autodiscover_tasks()
