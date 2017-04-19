# django-demo-mode/tests/urls.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 19th ,2017
# Description: Test URL configuration.

from django.conf.urls import url, include

from django_demo_mode.tests import views

urlpatterns = [
	url(r'^$', views.DemoView.as_view(), name='demo'),
	url(r'^demo/', include('django_demo_mode.urls'))
	]
