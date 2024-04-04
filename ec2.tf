provider "aws" {
  region = var.region # Change this to your desired region
}

resource "aws_instance" "example" {
  ami           = var.ami           # Change this to your desired AMI ID
  instance_type = var.instance_type # Change this to your desired instance type

  # Uncomment the following lines if you want to assign a specific subnet and security group
  # subnet_id     = "subnet-12345678"
  # vpc_security_group_ids = ["sg-12345678"]

  tags = {
    Name = var.Name
  }
}
