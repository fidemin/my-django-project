
from server.settings.base import *

TEST_MODE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db_name', # should have test_ prefix. e.g. test_my_django
        'HOST': 'db_host',
        'USER': 'db_user',
        'PASSWORD': 'db_pw',
        'PORT': 'db_port',
    }
}
