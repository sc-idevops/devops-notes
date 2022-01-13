#!/bin/bash
#check if installed first
echo "Installing nginx"
sudo apt update
sudo apt -y install nginx

#deploy static page
echo "installing test html file"
sudo rm /var/www/html/index.html
echo "Test File" > /var/www/html/index.html

#check test.idevops.com
echo "Checking local host"
curl localhost
