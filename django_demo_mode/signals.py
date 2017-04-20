# django_demo_mode/signals.py
# django-demo-mode
# Author: Rushy Panchal
# Date: April 20th, 2017
# Description: Signals for django-demo-mode.

from django.dispatch import Signal

demo_user_created = Signal(providing_args=('request', 'user'))
demo_user_logout = Signal(providing_args=('request', 'user'))
