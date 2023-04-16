# Starts a test server

import os

import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "safety"))


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },

        INSTALLED_APPS=(
            "safety",
            "django.contrib.auth",
            "django.contrib.contenttypes",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )

    django.setup()
