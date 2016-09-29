import pytest
from tools.registry import *


class Base(object):
    __metaclass__ = Registry
    __base__ = True


class A(Base):
    pass


def test_registry():
    assert Registry['A'] is A
