# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages



setup(
    name='learning_flask',
    version='0.1.0',
    description='learning flask basics',
    author='Martin Casey',
    author_email='martin.casey@ucdconnect.ie',
    url='https://github.com/MartinC20xx/learning_flask',
    packages=['app'],
    entry_points={
          "console_scripts":['comp30670_learning_flask=app.run']})
#check this entry point once issue with run.py is resolved. 

