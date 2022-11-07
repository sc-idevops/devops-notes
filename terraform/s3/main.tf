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

resource "aws_s3_bucket" "b" {
  bucket = "stephen-card-bucket"

  tags = {
    Name        = "stephen-card-bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.b.id
  acl    = "private"
}

resource "aws_s3_bucket_lifecycle_configuration" "example" {
  bucket = aws_s3_bucket.b.id
  rule {
    status = "Enabled"
    id     = "monthly_retention"

    expiration {
      days = 30
    }
  }
}

resource "aws_iam_role_policy" "my-s3-read-policy" {
  name   = "sc-s3-tf-created-policy"
  role   = "s3-role"
  policy = data.aws_iam_policy_document.s3_read_permissions.json
}

data "aws_iam_policy_document" "s3_read_permissions" {
  statement {
    effect = "Allow"

    actions = [
      "s3:PutObject",
      "s3:DeleteObject",
      "s3:GetObject",
      "s3:GetObjectAcl",
      "s3:ListBucket",
      "s3:ListMultipartUploadParts",
      "s3:AbortMultipartUpload"
    ]

    resources = ["arn:aws:s3:::stephen-card-bucket",
      "arn:aws:s3:::stephen-card-bucket/*"
    ]
  }
}