Django startproject
===================

Wrapper around Django's ``startproject`` command. Supersets the command by adding an ``--extra_context`` flag.

This command can be invoked with the same flags that ``startproject`` supports.


Why?
----

The template functionality on Django's ``startproject`` command is great, but a template system without support for more context variables is not very helpful with more complex setups.

This issue has been brought up to the django-devs mailing list https://code.djangoproject.com/ticket/18277


Installation
------------

This package requires Django 1.5.x installed.

The package is available in pypi::

    pip install django-startproject-plus


Usage
-----

This is a drop in replacement for the django-admin.py startup, with an ``extra_context`` flag::


  django-startproject.py myproject --extra_context='{"some": "json"}'


TODO
----

- Support ``django-admin.py startapp``.
