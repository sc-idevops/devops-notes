#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.chdir('/usr/')
path = os.getcwd()
name = "bash"
print(">> Current Directory: ", os.getcwd())
print(">> Scanning for: ", name)

for root, dirs, files in os.walk(path):
    if name in files:
        print(os.path.join(root,name))
