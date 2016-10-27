#!/bin/env python
# -*- coding: utf-8 -*-

"""An example setup.py."""

from setuptools import setup


def get_readme():
    with open("README.rst") as readme:
        return readme.read()


setup(name="roman_numerals",
      version="0.1",
      description="Utilities for converting between Roman and Arabic numerals.",
      long_description=get_readme(),
      author="Daniel Lee",
      author_email="Daniel.Lee@dwd.de",
      packages=["roman_numerals"],
      scripts=["bin/orobazus"],
      test_suite="roman_numerals.test")
