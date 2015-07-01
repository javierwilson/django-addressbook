# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-addressbook',
    version='0.1.33',
    author=u'Ben Lee',
    author_email='ben86lee@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'django-countries',
        'vobject',
        'django-crispy-forms-ng',
	'django-taggit',
        'easy-thumbnails',
    ],
    url='https://github.com/iiilx/addressbook',
    license='BSD license, see LICENSE.txt',
    description='A django app that allows users to create contact groups and contacts, as well as views for displaying a contact in hcard format, downloading a vcard for the contact, a gravatar, and a QR code.',
    long_description=open('README.rst').read(),
    zip_safe=False,
)
