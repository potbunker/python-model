from descriptors import *
from enum import Enum



class Region(Enum):
    Global = 1
    North_America = 2


class Person(object):
    uuid = IntDescriptor('uuid', int)
    name = StringDescriptor('name', str)

    def __init__(self, dict={}):
        for key, value in dict.iteritems():
            setattr(self, key, value)

    def __eq__(self, other):
        conditions = [
            type(self) is type(other),
            self.uuid == other.uuid,
            self.name == other.name,
        ]
        return all(conditions)


class Idea(object):
    id = ObjectDescriptor('id', int)
    analyst = ObjectDescriptor('analyst', Person)
    region = ObjectDescriptor('region', Region)
    others = SequenceDescriptor('others', Person)

    def __init__(self, dict={}):
        for key, value in dict.iteritems():
            setattr(self, key, value)


class ObjectMeta(type):
    def __new__(meta, name, bases, class_dict):

        return super(ObjectMeta, meta).__new__(meta, name, bases, class_dict)

Event = ObjectMeta.__new__(ObjectMeta, 'Event', (object,), {'name': ObjectDescriptor('name', str)})


