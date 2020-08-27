"""
Django settings for oscardropship project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import secrets

from django.utils.translation import ugettext_lazy as _

from oscar.defaults import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APPS_DIR = os.path.join("oscardropship")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.setdefault('DJANGO_SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'system.User'

ADMINS = os.environ.setdefault("ADMINS", '[["Hanz", "hctura.official@gmail.com"]]')
# convert admins (in json) to object
try:
    ADMINS = json.loads(ADMINS)
    ADMINS = [tuple(admin) for admin in ADMINS]
except Exception as e:
    ADMINS = []

RANDOM_ADMIN_URL = '{}/'.format(secrets.token_urlsafe(6))
DJANGO_ADMIN_URL = os.environ.setdefault(
    'DJANGO_ADMIN_URL', RANDOM_ADMIN_URL)
DEFAULT_FROM_EMAIL = os.environ.setdefault(
    'DEFAULT_FROM_EMAIL', 'webmaster@oscardropship.com')
SERVER_EMAIL = os.environ.setdefault(
    'SERVER_EMAIL', 'server@@oscardropship.com')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'system.apps.SystemConfig',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'custom_oscar.config.CustomShop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    # 'oscar.apps.checkout.apps.CheckoutConfig',
    'oscardropship.custom_oscar.checkout.apps.CheckoutConfig',
    'oscar.apps.address.apps.AddressConfig',
    'oscar.apps.shipping.apps.ShippingConfig',
    # 'oscar.apps.catalogue.apps.CatalogueConfig',
    # 'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscardropship.custom_oscar.catalogue.apps.CatalogueConfig',
    'oscardropship.custom_oscar.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    # 'oscar.apps.partner.apps.PartnerConfig',
    'custom_oscar.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    # 'oscar.apps.payment.apps.PaymentConfig',
    'oscardropship.custom_oscar.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    # 'oscar.apps.order.apps.OrderConfig',
    'custom_oscar.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'django_tables2',
    'oscar_accounts.apps.AccountsConfig',
    'oscar_accounts.dashboard.apps.AccountsDashboardConfig',

    # must haves
    'django_extensions',
    'easy_thumbnails',
    'sorl.thumbnail',

    # wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.routable_page',

    'modelcluster',
    'taggit',

    # puput
    'django_social_share',
    'puput',
    'colorful',

    # other third parties
    'tinymce',
    'newsletter',

    # project
    'wagtail_pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(APPS_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.setdefault('OSCARDROPSHIP_DATABASE_NAME', ''),
        'USER': os.environ.setdefault('OSCARDROPSHIP_DATABASE_USER', ''),
        'PASSWORD': os.environ.setdefault('OSCARDROPSHIP_DATABASE_PASSWORD', ''),
        'HOST': os.environ.setdefault('OSCARDROPSHIP_DATABASE_HOST', ''),
        'PORT': os.environ.setdefault('OSCARDROPSHIP_DATABASE_PORT', ''),
        'ATOMIC_REQUESTS': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

ENVIRONMENT_FLOAT = True
ENVIRONMENT_NAME = "Production server"
ENVIRONMENT_COLOR = "#E74C3C"

# other django oscar settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

OSCAR_SHOP_NAME = "My Novelty Shop"
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': (
        'Being processed',
        'Cancelled',
    ),
    'Being processed': (
        'Shipped',
        'Cancelled',
    ),
    'Shipped': (
        'Received',
        'Cancelled',
    ),
    'Received': (),
    'Cancelled': (),
}
OSCAR_ORDER_STATUS_CASCADE = {
    'Being processed': 'Being processed',
    'Shipped': 'Shipped',
    'Received': 'Received',
    'Cancelled': 'Cancelled',
}
OSCAR_LINE_STATUS_PIPELINE = {
    'Pending': (
        'Being processed',
        'Cancelled',
    ),
    'Being processed': (
        'Shipped',
        'Cancelled',
    ),
    'Shipped': (
        'Received',
        'Cancelled',
    ),
    'Received': (),
    'Cancelled': (),
}
OSCAR_ALLOW_ANON_CHECKOUT = True
OSCAR_FROM_EMAIL = os.environ.setdefault("OSCAR_FROM_EMAIL", "oscar@example.com")
OSCAR_DEFAULT_CURRENCY = "USD"
OSCAR_USE_LESS = False
OSCAR_HOMEPAGE = reverse_lazy('wagtail_serve', args=[''])

# paypal
PAYPAL_SANDBOX_MODE = False
PAYPAL_CALLBACK_HTTPS = True
PAYPAL_API_ACCOUNT = os.environ.setdefault('PAYPAL_API_ACCOUNT', '')
PAYPAL_API_CLIENT_ID = os.environ.setdefault('PAYPAL_API_CLIENT_ID', '')
PAYPAL_API_SECRET = os.environ.setdefault('PAYPAL_API_SECRET', '')
PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = 'USD'
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True

# oscar-accounts
OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': 'Accounts',
        'icon': 'icon-globe',
        'children': [
            {
                'label': 'Accounts',
                'url_name': 'accounts_dashboard:accounts-list',
            },
            {
                'label': 'Transfers',
                'url_name': 'accounts_dashboard:transfers-list',
            },
            {
                'label': 'Deferred income report',
                'url_name': 'accounts_dashboard:report-deferred-income',
            },
            {
                'label': 'Profit/loss report',
                'url_name': 'accounts_dashboard:report-profit-loss',
            },
        ]
    })

# wagtail
WAGTAIL_SITE_NAME = 'My Example Site'

# puput
PUPUT_AS_PLUGIN = True

# django-newesletter
NEWSLETTER_CONFIRM_EMAIL = False
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"
# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1

# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60

# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100
