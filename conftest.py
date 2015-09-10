"""
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
            # The ordering here, the apps using the organization base models
            # first and *then* the organizations app itself is an implicit test
            # that the organizations app need not be installed in order to use
            # its base models.
            "firstclass",
        ],
        MIDDLEWARE_CLASSES=(),  # Silence Django 1.7 warnings
        SITE_ID=1,
        FIXTURE_DIRS=['tests/fixtures'],
    )
    try:
        django.setup()
    except AttributeError:
        # Django 1.4
        pass
