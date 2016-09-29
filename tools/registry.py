import six


class RegistryMeta(type):
    def __getitem__(meta, key):
        return meta._registry[key]


@six.add_metaclass(RegistryMeta)
class Registry(type):
    _registry = {}

    def __new__(meta, name, bases, classdict):
        cls = super(Registry, meta).__new__(meta, name, bases, classdict)
        if not classdict.pop('__base__', False):
            meta._registry[name] = cls
        return cls