# django_autodemo/settings.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 20th, 2017
# Description: Automatically load settings

from django.conf import settings

DEFAULT_SETTINGS = {
	'ENABLED': False,
	'MAX_USER_ATTEMPTS': 10,
	'USERNAME_LENGTH': 16,
	'DELETE_USER': False,
	}

DEMO_SETTINGS = DEFAULT_SETTINGS.copy()
DEMO_SETTINGS.update(getattr(settings, 'DEMO_SETTINGS', {}))
