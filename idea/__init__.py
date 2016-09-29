import json
import os
from itertools import imap

from enum import EnumMeta, Enum

package_dir = os.path.dirname(os.path.abspath(__file__))


enum_registry = {}
entity_registry = {}

class EntityMeta(type):
    def __new__(meta, name, parents, definition):

        def property_func(key, type):
            def getter(instance):
                return instance.__dict__[key]
            def setter(instance, value):
                assert isinstance(value, type), 'value {} for {} must be of type {}.'.format(value, key, type)
                instance.__dict__[key] = value
            return property(getter, setter)

        props = definition['properties']

        class_dict = {
            '__slots__': tuple(map(lambda x: x['name'], props))
        }
        typed_props = imap(lambda prop: (prop[0], to_class(prop[1])),
             imap(lambda x: ( x['name'], x['type'] ), definition['properties']))

        def to_class(type_name):
            if 'str' == type_name:
                return str
            elif 'int' == type_name:
                return int
            elif type_name in enum_registry:
                return enum_registry[type_name]
            elif type_name in entity_registry:
                return entity_registry[type_name]
            else:
                raise TypeError('{} cannot resolve to a type.'.format(type_name))

        #class_dict.update(dict((name, property_func(name, class_name)) for name, class_name in typed_props))

        cls = super(EntityMeta, meta).__new__(meta, name, parents, class_dict)
        for k, value in dict((name, property_func(name, class_name)) for name, class_name in typed_props).iteritems():
            setattr(cls, k, value)
        return cls


class CustomEnumMeta(EnumMeta):
    def __new__(cls, name, parents, definition):
        values = dict((value, index + 1) for index, value in enumerate(definition['values']))
        meta = super(CustomEnumMeta, cls).__new__(cls, name, parents, values)
        return meta


def get_value(key, definition):
    assert key in definition, 'Entity definition is missing {}.'.format(key)
    assert isinstance(definition[key], unicode), 'Value for {} must be unicode.'.format(key)
    return definition[key]


def to_enum(definition):
    class_type = get_value('type', definition)
    assert 'enum' == class_type
    name = get_value('name', definition)
    return name, CustomEnumMeta(str(name), (Enum,), definition)


def to_entity(definition):
    class_type = get_value('type', definition)
    assert 'entity' == class_type
    name = get_value('name', definition)
    return name, EntityMeta(str(name), (object,), definition)


with open(os.path.join(package_dir, 'enums.json'), 'r') as file:
    definitions = json.load(file)
    enum_registry.update(map(to_enum, definitions))


with open(os.path.join(package_dir, 'entities.json'), 'r') as file:
    definitions = json.load(file)
    entity_registry.update(map(to_entity, definitions))

