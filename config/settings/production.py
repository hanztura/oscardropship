from .base import *

DEBUG = False

ALLOWED_HOSTS = os.environ.setdefault('ALLOWED_HOST', '')
ALLOWED_HOSTS = ALLOWED_HOSTS.split(',')

INSTALLED_APPS += ['anymail']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.setdefault('DATABASE_NAME', ''),
        'USER': os.environ.setdefault('DATABASE_USER', ''),
        'PASSWORD': os.environ.setdefault('DATABASE_PASSWORD', ''),
        'HOST': os.environ.setdefault('DATABASE_HOST', ''),
        'PORT': os.environ.setdefault('DATABASE_PORT', ''),
        'ATOMIC_REQUESTS': True,
    }
}

MEDIA_ROOT = os.environ.setdefault('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = os.environ.setdefault('MEDIA_URL', '/media/')

COMPRESS_OFFLINE = False

# EMAIL CONFIGURATION
# ----------------------------------------------------------------------------

MAILGUN_API_KEY = os.environ.setdefault(
    "MAILGUN_API_KEY", "")
MAILGUN_API_BASE_URL = os.environ.setdefault(
    "MAILGUN_API_BASE_URL", "")

ANYMAIL = {
    "MAILGUN_API_KEY": MAILGUN_API_KEY,
    "MAILGUN_SENDER_DOMAIN": MAILGUN_API_BASE_URL
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

OSCAR_URL_SCHEMA = "https"
