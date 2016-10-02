import pytest
import logging
from modellib.idea.descriptors import *
from modellib.idea.classes import *


logger = logging.getLogger(__name__)


def test_object_descriptor():

    class_dict = {

    }
    PersonDescriptor = DescriptorMeta('PersonDescriptor', (BaseDescriptor, ), class_dict)

    class Sample(BaseObject):
        person = PersonDescriptor('person', Person)

    sample = Sample({
        'person': Person({
            'uuid': 123564536,
            'name': 'Jaewan'
        })
    })

