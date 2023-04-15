from .base import *
import os

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = []

REST_FRAMEWORK.update(
    {
        "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    }
)
