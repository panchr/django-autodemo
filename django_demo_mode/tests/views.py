# django-demo-mode/tests/views.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th ,2017
# Description: Test views.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

@login_required
def demo_view(request):
	return HttpResponse('''Authenticated as {u}.
		<a href="{logout}?next=/">Logout.</a>'''.format(
			logout=reverse('django-demo-mode:logout'),
			u=request.user.username)
			)
