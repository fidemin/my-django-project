import logging
from django.http import HttpResponse
from django.db import transaction

from polls.models import Question, Choice

logger = logging.getLogger('app.logic')


def index(request):
    logger.error('WHAT?')
    logger.info('API Call!!')
    return HttpResponse("Hello, world. You're at the polls index.")


def use_nested_atomic(request):
    with transaction.atomic():
        print('first transaction.atomic')

        with transaction.atomic():  # use save point
            print('second transaction.atomic')
            question = Question.objects.create(question_text='first question?')

        print('second transaction ends')

        Choice.objects.create(question_id=question.pk, choice_text='first choice')
        #raise Exception('intented error')

    print('first transcation ends')
    return HttpResponse('success')


def use_nested_commit(request):
    with transaction.atomic():
        print('first transaction.atomic')

        question = Question.objects.create(question_text='first question?')

        transaction.set_autocommit(False)
        print('set autocommit false')
        Choice.objects.create(question_id=question.pk, choice_text='first choice')
        transaction.commit()  # Error happned here: This is forbidden when an 'atomic' block is active 
        print('second commit')

    print('first transcation ends')
    return HttpResponse('success')

