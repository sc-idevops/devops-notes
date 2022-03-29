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

note it takes like 20 minutes to do `terraform apply` so make sure things are right before committing.

**RUN TERRAFORM DESTROY AFTER TESTING**

----------------

Terraform is stateful, and it stores the current state in a tfstate file.
It records what it does, the state of the configuration. 
It is provider agnostic, you can work with anything and even write your own in python.

## Terraform Conflicts
Only one person can be running terraform against a resource otherwise it will get confused and the state file might be corrupted.
You can use a database in permanent storage (like S3 in AWS) to lock access to a resource.

## Terraform Modules
Modules can be referenced and downloaded from github or stored locally.
They simplify deployments by including all the resorces needed for production and you just have to specify what's needed in one block. 
You can have submodules inside a module.
These make complicated deployments much more simple and easy to automate.

## Terraform Outputs
These outputs objects created in the cloud to your console so you don't have to go look them up yourself.
These can be referenced using object notation.

## Workflow
create a folder with a terraform main.tf file.
Include your provider
execute:
`terraform init`
and then
`terraform plan`
ALWAYS RUN TERRAFORM PLAN FIRST.
Check if you're going to create something if you intend to. (green plus signs)
If you see red minus signs and you didn't want to delete something, something has gone wrong!
`terraform apply` will apply the plan you just created.
**RUN TERRAFORM DESTROY AFTER TESTING**

# Terraform Deployments
To run your terraform file, there is only 1 pipeline with catalog items
Provide the following:
* terraform template: name of the folder name
* what terraform action to do

There's an AWS catalog and an Azure catalog.
Note the folder name must be consistent across all of our directories.

**ALL TECH NEEDS TO BE UPDATED SO TERRAFORM DESTROY CAN RUN CORRECTLY**

```
terraform {
  backend "azurerm" {
    container_name       = "terraformbackend"
    storage_account_name = "idevopsioterraform"
    resource_group_name  = "idevopsio-aks"
    key                  = "terraformbackend"
  }

  required_providers {
    azuredevops = {
      source = "microsoft/azuredevops"
      version = "=0.1.7"
    }
    azurerm = {
      source = "hashicorp/azurerm"
      version = "=2.98.0"
    }
  }
}

provider "azurerm" {
  features {}
}
```
## Terraform Variables
declare variables in vars.tf with:
`variable "name" { }`
reference variables in main.tf with:
`name = var.name`

vars.json contains all variables with `TF_VAR_variableName`
the json file contains the variable values, and the vars.tf just declares them.

