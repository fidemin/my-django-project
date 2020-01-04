import logging
from django.http import HttpResponse

logger = logging.getLogger('app.logic')


def index(request):
    logger.error('WHAT?')
    logger.info('API Call!!')
    return HttpResponse("Hello, world. You're at the polls index.")

