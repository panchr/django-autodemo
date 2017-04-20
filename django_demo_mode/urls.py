# django_demo_mode/urls.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Authentication urls for django-demo-mode.

from django.conf.urls import url
from django_demo_mode.views import login_view, logout_view

app_name = 'django-demo-mode'
urlpatterns = [
	url(r'^login$', login_view, name='login'),
	url(r'^logout$', logout_view, name='logout')
	]
