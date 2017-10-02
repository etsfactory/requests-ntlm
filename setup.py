#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='requests_ntlm_sspi',
    version='0.3.0',
    packages=[ 'requests_ntlm_sspi' ],
    install_requires=[ 'requests>=2.0.0', 'python-ntlm3', 'pypiwin32'],
    provides=[ 'requests_ntlm_sspi' ],
    author='Ben Toews',
    author_email='mastahyeti@gmail.com',
    url='https://github.com/etsfactory/requests-ntlm-sspi',
    description='This package allows for HTTP NTLM authentication using the requests library.',
    license='ISC',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: ISC License (ISCL)',
    ],
)
