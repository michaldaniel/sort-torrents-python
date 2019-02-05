# -*- coding: utf-8 -*-

from setuptools import setup
import platform
import sys


if sys.version_info[0] != 3 or sys.version_info[1] < 6:
    sys.exit('Sorry, Python < 3.6 is not supported, upgrade from ' + platform.python_version())


setup(name='sort-torrents',
      version='1.0',
      description='Searches source directory for anime video downloads and '
                  'sorts them into directories based on the series name.',
      url='https://morningbird.eu',
      author='Michał Daniel',
      author_email='contact@michaldaniel.eu',
      license='DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE',
      packages=['torrent_sorter'],
      python_requires='>=3.6',
      scripts=['bin/sort-torrents'],
      install_requires=[
      ],
      zip_safe=False)
