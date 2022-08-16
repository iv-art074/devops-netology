# Домашнее задание к занятию "14.5 SecurityContext, NetworkPolicies"  
#### Задача 1: Рассмотрите пример 14.5/example-security-context.yml  
Создайте модуль  
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks# kubectl apply -f 14.5/example-security-context.yml
pod/security-context-demo created
```
Проверьте установленные настройки внутри контейнера  
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks# kubectl logs security-context-demo
uid=1000 gid=3000 groups=3000
```
