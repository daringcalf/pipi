from .base import *
DEBUG = True

DATABASE_ROUTERS = ['common.routers.SsDatabase']

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': '',
    },

    'heavenms': {
        'ENGINE': 'django.db.backends.mysql',
        #'ENGINE': 'mysql.connector.django',
        'NAME': os.getenv('SSDB_NAME'),
        'USER': os.getenv('SSDB_USER'),
        'PASSWORD': os.getenv('SSDB_PASS'),
        'HOST': os.getenv('SSDB_HOST'),
        'PORT': '',
    },
}

STATIC_URL = 'https://static.simplestory.cyou:7529/'
STATIC_ROOT = '/home/nobia/djangostatics'