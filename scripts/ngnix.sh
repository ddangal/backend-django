#!/usr/bin/env bash

mkdir -p /etc/nginx/sites-enabled
mkdir -p /etc/nginx/sites-available
rm -rf /etc/nginx/sites-available/hackthon
rm -rf /etc/nginx/sites-enabled/hackthon

sudo cp /home/ubuntu/orlando/nginx/default.conf /etc/nginx/nginx.conf
sudo ls /home/ubuntu/hackthon
sudo systemctl daemon-reload
sudo systemctl restart gunicorn


sudo cp /home/ubuntu/orlando/nginx/staging.conf /etc/nginx/sites-available/hackthon

sudo ln -s /etc/nginx/sites-available/orlando /etc/nginx/sites-enabled/hackthon

# cat /etc/log/nginx/error.log


# sudo systemctl status nginx.service
