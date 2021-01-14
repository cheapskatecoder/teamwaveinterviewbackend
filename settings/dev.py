from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'interview_teamwave',
        'USER': 'postgres',
        'PASSWORD': 'postgres'
    }
}

CORS_ALLOW_ALL_ORIGINS = True
