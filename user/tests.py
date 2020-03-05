from django.test import TestCase

# Create your tests here.

__all__ = ['external_func', '_internal_func']


def external_func():
    return 23


def _internal_func():
    return 42
