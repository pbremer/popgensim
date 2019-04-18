# /usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Simulator for population genetics
# Copyright (C) 2019  Patrick Bremer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import path
from io import open

try:
    # use setuptools, if available, for install_requires
    import setuptools
    from setuptools import setup
except ImportError:
    setuptools = None
    from distutils.core import setup

kwargs = {}

if setuptools is not None:
    python_requires = '>= 3.5'
    kwargs['python_requires'] = python_requires

root_dir = path.abspath(path.dirname(__file__))

with open(path.join(root_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(root_dir, 'popgensim/__init__.py'), encoding='utf-8') as f:
    ns = {}
    exec(f.read(), ns)
    version = ns['__version__']

setup(
    name='PopGenSim',
    version=version,
    description='Population genetics simulator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pbremer/popgensim',
    author='Patrick Bremer',
    packages=['popgensim'],
    **kwargs
)
