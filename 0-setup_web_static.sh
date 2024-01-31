#!/usr/bin/env bash
# This scripts sets up your web servers for the deployment of web_static
if ! command -v nginx &> /dev/null
then
        sudo apt-get update && sudo apt-get upgrade -y
        sudo apt-get install nginx -y
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Hello, World!" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias \
	     /data/web_static/current/;\n}\n' \
	     /etc/nginx/sites-available/default
sudo service nginx restart
