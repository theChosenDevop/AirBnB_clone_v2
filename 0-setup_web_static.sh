#!/usr/bin/env bash
# This scripts sets up your web servers for the deployment of web_static
if ! [ -x "$(command -v nginx)" ]; then
        sudo apt-get update -y && sudo apt upgrade -y
        sudo apt-get install nginx -y
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/

sudo echo "Hello, World!" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo rm /etc/nginx/sites-available/default
sudo echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html;
        server_name _;
        location / {
                try_files $uri $uri/ -404;
        }
}"
sudo service nginx restart
