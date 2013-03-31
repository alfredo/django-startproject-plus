#!/usr/bin/env python
import sys
import json
from optparse import make_option

from django.core.management.commands import startproject


class StartProjectPlus(startproject.Command):

    option_list = startproject.Command.option_list + (
        make_option('--extra_context',
                    action='store', dest='extra_context',
                    help='Extra context in JSON to pass to the templates.'),
    )

    def usage(self, subcommand):
        """Return a brief description of how to use this command, by
        default from the attribute ``self.help``."""
        usage = '%%prog [options] %s' % self.args
        if self.help:
            return '%s\n\n%s' % (usage, self.help)
        else:
            return usage

    def handle(self, *args, **kwargs):
        """Parse the ``extra_context`` flag, as JSON, because it is possible
        to conserve datatypes."""
        if kwargs['extra_context']:
            extra_context = kwargs.pop('extra_context')
            extra_context = json.loads(extra_context)
            kwargs.update(extra_context)
        super(StartProjectPlus, self).handle(*args, **kwargs)


if __name__ == "__main__":
    startproject_plus = StartProjectPlus()
    # Only the flags passed are important because the ``startproject``
    # command is being invoked directly.
    # Fool the parser into believing the command was called via
    # ``django-admin.py startproject``.
    # This is possible because ``django-admin.py`` doesn't require a proper
    # Django installation to execute this command.
    argv = [sys.argv[0]] + ['startproject'] + sys.argv[1:]
    startproject_plus.run_from_argv(argv)
