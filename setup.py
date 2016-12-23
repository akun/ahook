#!/usr/bin/env python

from setuptools import setup, find_packages

from ahook import __version__


setup(
    name='ahook',
    version=__version__,
    description='a collection of Git hooks',
    author='akun',
    author_email='6awkun@gmail.com',
    license='MIT License',
    url='https://github.com/akun/ahook',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'six>=1.10.0',
    ],
    extras_require={
        'dev': [
            'bandit>=1.3.0',
            'prospector>=0.12.4',
        ],
        'test': [
            'coverage>=4.2',
            'coveralls>=1.1',
            'nose>=1.3.7',
            'python-coveralls>=2.9.0',
        ],
        'docs': [
            'Sphinx>=1.5.1',
            'sphinx_rtd_theme>=0.1.9',
        ],
    },
    test_suite='nose.collector',
)
