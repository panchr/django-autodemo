# django_autodemo/signals.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 20th, 2017
# Description: Signals for django-autodemo.

from django.dispatch import Signal

demo_user_created = Signal(providing_args=('request', 'user'))
demo_user_logout = Signal(providing_args=('request', 'user'))
