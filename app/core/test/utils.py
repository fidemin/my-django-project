from django.conf import settings


def test_mode():
    return hasattr(settings, 'TEST_MODE') and settings.TEST_MODE

