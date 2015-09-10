# -*- coding: utf-8 -*-

"""
Tests for model methods
"""

from __future__ import unicode_literals

import pytest
from firstclass.models import Message

pytestmark = pytest.mark.django_db


def test_absolute_url():
    m = Message(key='1' * 40)
    assert m.get_absolute_url()


def test_string_representation():
    m = Message(
        key='1' * 40,
        data={'subject': 'hello', 'to': ['grandma@yahoo.com']},
    )
    assert m.__str__() == 'hello to grandma@yahoo.com'


def test_unicode_representation():
    m = Message(
        key='1' * 40,
        data={'subject': 'héllô', 'to': ['grandma@yahoo.com']},
    )
    assert m.__str__() == 'héllô to grandma@yahoo.com'


def test_save():
    m = Message(data={})
    m.save()
    assert len(m.key) == 40
