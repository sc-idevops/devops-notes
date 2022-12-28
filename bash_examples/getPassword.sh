#!/bin/bash
# pull password from passwords.idevops.io
# select the password using jq
curl -s https://passwords.idevops.io | jq -r '.password' 
