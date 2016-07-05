#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from companycase import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
    name='companycase',
    version=__version__,
    author='Nagarjuna Kumar',
    author_email='nagarjuna.kumar@duedil.com',
    packages=['companycase'],
    url='https://github.com/nk412/companycase',
    license=open('LICENSE').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3'
    ],
    description='Proper word casing for company names',
    long_description=open_file('README.md').read(),
    zip_safe=True,
)