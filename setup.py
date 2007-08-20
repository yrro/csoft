#!/usr/bin/python

from distutils.core import setup

setup (name = 'csoft',
       description = 'Send SMS messages with csoft.co.uk',
       version = '0.1',
       author = 'Sam Morris',
       author_email = 'sam@robots.org.uk',
       url = 'http://robots.org.uk/src/csoft/',

       packages = ('csoft',),
       scripts = ('check_csoft_messages',))
