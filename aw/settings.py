#-*- encoding:utf-8 -*-
"""
Django settings for aw project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ID = 1


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static/')
STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'aw.context_processors.application',
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'south',

    'feincms',
    'mptt',
    'feincms.module.page',
    'feincms.module.medialibrary',

    'aw',
    'news',
    'articles',
    'schedule',
    'players',
    'gallery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aw.urls'

WSGI_APPLICATION = 'aw.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# WIP
NEWS_PAGINATOR ='4'

# WIP use flatpages
GLOBAL_VARS = {
    'FAQ_URL': '/hockey-world/faq/', # for footer
    'SITEMAP_URL' : '/sitemap/', # for footer
    'NEWS_URL' :'neaanakoinwseis', #for latest news
    'ARTICLES_URL' :'ar8ra', #for article slideshow
    }

# WIP: use i18n
WORDS = {
    'SHOW_MORE' : 'Διαβάστε περισσότερα',
    'BACK' : 'Επιστροφή'
    }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'my-email@gmail.com'
EMAIL_HOST_PASSWORD = 'my-password'
EMAIL_PORT = 587

try:
    from local_settings import *
except ImportError as e:
    pass
