#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
cd /home/grin/wintele/app_wintele  && gunicorn -w 4 app:app -b :5000
