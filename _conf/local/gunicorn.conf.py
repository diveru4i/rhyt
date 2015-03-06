# -*- coding: utf-8 -*-

bind = '0.0.0.0:1488'
pidfile = '/home/www/rhyt/run/rhyt.gunicorn.pid'
workers = 3
timeout = 900

## Logging
loglevel = 'error'
errorlog = '/home/www/rhyt/log/gunicorn.error.log'
# accesslog = '/home/www/rhyt/log/gunicorn.access.log'
