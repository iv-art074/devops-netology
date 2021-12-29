#### Задача 2. Написать серверный конфиг для атлантиса.

Файлы:
https://github.com/iv-art074/devops-netology/tree/main/Terraform/ec2_module 

servers.yaml
```
#repos lists the config for specific repos.
repos:
  
- id: github.com/iv-art074/devops-netology

  apply_requirements: [mergeable]
  
  workflow: custom
  
  allowed_overrides: [workflow]

  allowed_workflows: [custom]

  allow_custom_workflows: true
  
workflows:
  # It's important that this is "default".
  default:
    plan:
      steps:
      - init
      - plan:
          extra_args: ["-lock=false"]
```

atlantis.yaml
```
version: 3
automerge: true
delete_source_branch_on_merge: true
projects:
- name: project1
  dir: .
  workspace: stage
    autoplan:
    when_modified: ["*.tf"]
    enabled: true
  workspace: prod
    autoplan:
    when_modified: ["*.tf"]
    enabled: true
  apply_requirements: [mergeable]
  workflow: myworkflow
workflows:
  myworkflow:
    plan:
      steps:
      - init
      - plan:
          extra_args: ["-lock", "false"]
    apply:
      steps:
      - apply
```
#### Задача 3. Знакомство с каталогом модулей.

Модули удобно использовать для сложной инфраструктуры с сотнями строк конфигураций, они снижают вероятность ошибок с повторениями кода, названий ресурсов. Оптимизируется время при повторном использовании конфигурации, применение модулей обеспечивает большую безопасность, т.к. включают передовые методы конфигурирования. 
Я бы стал использовать готовый модуль на серьезных проектах после проверки кода, на тестовых и небольших работ достаточно упрощенного варианта ресурса aws_instance.

https://github.com/iv-art074/devops-netology/tree/main/Terraform/ec2_module
main.tf
```
provider "aws" {
        region = "us-east-2"
}

module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 3.0"

  name = "devops-netology"

  ami                    = "ami-ebd02392"
  instance_type          = "t2.micro"
  key_name               = "ivart"
  monitoring             = true
  vpc_security_group_ids = ["sg-12345678"]
  subnet_id              = "subnet-eddcdzz4"

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```
![Screenshot 2021-12-29 200239](https://user-images.githubusercontent.com/87374285/147650594-30b0daab-6eed-4907-a862-96b088dcfd85.png)



