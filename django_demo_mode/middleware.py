# django_demo_mode/middleware.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Authentication middleware for django-demo-mode.

from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.crypto import get_random_string
from django.db import IntegrityError

class DemoMiddleware(object):
	def __init__(self, get_response=None):
		self.get_response = get_response

	def __call__(self, request):
		if not request.user.is_authenticated() and getattr(settings, 'DEMO_MODE', False):
			ser = None
			attempts = 0

			if user_id:
				return self.get_user(user_id)

			while user is None and attempts < 10:
				try:
					user = User.objects.create(username=get_random_string(150))
				except IntegrityError:
					attempts += 1

			print('User', user.username, user.is_authenticated(), attempts)
			login(request, user)

		if self.get_response:
			return self.get_response(request)
