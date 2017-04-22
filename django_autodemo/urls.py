# django_autodemo/urls.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 19th, 2017
# Description: Authentication urls for django-autodemo.

from django.conf.urls import url
from django_autodemo.views import login_view, logout_view

app_name = 'django-autodemo'
urlpatterns = [
	url(r'^login$', login_view, name='login'),
	url(r'^logout$', logout_view, name='logout')
	]
