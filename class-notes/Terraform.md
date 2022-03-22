# Terraform
Terraform is the automation of cloud infrastructure. 
Instead of searching for information on how to make a dockerfile and a kubernetes deployment, we can now automate this. 
Similar to our other deployments we have template files `template.tf` 
We will need to replace some variables, which end up in `vars.tf`
* ami id
    * This is an ID for the amazon machine we will be utilizing for our deployment
* subnets
    * at first we will be using the default already created subnets

Some deployments are really this straightforward.


Something about a vars.json file
it's kind of like your login credentials???

RUN TERRAFORM DESTROY AFTER TESTING
