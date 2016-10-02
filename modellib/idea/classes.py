from descriptors import *
from enum import Enum, EnumMeta
from itertools import chain


class Region(Enum):
    Global = 1
    North_America = 2


class BaseObject(object):

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


class ObjectMeta(type):
    def __new__(meta, name, bases, class_dict):

        return super(ObjectMeta, meta).__new__(meta, name, bases, class_dict)


class BaseEnum(Enum):
    __metaclass__ = EnumMeta

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


Event = ObjectMeta.__new__(ObjectMeta, 'Event', (object,), {'name': ObjectDescriptor('name', str)})


