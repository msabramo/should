# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.4.2'

setup(name='should',
      version=version,
      description="assert with should",
      long_description=open('R.rst').read(),
      keywords='assert,should,test,BDD',
      author='Ralph-Wang',
      author_email='ralph.wang1024@gmail.com',
      url='https://github.com/Ralph-Wang/should',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      py_modules=['should'],
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
