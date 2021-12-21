output "account_id" {  
  value = data.aws_caller_identity.current.account_id  
}  

output "caller_user" {  
  value = data.aws_caller_identity.current.user_id  
}  

output "region" {  
  value = data.aws_region.current.name  
}  


output "instance_ip_addr" {  
  value = resource.aws_network_interface.foo.private_ips  
}  


output "subnet_id" {  
  value = resource.aws_network_interface.foo.subnet_id  
}  
