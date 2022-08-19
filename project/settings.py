import os
import dj-database-url
from dotenv import load_dotenv


load_dotenv()

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['.localhost', '127.0.0.1', '[::1]'])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
