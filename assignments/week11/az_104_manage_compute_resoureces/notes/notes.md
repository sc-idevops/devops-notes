## Hosting a web app with azure app service
az webapp up requires certain things:
`export APPNAME=$(az webapp list --query [0].name --output tsv)
export APPRG=$(az webapp list --query [0].resourceGroup --output tsv)
export APPPLAN=$(az appservice plan list --query [0].name --output tsv)
export APPSKU=$(az appservice plan list --query [0].sku.name --output tsv)
export APPLOCATION=$(az appservice plan list --query [0].location --output tsv)`


