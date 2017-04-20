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
		return HttpResponse('Authenticated as %s.' % request.user.username)
