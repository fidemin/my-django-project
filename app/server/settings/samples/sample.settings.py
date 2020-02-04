
from server.settings.base import *

CELERY_BROKER_URL = 'amqp://user:password@localhost:5672/your-vhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'HOST': 'db_host',
        'USER': 'db_user',
        'PASSWORD': 'db_pw',
        'PORT': 'db_port',
    }
}
