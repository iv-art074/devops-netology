provider "aws" {
        region = "us-east-2"
}

/*resource "aws_instance" "web" {
  ami = "ami-00514a528eadbc95b" // Amazon Linux
  instance_type = "t3.micro"
  
  tags = {Name = "HelloWorld"}
}*/

data "aws_ami" "amazon_linux" {
 most_recent = true
 owners      = ["amazon"]
 filter {
   name = "name"
   values = ["amzn-ami-hvm-*-x86_64-gp2"]
   }
 filter {
   name = "owner-alias"
   values = ["amazon"] 
 }
}

locals {
  web_instance_type_map = {
    stage = "t3.micro"
    prod = "t3.large"
  }
}

resource "aws_instance" "web" {
  ami = data.aws_ami.amazon_linux.id
  instance_type = local.web_instance_type_map[terraform.workspace]
}

locals {
  web_instance_count_map = {
  stage = 1
  prod = 2
  }
}





resource "aws_s3_bucket" "bucket" {
  bucket = "netology-bucket-${count.index}-${terraform.workspace}"
  acl    = "private"
  tags = {
    Name        = "Bucket ${count.index}"
    Environment = terraform.workspace
  }
  count = local.web_instance_count_map[terraform.workspace]
}

locals {
  backets_num = toset([
    "each1",
    "each2",
  ])
}
resource "aws_s3_bucket" "bucket_each" {
  for_each = local.backets_num
  bucket = "netology-bucket-${each.key}-${terraform.workspace}"
  acl    = "private"
  tags = {
    Name        = "Bucket ${each.key}"
    Environment = terraform.workspace
  }
}