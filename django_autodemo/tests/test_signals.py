# django_autodemo/tests/test_integration.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 20th, 2017
# Description: Test signals.

import re

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase
from django.contrib.auth.models import User

from django_autodemo.settings import DEMO_SETTINGS
from django_autodemo import signals

import mock

_LOGIN_URL = settings.LOGIN_URL
_LOGOUT_URL = reverse_lazy('django-autodemo:logout')
_USER_RE = re.compile(r'^Authenticated as ([a-zA-Z0-9]+)\..*$', re.DOTALL)

class TestSignals(TestCase):
	def get_login_user(self):
		response = self.client.get('/', follow=True)
		matches = _USER_RE.match(response.content.decode('ascii'))
		if not matches:
			self.fail('Does not match username pattern')

		username = matches.group(1)

		try:
			return response, User.objects.get(username=username)
		except User.DoesNotExist:
			return response, None

	def test_login_signal(self):
		'''A login signal should be received with the correct parameters.'''
		self.user_created_signal_sent = False

		def handler(sender, request, user, **kwargs):
			self.user_created_signal_sent = True
			self.received_user = user

		signals.demo_user_created.connect(handler)

		response, self.expected_user = self.get_login_user()
		self.assertEqual(self.received_user, self.expected_user)
		self.assertTrue(self.user_created_signal_sent)

	def test_login_signal_repeated(self):
		'''A login signal should be received with the correct parameters.'''
		self.user_created_signal_count = 0

		def handler(sender, request, user, **kwargs):
			self.user_created_signal_count += 1
			self.received_user = user

		signals.demo_user_created.connect(handler)

		response, self.expected_user = self.get_login_user()
		response2 = self.client.get('/', follow=True)

		self.assertEqual(self.received_user, self.expected_user)
		self.assertEqual(self.user_created_signal_count, 1)

	def test_logout_signal(self):
		'''A logout signal should be sent when the user is logged out.'''
		self.user_logout_signal_sent = False

		def handler(sender, request, user, **kwargs):
			self.user_logout_signal_sent = True
			self.received_user = user

		signals.demo_user_logout.connect(handler)

		response, self.expected_user = self.get_login_user()
		self.client.get(_LOGOUT_URL, follow=True)
		self.assertEqual(self.received_user, self.expected_user)
		self.assertTrue(self.user_logout_signal_sent)

	def test_logout_delete_signal(self):
		'''A logout signal should be sent when the user is logged out.'''
		with mock.patch.dict(DEMO_SETTINGS, {'DELETE_USER': True}):
			self.user_logout_signal_sent = False

			def handler(sender, request, user, **kwargs):
				self.user_logout_signal_sent = True
				self.received_user = user

			signals.demo_user_logout.connect(handler)

			response, self.expected_user = self.get_login_user()
			self.client.get(_LOGOUT_URL, follow=True)
			self.assertEqual(self.received_user.username,
				self.expected_user.username)
			self.assertTrue(self.user_logout_signal_sent)
