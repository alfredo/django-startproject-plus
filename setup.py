#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-startproject-plus',
      version='0.1a',
      description='Django superset startproject command for creating '
      'new projects.',
      long_description='Drop-in replacement for django-admin.py supersets '
      'the command by adding extra_context support.',
      author='Alfredo Aguirre',
      author_email='hello@madewithbyt.es',
      license='BSD License',
      url='https://github.com/alfredo/django-startproject-plus',
      include_package_data=True,
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
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: WSGI',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      packages=find_packages(exclude=['tests']),
      install_requires=[])
