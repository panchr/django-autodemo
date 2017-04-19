# django-demo-mode/tests/views.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th ,2017
# Description: Test views.

from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class DemoView(LoginRequiredMixin, View):
	def get(self, request):
		if request.user:
			return HttpResponse('Authenticated as %d.' % request.user.username)
		else:
			return HttpResponse('Unauthenticated')
