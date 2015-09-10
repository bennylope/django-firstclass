#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import firstclass
from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='pony-express',
    version=firstclass.__version__,
    license='MIT',
    author='Ben Lopatin, Andrew McCloud',
    author_email='ben@wellfire.co',
    url='http://github.com/bennylope/django-firstclass/',
    description='Proxy email backend for Django for global email transformations',
    long_description=readme + '\n\n' + history,
    packages=find_packages(exclude=['tests']),
    install_requires=open('requirements.txt').readlines(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development'
    ],
)
