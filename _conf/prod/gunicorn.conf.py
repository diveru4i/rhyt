# -*- coding: utf-8 -*-

bind = '127.0.0.1:1588'
pidfile = '/home/www/opirogova/run/opirogova.gunicorn.pid'
workers = 3
timeout = 900

## Logging
loglevel = 'error'
errorlog = '/home/www/opirogova/log/gunicorn.error.log'
accesslog = '/home/www/opirogova/log/gunicorn.access.log'
