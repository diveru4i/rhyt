#!/usr/bin/env python
import os
import sys


def color_text(text, colorcode):
    return "\x1b[1;{1}m{0}\x1b[0m".format(text, colorcode)


if __name__ == "__main__":
    env = os.environ.get('DPE')
    if not env:
        env = 'dev'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_conf.%s" % env)

    from django.core.management import execute_from_command_line

    sys.stderr.write(color_text(u'Running with DPE=%s\n' % env, 32))
    execute_from_command_line(sys.argv)
