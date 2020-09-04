#!/usr/bin/env bash
cd /home/ubuntu/hackthon/
source /home/ubuntu/envs/bin/activate
#python manage.py makemigrations

python manage.py migrate

sudo service gunicorn stop
sudo service gunicorn start
sudo service nginx restart




