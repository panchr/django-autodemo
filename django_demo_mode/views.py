# django_demo_mode/views.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Authentication views for django-demo-mode.

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import REDIRECT_FIELD_NAME

def login_view(request):
	user = authenticate(request=request)
	next_page = request.GET.get(REDIRECT_FIELD_NAME)
	return HttpResponseRedirect(next_page)
