#!/usr/bin/python
"""
A python wrapper for the QPX cheap flights API.
"""

from setuptools import setup

setup(
    name='flightspy',
    version='0.1dev',
    packages=['flightspy'],
    description='A wrapper for the Google cheap flights API',
    entry_points = {
        'console_scripts': (
            'flightspy = flightspy.cli:main',
            )
    },
    author='Jonathan Cox',
    author_email='jonathan.cox.c@gmail.com',
    license='MIT',
    keywords='QPX api'
)
