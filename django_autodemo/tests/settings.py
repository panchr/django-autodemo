# django-autodemo/tests/settings.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Test application settings.

from django.core.urlresolvers import reverse_lazy

DEBUG = True
TESTING = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'test.db',
		}
	}

SECRET_KEY = "BITlFxZunJXWaoiKhMAE"

ROOT_URLCONF = 'django_autodemo.tests.urls'
STATIC_URL = '/static/'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.staticfiles',
	'django.contrib.admin',

	'django_autodemo',
	)

MIDDLEWARE_CLASSES = (
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	)

DEMO_SETTINGS = {
	'ENABLED': True,
	}
LOGIN_URL = reverse_lazy('django-autodemo:login')
