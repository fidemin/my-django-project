from django.db import models
from core.test.testcase import UsedModels


class TestModel(models.Model):
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        UsedModels.add(self.__class__)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        abstract = True

