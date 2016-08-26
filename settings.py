# Django settings for herkules project.
import os
import re

############################
#      PROJECT
############################
from sfsystem.system.plugin import settings as plugin_settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SERVE_STATIC = not DEBUG

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

AUTH_USER_MODEL = 'user.User'

LOGIN_REDIRECT_URL = '/user/choose_account'
LOGIN_URL = '/user/auth/login'

############################
#   DATABASE SETTINGS
############################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db-name>',                            
        'USER': '<db-user>',                                
        'PASSWORD': '<db-pass>',                       
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

############################
#   APPLICATION SETTINGS
############################

SITE_ID = 1
SITE_URL = 'http://127.0.0.1/'

WSGI_APPLICATION = '<project-name>.wsgi.application'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

############################
#       URL SETTINGS
############################

ROOT_URLCONF = '<project-name>.urls'

############################
#          EMAIL
############################

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = '<email>@gmail.com'
EMAIL_HOST_PASSWORD = '<pass>'
EMAIL_PASSWORD_SECRET = '<pass secret>'
EMAIL_FROM = '<email>@gmail.com'

############################
#        SECURITY
############################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1']

# Make this unique, and don't share it with anybody.
SECRET_KEY = '<secret>'

############################
#     I18N & L10N
############################

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Poland'

DATE_FORMAT = 'd-m-Y'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LANGUAGES = [('pl', 'polski')]

############################
#         TEMPLATE
############################

TEMPLATE_NAME = 'default'

############################
#     STATIC, MEDIA
############################

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, os.pardir, "templates", TEMPLATE_NAME, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, os.pardir, "templates", TEMPLATE_NAME), 
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages"
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'sfsystem.system.apps.core.context_processors.sfsystem',
    'sfsystem.system.apps.core.context_processors.site',
    'sfsystem.system.apps.user.context_processors.accounts'
)

############################
#      APPS SETTINGS
############################

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

if not DEBUG:
    MIDDLEWARE_CLASSES += (
        'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
        'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    )

MIDDLEWARE_CLASSES += (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

INSTALLED_APPS += (
    'widget_tweaks',
    'south',
    'ajax_select',
    'mptt',
    'django_extensions',
)

if not DEBUG:
    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )

# SFSYSTEM APPS

SFSYSTEM_APPS = (
    'sfsystem.system.apps.core',
    'sfsystem.system.apps.notifications',
    'sfsystem.system.apps.facility',
    'sfsystem.system.apps.menu',
    'sfsystem.system.apps.user',
    'sfsystem.system.apps.payment',
    'sfsystem.system.apps.finance',
    'sfsystem.system.apps.money_account',
    'sfsystem.system.apps.carnet',
    'sfsystem.system.apps.partners',
)

SFSYSTEM_APPS += (
    'sfsystem.apps.pay_transferuj',
    'sfsystem.apps.messages_center',
    'sfsystem.apps.classrooms',
    'sfsystem.apps.shop',
    'sfsystem.apps.group_classes',
    'sfsystem.apps.announcement',
    'sfsystem.apps.id_scan_card',
)

INSTALLED_APPS += SFSYSTEM_APPS

############################
#           RAVEN
############################

SENTRY_CLIENT = 'sfsystem.system.raven.client.SentryClient'

RAVEN_CONFIG = {
    'dsn': '<raven-url>',
}

############################
#     SETTINGS UPDATE
############################

import sys
plugin_settings.update_settings(sys.modules[__name__], SFSYSTEM_APPS)

############################
#       ERROR 404
############################

IGNORABLE_404_URLS = (
    re.compile('^/media/'),
    re.compile('^/static/'),
)

############################
#   LOGGING CONFIGURATION
############################

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
