#!/bin/bash
if [ ! $1 ]; then
  echo "please provide a URL to query"
  exit 1
fi 
echo ">> Querying Domain" $1
curl "$1"
