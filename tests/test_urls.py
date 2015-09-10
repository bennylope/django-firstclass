# -*- coding: utf-8 -*-

"""
A few simple tests for the URLs
"""

import pytest
from django.core.urlresolvers import reverse, NoReverseMatch

pytestmark = pytest.mark.django_db


def test_40_chars():
    assert reverse('view_message_online', kwargs={
        'key': '1' * 40})


def test_any_chars():
    assert reverse('view_message_online', kwargs={
        'key': '3d-1duIIiî' * 4})


def test_short_key():
    with pytest.raises(NoReverseMatch):
        assert reverse('view_message_online', kwargs={
            'key': '1' * 39})


def test_long_key():
    with pytest.raises(NoReverseMatch):
        assert reverse('view_message_online', kwargs={
            'key': '1' * 41})
