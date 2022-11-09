terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
}

resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"
  enable_dns_hostnames = true
  tags = {
    Name = "cards-VPC"
  }
}

resource "aws_subnet" "subnet-one" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone    = "us-east-2a"
  tags = {
    Name = "cards-Subnet-1-Public"
  }
}

resource "aws_subnet" "subnet-two" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
  availability_zone    = "us-east-2b"
  tags = {
    Name = "cards-Subnet-2"
  }
}

resource "aws_subnet" "subnet-three" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.3.0/24"
  availability_zone    = "us-east-2c"
  tags = {
    Name = "cards-Subnet-3"
  }
}

resource "aws_route_table" "vpc-route-table" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "cards-Route-Table"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet-one.id
  route_table_id = aws_route_table.vpc-route-table.id
}

resource "aws_route_table_association" "b" {
  subnet_id      = aws_subnet.subnet-two.id
  route_table_id = aws_route_table.vpc-route-table.id
}

resource "aws_route_table_association" "c" {
  subnet_id      = aws_subnet.subnet-three.id
  route_table_id = aws_route_table.vpc-route-table.id
}

resource "aws_route" "r" {
  route_table_id            = aws_route_table.vpc-route-table.id
  destination_cidr_block    = "0.0.0.0/0"
  depends_on                = [aws_route_table.vpc-route-table]
  gateway_id = aws_internet_gateway.gw.id
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "cards-gateway"
  }
}