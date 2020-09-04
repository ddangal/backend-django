#!/usr/bin/env bash
apt-get update
apt-get install build-essential libssl-dev libffi-dev python-dev python3-dev -y
apt-get install libxml2-dev libxslt1-dev zlib1g-dev -y
apt-get install python3-dev libmysqlclient-dev -y
apt-get install python3-dev -y
apt-get install nginx -y

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

pip install virtualenv

/etc/init.d/nginx stop
