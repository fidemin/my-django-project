from django.core.exceptions import ImproperlyConfigured
from django.db import connections
from django.db.utils import load_backend
from django.test.runner import DiscoverRunner

from core.test.utils import test_mode


class CustomTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        if not test_mode():
            message = 'TEST_MODE = True is required in settings'
            raise ImproperlyConfigured(message)
        databases_alias = connections.databases.keys()

        for alias in databases_alias:
            test_db = connections.databases[alias]
            # code below is from original django TestRunner
            test_db.setdefault('ATOMIC_REQUESTS', False)
            test_db.setdefault('AUTOCOMMIT', True)
            test_db.setdefault('ENGINE', 'django.db.backends.dummy')
            if test_db['ENGINE'] == 'django.db.backends.' or not test_db['ENGINE']:
                test_db['ENGINE'] = 'django.db.backends.dummy'
            test_db.setdefault('CONN_MAX_AGE', 0)
            test_db.setdefault('OPTIONS', {})
            test_db.setdefault('TIME_ZONE', None)
            for setting in ['NAME', 'USER', 'PASSWORD', 'HOST', 'PORT']:
                test_db.setdefault(setting, '')

            backend = load_backend(test_db['ENGINE'])
            conn = backend.DatabaseWrapper(test_db, alias)
            connections[alias] = conn

    def teardown_databases(self, old_config, **kwargs):
        pass
