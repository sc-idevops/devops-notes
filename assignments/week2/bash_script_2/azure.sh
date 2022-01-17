#!/usr/bin/env bash

#List Subscriptions
sub=$(az account show --query 'name')
echo "Subcriptions:" $sub
#Get List of Group Names and store in $grp
grp=$(az group list -o tsv)

for g in "${grp[@]}"; do
  echo $g
  #az resource list --output table --resource-group $g
done
