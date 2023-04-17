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

# Conf
from {{ cookiecutter.project_slug }}.conf.debug_toolbar import *
from {{ cookiecutter.project_slug }}.conf.swagger import *
from {{ cookiecutter.project_slug }}.conf.email.dev import *
