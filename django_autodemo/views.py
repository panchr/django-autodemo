# django_autodemo/views.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Authentication views for django-autodemo.

from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import (authenticate, login,
	REDIRECT_FIELD_NAME, logout)
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db import IntegrityError

from django_autodemo import signals
from django_autodemo.settings import DEMO_SETTINGS

def login_view(request):
	'''
	On an unauthenticated request, automatically generate a user and log that
	user in. This allows for demo users to be made automatically.
	'''
	next_page = request.GET.get(REDIRECT_FIELD_NAME)
	if request.user.is_authenticated():
		# Redirect user if already authenticated.
		return HttpResponseRedirect(next_page)

	if DEMO_SETTINGS['ENABLED']:
		user = None
		attempts = 0

		# Attempt to create user with random username _MAX_ATTEMPTS times.
		while user is None and attempts < DEMO_SETTINGS['MAX_USER_ATTEMPTS']:
			try:
				username=get_random_string(DEMO_SETTINGS['USERNAME_LENGTH'])
				user = User.objects.create(username=username)
			except IntegrityError:
				attempts += 1

	if user:
		user.backend = settings.AUTHENTICATION_BACKENDS[0]
		login(request, user)
		signals.demo_user_created.send(sender=login_view, request=request,
			user=user)

	return HttpResponseRedirect(next_page)

def logout_view(request):
	'''
	On an authenticated request, logout and (optionally) delete the user.
	'''
	next_page = request.GET.get(REDIRECT_FIELD_NAME)
	if not request.user.is_authenticated():
		# Redirect user if not currently authenticated.
		return HttpResponseRedirect(next_page)

	if DEMO_SETTINGS['ENABLED']:
		user = request.user
		logout(request)
		signals.demo_user_logout.send(sender=login_view, request=request,
			user=user)

		if DEMO_SETTINGS['DELETE_USER']:
			user.delete()

	return HttpResponseRedirect(next_page)
