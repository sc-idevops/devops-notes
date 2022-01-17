#!/usr/bin/env bash
#Get List of Group Names and store in $grp
grp=$(az group list -o tsv --query "[?name].name")

#Iterate through array grp and output resources for that group name
for g in $grp; do
  echo -e "\nResources in Resource Group: $g\n"
  az resource list --output table --resource-group $g
done
