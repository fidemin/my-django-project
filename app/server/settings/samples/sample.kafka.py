
from server.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydjango',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'rlaguswjd',
        'PORT': '9007',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'kafka': {
            'level': 'INFO',
            'class': 'core.logging.handlers.KafkaStreamHandler',
            'brokers': ['127.0.0.1:9092'],
            'topic': 'log-test'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'app.logic': {
            'handlers': ['console', 'kafka'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}
