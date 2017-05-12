#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

is_release = False
if "--release" in sys.argv:
    sys.argv.remove("--release")
    is_release = True

base = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(base, "README.rst")

setup(name='nlgen',
      setup_requires=["vcver==0.0.8"],
      vcver={"is_release": is_release, "path": base},
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
      })
