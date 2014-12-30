#!/usr/bin/python

from setuptools import setup

setup(name='ramlizer',
      version='0.1.1',
      description='A parser for the RAML (RESTful API Modeling Language) file format.',
      url='https://github.com/SandyChapman/ramlizer',
      author='Sandy Chapman',
      author_email='sandychapman@gmail.com',
      license='MIT',
      packages=['ramlizer'],
      install_requires=['yaml', 'json', 'jsonschema'],
      zip_safe=False)