import logging
import json

from django.http import HttpResponse
from django.db import transaction
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


from polls.models import Question, Choice

logger = logging.getLogger('app.logic')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
@require_http_methods(('POST',))
def create_question(request):
    """ create question record
    """
    body = json.loads(request.body)
    Question.objects.create(**body)
    response = HttpResponse()
    response.status_code = 201
    return response


def use_nested_transaction_atomic(request):
    logger.debug('first transaction.atomic starts')
    with transaction.atomic():

        logger.debug('second transaction.atomic starts')
        with transaction.atomic():  # use save point
            question = Question.objects.create(
                title='first question', description='first question description')

        logger.debug('second transaction ends')
        Choice.objects.create(question_id=question.pk, choice_text='first choice')

    logger.debug('first transcation ends')
    return HttpResponse()


def use_nested_commit(request):
    logger.debug('first transaction.atomic starts')
    with transaction.atomic():
        question = Question.objects.create(
                title='first question', description='first question description')

        logger.debug('set autocommit false')
        transaction.set_autocommit(False)

        Choice.objects.create(question_id=question.pk, choice_text='first choice')

        logger.debug('commit')
        transaction.commit()  # Error happned here: This is forbidden when an 'atomic' block is active 

    logger.debug('first transaction.atomic ends')
    return HttpResponse()

