from .common import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOST")]

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}
