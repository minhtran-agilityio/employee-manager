from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Django-nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--spec-color',
    '--with-spec',
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-package=.'
]

NOSE_COVER_BRANCHES = [
    '--cover-branches'
]


# Haystack search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
