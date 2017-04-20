# django_demo_mode/backends.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Authentication backends for django-demo-mode.

from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db import IntegrityError

class DemoBackend(object):
	def authenticate(self, request=None, user_id=None):
		'''
		Attempt to generate a random user for the request.
		'''
		print('called!')
		if getattr(settings, 'DEMO_MODE', False):
			user = None
			attempts = 0

			if user_id:
				return self.get_user(user_id)

			while user is None and attempts < 10:
				try:
					user = User.objects.create(username=get_random_string(150))
				except IntegrityError:
					attempts += 1

			print('User', user.username, user.is_authenticated(), attempts)
			return user
		else:
			return None

	def get_user(self, user_id):
		'''
		Get the user given the user's ID.

		:param user_id: user's ID

		:return: User object or None if not found
		:rtype: django.contrib.auth.models.User
		'''
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
