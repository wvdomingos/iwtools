#!/usr/bin/env python3

from setuptools import setup
from module import VERSION

modname = distname = 'iwtools'

setup(
    name=distname,
    python_requires='>3.6',
    py_modules=['__init__','iwtools','module'],
    version=VERSION,
    description='Tool for real-time monitoring of wireless network devices.',
    long_description="""
        IwTools is tool for real-time monitoring of wireless network devices.
        """,
    author='Wander Vilhalva Domingos',
    author_email='wander.domingos@edu.ufes.br',
    install_requires=['setuptools'],
    entry_points='''
    [console_scripts]
    iwtools=iwtools:main
    '''
)