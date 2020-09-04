#!/usr/bin/env bash
cd /home/ubuntu/hackthon/
#python manage.py makemigrations

python manage.py migrate

sudo service gunicorn stop
sudo service gunicorn start
sudo service nginx restart