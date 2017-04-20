# django-demo-mode/tests/views.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th ,2017
# Description: Test views.

from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views import View

class DemoView(LoginRequiredMixin, View):
	def get(self, request):
		return HttpResponse('''Authenticated as {u}.
			<a href="{logout}?next=/">Logout.</a>'''.format(
				logout=reverse('django-demo-mode:logout'),
				u=request.user.username)
				)
