#!/bin/bash

cd /home/wst/www/mailadmin.bsmsite.com
./manage.py runfcgi host=127.0.0.1 port=3000 method=threaded
