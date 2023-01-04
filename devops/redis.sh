#!/bin/bash
#This script will duplicate the redis example we did in class on 11/1/2022
#This script assumes you have a working docker installation and a working python installation with pip
#Author: Stephen Card <scard@idevops.io>

mkdir redis_docker && cd redis_docker
#Download the Dockerfile and required entrypoint.sh script from github
wget -O Dockerfile https://raw.githubusercontent.com/docker-library/redis/0f2bb676ab5153905089537230a732a77d26e438/6.2/Dockerfile
wget -O docker-entrypoint.sh https://raw.githubusercontent.com/docker-library/redis/0f2bb676ab5153905089537230a732a77d26e438/6.2/docker-entrypoint.sh
#create python test script file
cat << EOF > test-redis.py
import redis
r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

potato = r.get("Bahamas")

print(potato)
EOF

#Pip install the redis library
python3 -m pip install redis

#Docker build & run
docker build -t local/redis:latest .
docker run -p 6379:6379 local/redis:latest

#run test script
python3 test-redis.py
#Expected output is "Nassau" I didn't code the example. Check the Debug Console/Output in vscode to see output.