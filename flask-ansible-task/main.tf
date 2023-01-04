provider "aws" {
  region = "us-west-2"
}

terraform {
  backend "s3" {
    bucket         = "idevops-terraform-backend"
    key            = "global/s3/eks.tfstate"
    region         = "us-east-2"
    dynamodb_table = "terraform_state_locking"
    encrypt        = true
  }
}

resource "aws_instance" "ec2_in" {
  ami           = "ami-03f8756d29f0b5f21"
    key_name = "padawan"
  instance_type = "t3.micro"
  tags = {
    Name = "scard"
  }
  vpc_security_group_ids = [aws_security_group.allow_ssh_scard.id]
}

output "ec2_ip" {
  value = aws_instance.ec2_in.public_ip
}

resource "aws_security_group" "allow_ssh_scard" {
  name        = "allow_ssh_scard"
  description = "Allow SSH inbound traffic"
  vpc_id      = "vpc-0cbb666e4acbb30c7"

  ingress {
    description      = "ssh from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_ssh_scard"
  }
}