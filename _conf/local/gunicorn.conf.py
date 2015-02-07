# -*- coding: utf-8 -*-

bind = '0.0.0.0:2388'
pidfile = '/home/www/rhyt/run/rhyt.gunicorn.pid'
workers = 5
timeout = 900

## Logging
loglevel = 'error'
errorlog = '/home/www/rhyt/log/gunicorn.error.log'
# accesslog = '/home/www/rhyt/log/gunicorn.access.log'
