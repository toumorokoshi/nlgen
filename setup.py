#!/usr/bin/env python
import os
import sys
try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup

base = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(base, "README.rst")

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name='nlgen',
      version='0.0.6',
      description='natural language generator',
      long_description=open(README_PATH).read(),
      author='Yusuke Tsutsumi',
      author_email='yusuke@tsutsumi.io',
      packages=find_packages(),
      install_requires=[
          "grako"
      ],
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
      ],
      entry_points={
          'console_scripts': []
      },
      setup_requires=pytest_runner,
      tests_require=pytest_runner
)
