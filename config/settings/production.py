from .base import *

ALLOWED_HOSTS = ['*']
SECRET_KEY = env('DJANGO_SECRET_KEY')

BROKER_URL = env.str('CLOUDAMQP_URL')
CELERY_RESULT_BACKEND = env.str('CLOUDAMQP_URL')
