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
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'], # might need to add systeminfo here.
    #also may need to alter manifest file to include templates and static folders
    entry_points={
          "console_scripts":["comp30670_learning_flask=app:run.py"]})
#check this entry point once issue with run.py is resolved. 

