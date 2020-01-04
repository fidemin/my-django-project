from django.db import models
from django.db.models import Model

from core.test.utils import test_mode

if test_mode():
    from core.test.model import TestModel as Model


class Question(Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'question'


class Choice(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        managed=False
        db_table = 'choice'
