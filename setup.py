#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

chishop = __import__('chishop', {}, {}, [''])

tests_require = []

setup(
    name='chishop',
    version=chishop.__version__,
    description='Simple PyPI server written in Django.',
    author='Ask Solem',
    author_email='askh@opera.com',
    packages=find_packages(),
    include_package_data=True,
    url="http://ask.github.com/chishop",
    zip_safe=False,
    install_requires=[
        'djangopypi>=0.4',
        'South==0.7.1',
        'Django==1.2.1',
        'django-registration==0.8-alpha-1',
        'django-haystack',
        'Whoosh',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: System :: Software Distribution",
        "Programming Language :: Python",
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
