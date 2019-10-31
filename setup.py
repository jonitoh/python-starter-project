# -*- coding: utf-8 -*-
"""Setup"""
from setuptools import setup, find_packages
from codecs import open # To use a consistent encoding
from os import path, environ


HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'DESCRIPTION'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open(path.join(HERE, 'LICENSE'), encoding='utf-8') as f:
    LICENSE = f.read()


setup(
    # Application name:
    name="base",

    # Version number (initial):
    version='1.0.0',

    # Application author details:
    author='jonitoh',
    author_email='njordant@hotmail.com',

    # Details
    url='',
    description='Starter project for any application',
    long_description=LNG_DESC,
    license=LICENSE_,

    #
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Topic :: Other/Nonlisted Topic',
    ],

    #
    keywords='jonitoh starter python',

    # Packages
    packages=find_packages(exclude=["*.tests", "*.tests.*", "docs"]),

    # Include additional files into a package
    include_package_data=True,
    
    # Dependent packages (distributions)
    install_requires=[
    ],

    # #
    # extras_require={
    #   'dotenv': [],
    #   'dev': [
    #       'coverage',
    #       'unittest'
    #   ],
    # },

    #
    entry_points={
        'console_scripts':[
            'base = base.main:main',
        ]
    },
)
