# runtests.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 20th, 2017
# Description: Test runner for Django application.
# See: https://docs.djangoproject.com/en/1.9/topics/testing/advanced/#using-the-django-test-runner-to-test-reusable-applications

import os
import sys

import django
from django.test.runner import DiscoverRunner

if __name__ == "__main__":
	os.environ['DJANGO_SETTINGS_MODULE'] = 'django_autodemo.tests.settings'
	django.setup()
	runner = DiscoverRunner()
	failures = runner.run_tests([])
	sys.exit(bool(failures))
