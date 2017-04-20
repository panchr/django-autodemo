# django_demo_mode/views.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Authentication views for django-demo-mode.

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db import IntegrityError

def login_view(request):
	next_page = request.GET.get(REDIRECT_FIELD_NAME)
	if request.user.is_authenticated():
		return HttpResponseRedirect(next_page)

	if getattr(settings, 'DEMO_MODE', False):
		user = None
		created_password = ''
		attempts = 0

		while user is None and attempts < 10:
			try:
				user = User.objects.create(username=get_random_string(16))
			except IntegrityError:
				attempts += 1

	if user:
		login(request, user)

	return HttpResponseRedirect(next_page)
