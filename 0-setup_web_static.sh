#!/usr/bin/env bash
# Installs Nginx web server if it is not already installed.
#+ Creates two directories /data/web_static/shared and /data/releases/test if they don't already exist.
#+ Creates a symbolic link /data/web_static/current that points to /data/web_static/releases/test/.
#+ Creates an HTML file named index.html in the /data/web_static/releases/test directory.
#+ Configures Nginx web server to serve the content of /data/web_static/current/ directory to the URL path hbnb_static.

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Welcome to The_Masterminds home" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
