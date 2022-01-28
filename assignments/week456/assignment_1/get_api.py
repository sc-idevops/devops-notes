#!/usr/bin/env python
# -*- coding: utf-8 -*-

#reference https://docs.python-requests.org/en/latest/user/quickstart/
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)

data = r.json()

print("The first index of data from", url, "is:")
print(data[0])
