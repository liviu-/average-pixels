#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='average_pixels',
      version='0.0.1',
      description='Average pixels from multiple images off Bing Image Search',
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
        "console_scripts": ['average_pixels = average_pixels.average_pixels:main']
	    },
      )
