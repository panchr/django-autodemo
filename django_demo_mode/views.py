# django_demo_mode/views.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Authentication views for django-demo-mode.

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import (authenticate, login,
	REDIRECT_FIELD_NAME, logout)
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db import IntegrityError

from django_demo_mode import signals

_IN_DEMO_MODE = getattr(settings, 'DEMO_ENABLED', False)
_MAX_ATTEMPTS = getattr(settings, 'DEMO_MAX_USER_ATTEMPTS', 10)
_USERNAME_LENGTH = getattr(settings, 'DEMO_USERNAME_LENGTH', 16)
_DELETE_USER = getattr(settings, 'DEMO_DELETE_USER', False)

def login_view(request):
	'''
	On an unauthenticated request, automatically generate a user and log that
	user in. This allows for demo users to be made automatically.
	'''
	next_page = request.GET.get(REDIRECT_FIELD_NAME)
	if request.user.is_authenticated():
		# Redirect user if already authenticated.
		return HttpResponseRedirect(next_page)

	if _IN_DEMO_MODE:
		user = None
		attempts = 0

		# Attempt to create user with random username _MAX_ATTEMPTS times.
		while user is None and attempts < _MAX_ATTEMPTS:
			try:
				user = User.objects.create(username=get_random_string(_USERNAME_LENGTH))
			except IntegrityError:
				attempts += 1

	if user:
		login(request, user)
		signals.demo_user_created.send(sender=login_view, request=request,
			user=user)

	return HttpResponseRedirect(next_page)

def logout_delete_view(request):
	'''
	On an authenticated request, logout and delete the user.
	'''
	next_page = request.GET.get(REDIRECT_FIELD_NAME)
	if not request.user.is_authenticated():
		# Redirect user if not currently authenticated.
		return HttpResponseRedirect(next_page)

	if _IN_DEMO_MODE:
		logout(request, request.user)
		signals.demo_user_logout.send(sender=login_view, request=request,
			user=request.user)
		
		if _DELETE_USER:
			request.user.delete()

	return HttpResponseRedirect(next_page)
