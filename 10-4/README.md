#### ELK пакет  
```
необходимо поднять в докере:  

elasticsearch(hot и warm ноды)  
logstash  
kibana  
filebeat  
и связать их между собой.  

Logstash следует сконфигурировать для приёма по tcp json сообщений.  

Filebeat следует сконфигурировать для отправки логов приложения run.py в logstash.
```
Одна из самых сложных домашних работ, над которой бился неделю из-за особенностей WSL (отсутствует systemd).   

Сначала отправил для оценки и комментариев  
https://github.com/iv-art074/devops-netology/blob/10-4/10-4/HW_10.4_Artemev.md   

потом обошел проблему через выгрузку логов напрямую в файл и победил )  
https://github.com/iv-art074/devops-netology/blob/10-4/10-4/10-4-5/addition.md
