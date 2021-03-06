#!/usr/bin/env python
# coding: utf8

import os.path
import re
import sys

from setuptools import setup
import versioneer


ROOT = os.path.dirname(__file__)
README = open(os.path.join(ROOT, 'README.rst')).read()
INIT_PY = open(os.path.join(ROOT, 'cssselect2', '__init__.py')).read()

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(
    name='cnx-cssselect2',
    version=versioneer.get_version(),
    author='OpenStax CNX',
    author_email='info@cnx.org',
    description='CSS selectors for Python ElementTree',
    long_description=README,
    url='https://github.com/connexions/cnx-cssselect2',
    license='BSD',
    cmdclass=versioneer.get_cmdclass(),
    packages=['cssselect2'],
    package_data={'cssselect2': ['tests/*']},
    install_requires=['tinycss2'],
    setup_requires=pytest_runner,
    test_suite='cssselect2.tests',
    tests_require=[
        'pytest-runner', 'pytest-cov', 'pytest-flake8', 'pytest-isort'],
    extras_require={'test': [
        'pytest-runner', 'pytest-cov', 'pytest-flake8', 'pytest-isort']},
)
