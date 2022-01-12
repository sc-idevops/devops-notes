#!/bin/bash
#check if installed first
echo "Installing nginx"
sudo apt -y install nginx
#check firewall
sudo ufw allow 'Nginx Full'
sudo ufw reload

#deploy static page
echo "installing test html file"
mkdir -pv ~/www
chmod 0755 ~/www
echo "This is the dummy index page." > ~/www/index.html

#configure nginx
echo "server {
        listen 80;
        server_name localhost;
        root /root/www;
        index index.html;
}" > /etc/nginx/sites-available/localhost
ln -s /etc/nginx/sites-available/localhost /etc/nginx/sites-enabled/
sudo systemctl restart nginx

#check localhost
echo "Checking local host"
curl localhost
