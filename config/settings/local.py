from .base import *  # noqa

DATABASES['default']['USER'] = 'root'

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ('rest_framework.authentication.BasicAuthentication',
                                                    'rest_framework.authentication.TokenAuthentication',)
