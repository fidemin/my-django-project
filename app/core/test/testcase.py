from django.db import connections
from django.test import TransactionTestCase


class UsedModels(object):
    """
    UsedModels for test
    """
    _list = set()

    @classmethod
    def add(cls, model_class):
        cls._list.add(model_class)

    @classmethod
    def all(cls):
        return cls._list

    @classmethod
    def reset(cls):
        cls._list = set()


class CustomTestCase(TransactionTestCase):
    def _pre_setup(self):
        super()._pre_setup()

    def _post_teardown(self):
        self._truncate_used_model_tables()
        UsedModels.reset()
        super()._post_teardown()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def _truncate_used_model_tables(self):
        with connections['default'].cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0')
            used_models = UsedModels.all()
            for model in used_models:
                cursor.execute('TRUNCATE {}'.format(model._meta.db_table))
            cursor.execute('SET FOREIGN_KEY_CHECKS=1')
