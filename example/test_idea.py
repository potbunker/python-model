import pytest
from idea import enum_registry, entity_registry

def test_registry():
    print enum_registry
    print entity_registry

    Idea = entity_registry['Idea']
    idea = Idea()
    idea.id = '12345'

