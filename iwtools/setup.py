#!/usr/bin/env python

from setuptools import setup

modname = distname = 'iwtools'

setup(
    name=distname,
    py_modules=['iwtools','module'],
    version='0.0.1',
    description='Tools scan network WiFi',
    author='Wander Vilhalva Domingos',
    author_email='wandervilhalvadomingos@gmail.com',
    install_requires=['setuptools'],
    entry_points='''
    [console_scripts]
    iwtools=iwtools:main
    
    '''
)