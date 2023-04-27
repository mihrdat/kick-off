from .base import *
from config.settings import rest_framework
import os

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = []

REST_FRAMEWORK = rest_framework.PROD
