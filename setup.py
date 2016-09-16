#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup

setup(name='nlgen',
      version='0.0.4',
      description='natural language generator',
      long_description="the language game.",
      author='Yusuke Tsutsumi',
      author_email='yusuke@tsutsumi.io',
      packages=find_packages(),
      install_requires=[
          "grako"
      ],
      classifiers=[
          'Programming Language :: Python :: 3',
      ],
      entry_points={
          'console_scripts': []
      },
      tests_require=[]
)
