#!/bin/bash
#check if installed first
echo "Installing nginx"
sudo apt install nginx
#check firewall
sudo ufw allow 'Nginx Full'
sudo ufw reload

#deploy static page
echo "installing test html file"
mkdir -pv ~/www
chmod 0755 ~/www
echo "This is the dummy index page." > ~/www/index.html

#check localhost
echo "Checking local host"
curl localhost
