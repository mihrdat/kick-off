from .base import *
from config.settings import rest_framework
from config.settings.swagger import *
from config.settings.debug_toolbar import *

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
    "drf_spectacular",
    "django_extensions",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

REST_FRAMEWORK = rest_framework.DEV
