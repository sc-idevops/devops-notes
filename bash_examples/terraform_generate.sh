#!/bin/bash
echo "Welcome to terraform, we're going to build a main.tf file to create an amazon aws ec2 instance"
echo "terraform {
  required_providers {
    aws = {
      source  = \"hashicorp/aws\"
      version = \"~> 4.0\"
    }
  }
}

provider \"aws\" { " > main.tf

echo "please specify what region you want to use for the provider: (e.g. us-west-2)"
read -p 'region: ' region

echo "  region = \"$region\"
}" >> main.tf

echo "Please provide a name for the ec2 instance:"
read instance
echo "resource \"aws_instance\" \"$instance\" {" >> main.tf

echo "What is the AMI? (e.g. ami-830c94e3)"
read ami
echo "  ami = \"$ami\"" >> main.tf

echo "Provide Instance Type (e.g. t2.micro)"
read instance_type
echo "  instance_type = \"$instance_type\"" >> main.tf

echo "please provide subnet ID. (e.g. subnet-087a611422455046f)"
read subnet
echo "  subnet_id = \"$subnet\"" >> main.tf

echo "provide a name tag, because that's all you're getting in version 1"
read tag
echo "  tags = {
    Name = \"$tag\"
  }
}" >> main.tf

echo "The main.tf file should be built now, exec terraform init, validate, and apply"
echo "--------"
terraform init
terraform validate && terraform apply --auto-approve
