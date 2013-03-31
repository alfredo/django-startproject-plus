Django startproject
===================

Provides an ``--extra_context`` flag for the django-admin.py startproject command.

More info see: https://code.djangoproject.com/ticket/18277

Only tested on Django 1.5.x

Usage
-----

This is a drop in replacement for the django-admin.py startup, with an ``extra_context`` flag


    django-startproject.py --extra_context='{"some": "json"}'
