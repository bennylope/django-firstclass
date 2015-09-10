"""
Configuration file for py.test
"""

import django
from django.conf import settings


def pytest_configure():
    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "test.sqlite3",
            }
        },
        ROOT_URLCONF="firstclass.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "firstclass",
        ],
        MIDDLEWARE_CLASSES=(),  # Silence Django 1.7 warnings
        SITE_ID=1,
    )
    try:
        django.setup()
    except AttributeError:
        # Django 1.4
        pass
