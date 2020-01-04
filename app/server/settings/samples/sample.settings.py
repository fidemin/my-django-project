
from server.settings.base import *

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
