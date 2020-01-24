from django.urls import path

from polls.views import index, use_nested_transaction_atomic, use_nested_commit, create_question


urlpatterns = [
    path('', index, name='index'),
    path('questions', create_question, name='create-questoin'),
    path('use-nested-atomic', use_nested_transaction_atomic, name='use-nested-atomic'),
    path('use-nested-commit', use_nested_commit, name='use-nested-commit'),
]

