#!/usr/bin/env python

import os
import sys

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

PACKAGES = [
    'smolder',
]

REQUIRES = [
    'argh >= 0.26.1',
    'decorator >= 3.4.0',
    'dpath >= 1.2-70',
    'ecdsa >= 0.11',
    'Jinja2 >= 2.7.3',
    'MarkupSafe >= 0.23',
    'requests >= 2.5.0',
    'retry >= 0.4.2',
    'retrying >= 1.3.3',
    'six >= 1.8.0',
    'jsonpickle >= 0.9.2',
    'PyYAML >= 3.11',
    'Yapsy >= 1.11.23',
    'validictory >= 1.0.0',
    'nose >= 1.3.7',
    'httpretty >= 0.8.10'
]

with open('README.md', 'r') as f:
    README = f.read()

with open('HISTORY', 'r') as f:
    HISTORY = f.read()

setup(
    name='smolder',
    version='0.3.0',
    description='Json wrapper around requests for simple smoke testing.',
    long_description=README + '\n\n' + HISTORY,
    author='Max Cameron',
    author_email='maxwell.cameron@bskyb.com',
    url='http://git.bskyb.com/lsd/smolder',
    packages=PACKAGES,
    package_data={'': ['LICENSE', '*.yapsy-plugin']},
    package_dir={'smolder': 'charcoal'},
    scripts=['smolder'],
    include_package_data=True,
    install_requires=REQUIRES,
    license='BSD License',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW / HTTP :: Site Management :: Link Checking',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: Software Development',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Testing'
    ),
)
