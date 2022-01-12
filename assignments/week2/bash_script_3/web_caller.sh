#!/bin/bash
#which nginx
echo "Installing nginx"
sudo apt install nginx

#deploy static page
echo "installing test html file"
mkdir -pv ~/www
