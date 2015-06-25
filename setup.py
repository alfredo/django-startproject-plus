#!/usr/bin/env python
import os

from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='django-startproject-plus',
      version='0.1b.2',
      description='Django superset startproject command for creating '
      'new projects.',
      long_description=README,
      author='Alfredo Aguirre',
      author_email='hello@madewithbyt.es',
      license='BSD License',
      url='https://github.com/alfredo/django-startproject-plus',
      include_package_data=True,
      package_data={
          'django-startproject_plus': [
              'django-startproject.py',
          ]
      },
      zip_safe=False,
      scripts=['django-startproject.py'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      packages=find_packages(exclude=['tests']),
      install_requires=[])
