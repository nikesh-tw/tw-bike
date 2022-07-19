#from .base import *
from bike_pro.settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost']
ROOT_URLCONF = 'bike_pro.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

