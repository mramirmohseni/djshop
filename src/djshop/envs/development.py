from .common import *
from decouple import config

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "daphne",
    "drf_spectacular"
] + INSTALLED_APPS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config('DB_NAME', default='djshop'),
        "USER": config('DB_USER', default='djshop'),
        "PASSWORD": config('DB_PASSWORD', default='123@456'),
        "HOST": config('DB_HOST', default='db'),
        "PORT": config('DB_PORT', default='5432'),
    }
}