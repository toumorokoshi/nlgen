#!/usr/bin/env python
import sys

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name='nlgen',
      version='0.0.5',
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
