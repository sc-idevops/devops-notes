#!/bin/bash
if [ ! $1 ]; then
  echo "please provide a URL to query"
  exit 1
fi 
curl "$1"
