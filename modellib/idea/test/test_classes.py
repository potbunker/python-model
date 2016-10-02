import pytest
import logging
from modellib.idea.classes import *

logger = logging.getLogger(__name__)

def test_person():

    person = Person()
    person = Person({
        'uuid': 123456,
        'name': 'Jaewan Kim'
    })

    assert 'Jaewan Kim' == person.name
    assert 123456 == person.uuid

    another_person = Person({
        'uuid': 123456,
        'name': 'Jaewan Kim'
    })

    assert another_person == person

    person.uuid = 12356
    assert not another_person == person

    person.name = 'Jaewan'

    assert 'Jaewan' == person.name
    assert 12356 == person.uuid

    with pytest.raises(AssertionError) as error:
        person.name = 12345
        logger.exception(error)

    with pytest.raises(AssertionError) as error:
        person.uuid = '6547657'
        logger.exception(error)


def test_idea():

    idea = Idea()
    idea.id = 654765
    idea.analyst = Person()
    idea.analyst = Person({
        'uuid': 123456,
        'name': 'Jaewan Kim'
    })

    idea.others = []
    idea.region = Region.Global

    assert 'Jaewan Kim' == idea.analyst.name

    with pytest.raises(AssertionError) as error:
        idea.id = '1234556'

    with pytest.raises(AssertionError) as error:
        idea.analyst = Person({ 'uuid': '123345'})

    assert idea.analyst ==  Person({
        'uuid': 123456,
        'name': 'Jaewan Kim'
    })

    assert not idea.analyst == Person({
        'uuid': 12345,
        'name': 'Jaewan Kim'
    })

def test_event():
    event = Event()
    with pytest.raises(AssertionError) as error:
        event.name = 123565
