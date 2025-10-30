from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://school-management-backend.onrender.com']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite',
        'NAME': 'render_db',
        'USER': 'render_user',
        'PASSWORD': 'render_password',
        'HOST': 'db-host',
        'PORT': '5432',
    }
}