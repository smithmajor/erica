# -*- coding: utf-8 -*-
#
# Copyright 2008,2009  Benoit Chesneau <benoitc@e-engura.org>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at#
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
import sys

if not hasattr(sys, 'version_info') or sys.version_info < (2, 5, 0, 'final'):
    raise SystemExit("Couchapp requires Python 2.5 or later.")

try:
    from setuptools import setup
except:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

data_files = []

for dir, dirs, files in os.walk('templates'):
    data_files.append((os.path.join('couchapp', dir), 
        [os.path.join(dir, file_) for file_ in files]))

for dir, dirs, files in os.walk('vendor'):
    data_files.append((os.path.join('couchapp', dir), 
        [os.path.join(dir, file_) for file_ in files]))
    

scripts = ['bin/couchapp']    
    
packages = ['couchapp', 'couchapp.simplejson', 'couchappext', 'couchappext.compress',]

setup(
    name = 'Couchapp',
    version = '0.5',
    url = 'http://github.com/couchapp/couchapp/tree/master',
    license =  'Apache License 2',
    author = 'Benoit Chesneau',
    author_email = 'benoitc@e-engura.org',
    description = 'Standalone CouchDB Application Development Made Simple.',
    long_description = """CouchApp is a set of helpers and a jQuery plugin
    that conspire to get you up and running on CouchDB quickly and
    correctly. It brings clarity and order to the freedom of CouchDB's
    document-based approach.""",
    keywords = 'couchdb couchapp',
    platforms = ['any'],

    packages=packages,
    data_files = data_files,
    include_package_data = True,
    
    install_requires = [],
    scripts = scripts,
    options = dict(py2exe=dict(packages=['couchappext']),
                   bdist_mpkg=dict(zipdist=True,
                                   license='LICENSE',
                                   readme='contrib/macosx/Readme.html',
                                   welcome='contrib/macosx/Welcome.html')),
    classifiers = [
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Utilities',
    ],
    test_suite='tests',
)
