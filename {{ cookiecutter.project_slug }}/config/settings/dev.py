from .base import *

SECRET_KEY = "django-insecure-v*!upq!^puv^gzfj6&lnssm5q7iu2jgl$vue=iqwe!x*@z#3^$"

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
    "django_extensions",
    "drf_spectacular",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# To fix django-debug-toolbar disappearing when running application with Docker.
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}

SPECTACULAR_SETTINGS = {
    "TITLE": "{{ cookiecutter.project_slug }} API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
