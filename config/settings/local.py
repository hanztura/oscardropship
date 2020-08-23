from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
COMPRESS_ENABLED = True

DJANGO_ADMIN_URL = 'xadmin/'
WAGTAIL_CMS_URL = 'xcms/'

ENVIRONMENT_NAME = "Development server"
ENVIRONMENT_COLOR = "#5DADE2"
