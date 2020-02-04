from django.urls import path

from polls.views import (
    index, use_nested_transaction_atomic, use_nested_commit, create_question,
    create_question_async
)

urlpatterns = [
    path('', index, name='index'),
    path('questions', create_question, name='create-question'),
    path('questions-async', create_question_async, name='create-question-async'),
    path('use-nested-atomic', use_nested_transaction_atomic, name='use-nested-atomic'),
    path('use-nested-commit', use_nested_commit, name='use-nested-commit'),
]

