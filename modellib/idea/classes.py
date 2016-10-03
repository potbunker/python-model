import logging
from itertools import chain

from enum import Enum, EnumMeta

from descriptors import *
from modellib.decorator import logged, log_methods

logger = logging.getLogger(__name__)


class Region(Enum):
    Global = 1
    North_America = 2


class ObjectMeta(type):
    def __new__(meta, name, bases, class_dict):

        cls = super(ObjectMeta, meta).__new__(meta, name, bases, class_dict)

        return log_methods(cls)


class BaseObject(object):
    __metaclass__ = ObjectMeta

    def __init__(self, dict={}):
        for key, value in dict.iteritems():
            setattr(self, key, value)

    def __eq__(self, other):
        conditions = chain(
            [lambda x: type(self) is type(x)],
            (lambda x: getattr(self, name) == getattr(x, name) for name in vars(self))
        )

        return all((cond(other) for cond in conditions))


class Person(BaseObject):
    uuid = ObjectDescriptor('uuid', int)
    name = ObjectDescriptor('name', str)


class Idea(BaseObject):
    id = ObjectDescriptor('id', int)
    analyst = ObjectDescriptor('analyst', Person)
    region = ObjectDescriptor('region', Region)
    others = SequenceDescriptor('others', Person)


class BaseEnum(Enum):
    __metaclass__ = EnumMeta

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


Event = ObjectMeta.__new__(ObjectMeta, 'Event', (object,), {'name': ObjectDescriptor('name', str)})


