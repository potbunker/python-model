import json

from idea.class_factory import get_value
from idea import EntityMeta, get_value


def test_idea_new():
    with open('entities.json', 'r') as file:
        definition = json.load(file)

    assert 'entity' == get_value('type', definition), 'object_type should be entity.'
    name = get_value('name', definition)
    Idea = EntityMeta(str(name), (object,), definition)
    idea = Idea()
    idea.id = '12345'
    assert '12345' == idea.id
    assert isinstance(idea, Idea)


