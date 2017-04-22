# django_autodemo/tests/test_integration.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 20th, 2017
# Description: Test integration of login/logout behavior.

import re

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase
from django.contrib.auth.models import User

from django_autodemo.settings import DEMO_SETTINGS

import mock

_LOGIN_URL = settings.LOGIN_URL
_LOGOUT_URL = reverse_lazy('django-autodemo:logout')
_USER_RE = re.compile(r'^Authenticated as ([a-zA-Z0-9]+)\..*$', re.DOTALL)

class TestIntegration(TestCase):
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

	def test_automatic_login(self):
		'''Automatic logging in should create a new user.'''
		num_users = User.objects.count()

		response, user = self.get_login_user()
		self.assertIsNotNone(user)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(num_users+1, User.objects.count())

	def test_multiple_login(self):
		'''Automatic logging in multiple users should succeed.'''
		num_users = User.objects.count()

		for _ in range(3):
			response, user = self.get_login_user()
			self.assertIsNotNone(user)
			self.assertEqual(response.status_code, 200)
			self.assertEqual(num_users+1, User.objects.count())

			num_users += 1
			self.client.logout()

	def test_login_preserves_users(self):
		'''Logging in should not affect other users.'''
		User.objects.all().delete()
		User.objects.bulk_create(User(username='test-user-%d' % i) for i in range(25))

		original_users = sorted(User.objects.all(), key=lambda x: x.username)

		response, user = self.get_login_user()
		self.assertIsNotNone(user)
		self.assertEqual(response.status_code, 200)

		user.delete()
		self.assertEqual(original_users,
			sorted(User.objects.all(), key=lambda x: x.username))

	def test_logout(self):
		'''Logging out should not delete a user.'''
		num_users = User.objects.count()

		response, user = self.get_login_user()
		self.assertIsNotNone(user)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(num_users+1, User.objects.count())

		self.client.get(_LOGOUT_URL, follow=True)
		self.assertEqual(num_users+1, User.objects.count())

	def test_logout_delete(self):
		'''
		Logging out a user should delete the user when that setting is enabled.
		'''
		with mock.patch.dict(DEMO_SETTINGS, {'DELETE_USER': True}):
			num_users = User.objects.count()

			response, user = self.get_login_user()
			self.assertIsNotNone(user)
			self.assertEqual(response.status_code, 200)
			self.assertEqual(num_users+1, User.objects.count())

			self.assertEqual(num_users+1, User.objects.count())

			self.client.get(_LOGOUT_URL, follow=True)
			self.assertEqual(num_users, User.objects.count())

	def test_logout_preserves_users(self):
		'''Logging in should not affect other users.'''
		with mock.patch.dict(DEMO_SETTINGS, {'DELETE_USER': True}):
			User.objects.all().delete()
			User.objects.bulk_create(User(username='test-user-%d' % i) for i in range(25))

			original_users = sorted(User.objects.all(), key=lambda x: x.username)

			response, user = self.get_login_user()
			self.assertIsNotNone(user)
			self.assertEqual(response.status_code, 200)

			self.client.get(_LOGOUT_URL, follow=True)
			self.assertEqual(original_users,
				sorted(User.objects.all(), key=lambda x: x.username))
