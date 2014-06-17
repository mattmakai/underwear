#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='underwear',
    version='0.4.5',
    description='Dead simple LAMP-stack deployments for Python-' + \
                'powered web applications',
    long_description=readme + '\n\n' + history,
    author='Matt Makai',
    author_email='matthew.makai@gmail.com',
    url='https://github.com/makaimc/underwear',
    packages=[
        'underwear',
    ],
    package_dir={'underwear': 'underwear'},
    include_package_data=True,
    install_requires=[
        'ansible',
    ],
    license="MIT",
    zip_safe=False,
    keywords=['underwear', 'deployment', 'django', 'LAMP', 
              'WSGI', 'ansible'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
)
