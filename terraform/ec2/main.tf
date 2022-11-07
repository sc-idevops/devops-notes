terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
}


resource "aws_instance" "web" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"
  subnet_id     = "subnet-087a611422455046f"

  tags = {
# change this to your name
    Name = "scard-terraform-example"
  }
}
