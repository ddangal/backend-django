#!/usr/bin/env bash

chmod 755 /home/ubuntu/hackthon
pip install gunicorn
 
pip install -r /home/ubuntu/hackthon/requirements.txt
#chmod a+x /home/ubuntu/env_migration.sh
#/home/ubuntu/env_migration.sh
cd hackthon
gunicorn --bind 0.0.0.0:8000 wsgi:application
deactivate
sudo cp /home/ubuntu/hackthon/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
