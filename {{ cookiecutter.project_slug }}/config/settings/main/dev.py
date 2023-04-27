from .base import *
from config.settings.swagger import *
from config.settings.debug_toolbar import *
from config.settings import rest_framework

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

REST_FRAMEWORK = rest_framework.DEV
