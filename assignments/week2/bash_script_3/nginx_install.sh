#!/bin/bash
#check if installed first
echo "Installing nginx"
sudo apt update
sudo apt -y install nginx

#check status of nginx
sudo systemctl status nginx.service || echo "E: Nginx not started correctly!"
#deploy static page
echo "installing test html file"
echo "<html><title>Test File</title></html>" > /var/www/html/index.html

#check localhost
echo "Checking local host"
curl localhost
