#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

setup(
  name = 'SQLtoDICT',
  packages = ['SQLtoDICT'],
  version = '0.1',
  description = 'Raw sql results returns as dictionary',
  author = u'Barbaros YILDIRIM',
  author_email = 'barbarosaliyildirim@gmail.com',
  url = 'https://github.com/RedXBeard/python-sqldict',
  download_url = 'https://github.com/RedXBeard/python-sqldict/tarball/0.1',
  keywords = ['sql','dict','sql to dict'],
  classifiers = [
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Natural Language :: English',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
  ],
  long_description = long_description
)
