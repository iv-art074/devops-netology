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
  value = aws_instance.server.private_ip  
}  

output "vpc_id" {  
  description = "ID of project VPC"  
  value       = module.vpc.vpc_id  
}  
