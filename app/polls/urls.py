from django.urls import path

from polls.views import index, use_nested_atomic, use_nested_commit


urlpatterns = [
    path('', index, name='index'),
    path('use-nested-atomic', use_nested_atomic, name='use-nested-atomic'),
    path('use-nested-commit', use_nested_commit, name='use-nested-commit'),
]

