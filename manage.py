#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Management command entry point for working with migrations
"""

import sys
import django
from django.conf import settings

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "firstclass",
]

if django.VERSION[1] < 7:
    INSTALLED_APPS = ['south'] + INSTALLED_APPS

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    ROOT_URLCONF="firstclass.urls",
    INSTALLED_APPS=INSTALLED_APPS,
    MIDDLEWARE_CLASSES=(),  # Silence Django 1.7 warnings
    SITE_ID=1,
)
try:
    django.setup()
except AttributeError:
    # Django 1.4
    pass


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
