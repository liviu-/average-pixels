#!/usr/bin/env python3
import os

from setuptools import setup, find_packages


package_name = 'average_pixels'
version_file = 'version.py'

def get_version(package_name=package_name, filename=version_file):
    version_path = os.path.join(package_name, version_file)
    return open(version_path).read().split('=')[-1].strip(' \'"\n')

setup(
    name='average-pixels',
    description='Average pixels from multiple images off Bing Image Search',
    version=get_version(),
    url='https://github.com/liviu-/average-pixels',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy',
        'requests',
        'Pillow'
        ],
    entry_points = {
      "console_scripts": ['average-pixels = average_pixels.average_pixels:main']
          },
)
