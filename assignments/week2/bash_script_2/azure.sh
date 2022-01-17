#!/usr/bin/env bash
#list of subscriptions
sub=$(az account list -o tsv --query "[].name")
#Get List of Group Names and store in $grp
grp=$(az group list -o tsv --query "[].name")

for s in $sub; do
  echo -e "\nSubscription: $s\n"
  #Iterate through array grp and output resources for that group name
  for g in $grp; do
    echo -e "\nResources in Resource Group: $g\n"
    az resource list --output table --resource-group $g
  done
done
