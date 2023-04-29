import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.main.dev")

celery = Celery("{{ cookiecutter.project_slug }}")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()