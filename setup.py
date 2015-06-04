#!/usr/bin/env python

from setuptools import setup 

def readme():
    with open('README.md') as f:
        return f.read() 

setup(name='tumblr_terminal',
      version='0.1',
      description='Just another way for you to feed your Tumblr addiction.',
      long_description=readme(),
      url='http://github.com/sahilprasad/tumblr-terminal',
      author='Sahil Prasad',
      author_email='sahilprasad916@gmail.com',
      license='MIT',
      packages=['tumblr_terminal'],
      install_requires=[
          'pytumblr',
          'pyyaml',
          'colorama',
      ],
      entry_points = {
          'console_scripts': ['tumblr=tumblr_terminal.command_line:main'],
      },
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
