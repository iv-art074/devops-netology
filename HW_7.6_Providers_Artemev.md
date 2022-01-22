##### 1. Найдите, где перечислены все доступные resource и data_source, приложите ссылку на эти строки в коде на гитхабе.

    resource = https://github.com/hashicorp/terraform-provider-aws/blob/c2b6a0b653ad8084a63bbe4bf5ff0cee43dda34b/aws/provider.go#L398
    data_source = https://github.com/hashicorp/terraform-provider-aws/blob/c2b6a0b653ad8084a63bbe4bf5ff0cee43dda34b/aws/provider.go#L167
    

##### 2. Для создания очереди сообщений SQS используется ресурс aws_sqs_queue у которого есть параметр name.
- С каким другим параметром конфликтует name? Приложите строчку кода, в которой это указано.
 - 	ConflictsWith: []string{"name_prefix"},
         https://github.com/hashicorp/terraform-provider-aws/blob/c2b6a0b653ad8084a63bbe4bf5ff0cee43dda34b/aws/resource_aws_sqs_queue.go#L56  

- Какова максимальная длина имени? 
 -  Длина строки не более 80  символов:
         errors = append(errors, fmt.Errorf("%q cannot be longer than 80 characters", k))
         https://github.com/hashicorp/terraform-provider-aws/blob/c2b6a0b653ad8084a63bbe4bf5ff0cee43dda34b/aws/validators.go#L1035

- Какому регулярному выражению должно подчиняться имя?
https://github.com/hashicorp/terraform-provider-aws/blob/c2b6a0b653ad8084a63bbe4bf5ff0cee43dda34b/aws/validators.go#L1060
 `^[0-9A-Za-z-_]+(\.fifo)?$` - может содержать только буквы и символы +".fifo" в конце
                 есть еще 2 доп условия ниже по коду : 
                     NonFifo = `^[0-9A-Za-z-_]+$` - может содержать только буквы, цифры, подчеркивание, 
                     Fifo = `^[0-9A-Za-z-_.]+$` - так же может содержать только буквы, цифры, подчеркивание, а так же точку, 
                            `^[^a-zA-Z0-9-_]` -  и при этом начинаться только с букв, цифр, подчеркивания,
         
