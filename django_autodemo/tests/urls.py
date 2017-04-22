# django-autodemo/tests/urls.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 19th ,2017
# Description: Test URL configuration.

from django.conf.urls import url, include
from django_autodemo.tests import views

urlpatterns = [
	url(r'^$', views.demo_view, name='demo'),
	url(r'^demo/', include('django_autodemo.urls'))
	]
