"""Setup file for the ansicolors
"""
from setuptools import setup
from setuptools.command.test import test as TestCommand

import io
import re
import sys

def read(*filenames, **kwargs):
    """Red the contents of the given files
    """
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as textfile:
            buf.append(textfile.read())
    return sep.join(buf)

DESCRIPTION = read('README.rst')


SOURCE = read('colors/__init__.py')


PATTERN = re.compile(r'''__version__ = ['"](?P<version>[\d.]+)['"]''')
VERSION = PATTERN.search(SOURCE).group('version')


class PyTest(TestCommand):
    """A basic test engine """
    def finalize_options(self):
        """ Finalize options"""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """ Do the test """
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='ansicolors',
    version=VERSION,
    description='ANSI colors for Python',
    long_description=DESCRIPTION,
    author='Giorgos Verigakis',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    author_email='verigak@gmail.com',
    url='http://github.com/verigak/colors/',
    license='ISC',
    packages=['colors'],
    include_package_data=True,
    platforms='any',
    test_suite='escrapper.test_app',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
        extras_require={
        'testing': ['pytest'],
    }
)
