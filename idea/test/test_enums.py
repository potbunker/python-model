import json

from enum import Enum

from idea.class_factory import get_value
from idea import CustomEnumMeta, get_value


def test_concept():
    with open('enums.json', 'r') as file:
        definitions = json.load(file)

    for definition in definitions:
        class_type = get_value('type', definition)
        assert 'enum' == class_type
        name = get_value('name', definition)
        clz = CustomEnumMeta(str(name), (Enum,), definition)
        assert issubclass(clz, Enum)
        for entry in clz:
            print entry.name, entry.value