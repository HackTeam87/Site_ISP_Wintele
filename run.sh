#!/bin/bash
# root user
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
cd /home/grin/wintele/Site_ISP_Wintele && gunicorn -w 4 app:app -b :5000 --access-logfile /var/log/wintele/access.log --error-logfile /var/log/wintele/error.log
#cd  /home/grin/wintele/Site_ISP_Wintele  &&  python3 app.py
