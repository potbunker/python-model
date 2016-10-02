from abc import abstractmethod, ABCMeta


class BaseDescriptor(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, cls):
        self.name = name
        self.cls = cls

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self._validate(value)
        instance.__dict__[self.name] = value

    def _validate(self, value):
        assert isinstance(value, self.cls), '{} must be of type {}: {}.'.format(self.name, self.cls, value)



class StringDescriptor(BaseDescriptor):
    pass


class IntDescriptor(BaseDescriptor):
    pass


class ObjectDescriptor(BaseDescriptor):
    pass


class SequenceDescriptor(BaseDescriptor):
    def __init__(self, name, item_cls):
        super(SequenceDescriptor, self).__init__(name, (list, set, tuple))
        self.item_cls = item_cls

    def _validate(self, value):
        super(SequenceDescriptor, self)._validate(value),
        assert all(map(lambda x: isinstance(x, self.item_cls), value)), \
            '{} must be of a {} of {}.'.format(self.name, self.cls, self.item_cls)

