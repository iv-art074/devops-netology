#### Задача 1. Регистрация в aws и знакомство с основами  

![Screenshot 2021-12-20 221523](https://user-images.githubusercontent.com/87374285/146766700-4471726b-31de-4b61-ae8f-e3e636e16dc7.png)  

#### Задача 2. Созданием ec2 через терраформ.  

1. Свой образ можно собрать при помощи CloudFormation.
2. Ссылка https://github.com/iv-art074/devops-netology/tree/main/Terraform
```
iv_art@Pappa:/mnt/c/Users/iv_ar/Documents/GitHub/devops-netology/Terraform$

terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.foo will be created
  + resource "aws_instance" "foo" {
      + ami                                  = "ami-005e54dee72cc1d00"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = (known after apply)
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + subnet_id                            = (known after apply)
      + tags_all                             = (known after apply)
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification {
          + capacity_reservation_preference = (known after apply)

          + capacity_reservation_target {
              + capacity_reservation_id = (known after apply)
            }
        }

      + ebs_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + snapshot_id           = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }

      + enclave_options {
          + enabled = (known after apply)
        }

      + ephemeral_block_device {
          + device_name  = (known after apply)
          + no_device    = (known after apply)
          + virtual_name = (known after apply)
        }

      + metadata_options {
          + http_endpoint               = (known after apply)
          + http_put_response_hop_limit = (known after apply)
          + http_tokens                 = (known after apply)
        }

      + network_interface {
          + delete_on_termination = false
          + device_index          = 0
          + network_interface_id  = (known after apply)
        }

      + root_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }
    }

  # aws_instance.web will be created
  + resource "aws_instance" "web" {
      + ami                                  = "ami-0fb653ca2d3203ac1"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t3.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = (known after apply)
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + source_dest_check                    = true
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "HelloWorld"
        }
      + tags_all                             = {
          + "Name" = "HelloWorld"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification {
          + capacity_reservation_preference = (known after apply)

          + capacity_reservation_target {
              + capacity_reservation_id = (known after apply)
            }
        }

      + ebs_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + snapshot_id           = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }

      + enclave_options {
          + enabled = (known after apply)
        }

      + ephemeral_block_device {
          + device_name  = (known after apply)
          + no_device    = (known after apply)
          + virtual_name = (known after apply)
        }

      + metadata_options {
          + http_endpoint               = (known after apply)
          + http_put_response_hop_limit = (known after apply)
          + http_tokens                 = (known after apply)
        }

      + network_interface {
          + delete_on_termination = (known after apply)
          + device_index          = (known after apply)
          + network_interface_id  = (known after apply)
        }

      + root_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }
    }

  # aws_network_interface.foo will be created
  + resource "aws_network_interface" "foo" {
      + arn                = (known after apply)
      + id                 = (known after apply)
      + interface_type     = (known after apply)
      + ipv4_prefix_count  = (known after apply)
      + ipv4_prefixes      = (known after apply)
      + ipv6_address_count = (known after apply)
      + ipv6_addresses     = (known after apply)
      + ipv6_prefix_count  = (known after apply)
      + ipv6_prefixes      = (known after apply)
      + mac_address        = (known after apply)
      + outpost_arn        = (known after apply)
      + owner_id           = (known after apply)
      + private_dns_name   = (known after apply)
      + private_ip         = (known after apply)
      + private_ips        = [
          + "172.16.10.100",
        ]
      + private_ips_count  = (known after apply)
      + security_groups    = (known after apply)
      + source_dest_check  = true
      + subnet_id          = (known after apply)
      + tags               = {
          + "Name" = "primary_network_interface"
        }
      + tags_all           = {
          + "Name" = "primary_network_interface"
        }

      + attachment {
          + attachment_id = (known after apply)
          + device_index  = (known after apply)
          + instance      = (known after apply)
        }
    }

  # aws_subnet.my_subnet will be created
  + resource "aws_subnet" "my_subnet" {
      + arn                             = (known after apply)
      + assign_ipv6_address_on_creation = false
      + availability_zone               = "us-west-2a"
      + availability_zone_id            = (known after apply)
      + cidr_block                      = "172.16.10.0/24"
      + id                              = (known after apply)
      + ipv6_cidr_block_association_id  = (known after apply)
      + map_public_ip_on_launch         = false
      + owner_id                        = (known after apply)
      + tags                            = {
          + "Name" = "tf-example"
        }
      + tags_all                        = {
          + "Name" = "tf-example"
        }
      + vpc_id                          = (known after apply)
    }

  # aws_vpc.my_vpc will be created
  + resource "aws_vpc" "my_vpc" {
      + arn                            = (known after apply)
      + cidr_block                     = "172.16.0.0/16"
      + default_network_acl_id         = (known after apply)
      + default_route_table_id         = (known after apply)
      + default_security_group_id      = (known after apply)
      + dhcp_options_id                = (known after apply)
      + enable_classiclink             = (known after apply)
      + enable_classiclink_dns_support = (known after apply)
      + enable_dns_hostnames           = (known after apply)
      + enable_dns_support             = true
      + id                             = (known after apply)
      + instance_tenancy               = "default"
      + ipv6_association_id            = (known after apply)
      + ipv6_cidr_block                = (known after apply)
      + main_route_table_id            = (known after apply)
      + owner_id                       = (known after apply)
      + tags                           = {  
          + "Name" = "tf-example"  
        }  
      + tags_all                       = {  
          + "Name" = "tf-example"  
        }  
    }  

Plan: 5 to add, 0 to change, 0 to destroy.  

Changes to Outputs:  
  + account_id       = "357970280025"  
  + caller_user      = "AIDAVGWFQ7ZMYUUHIQUBB"  
  + instance_ip_addr = [  
      + "172.16.10.100",  
    ]  
  + region           = "us-east-2"  
  + subnet_id        = (known after apply)  

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────  

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if  
you run "terraform apply" now.  
iv_art@Pappa:/mnt/c/Users/iv_ar/Documents/GitHub/devops-netology/Terraform$  
```
![Screenshot 2021-12-21 221615](https://user-images.githubusercontent.com/87374285/146928507-acf80209-233d-4a02-95a2-c0339f4ec09e.png)  
