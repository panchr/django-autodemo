# setup.py
# django-autodemo
# Author: Rushy Panchal
# Date: April 20th, 2017
# Description: Setuptools configuration.

from setuptools import setup, find_packages

setup(
	name = 'django-autodemo',
	packages = find_packages(),
	version = '0.1.0',
	description = 'Demo mode to allow arbitrary authentication on website.',
	author = 'Rushy Panchal',
	author_email = 'rpanchal@princeton.edu',
	url = 'https://github.com/panchr/django-autodemo',
	keywords = ['django', 'authentication', 'demo'],
	license = 'LGPLv3',
	classifiers = [
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
		],
)