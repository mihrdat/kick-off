from .base import *

SECRET_KEY = "django-insecure-v*!upq!^puv^gzfj6&lnssm5q7iu2jgl$vue=iqwe!x*@z#3^$"

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
    "django_extensions",
]

# To fix django-debug-toolbar disappearing when running application with Docker.
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}