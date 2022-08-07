## 14.2 Синхронизация секретов с внешними сервисами. Vault"  
#### Задача 1: Работа с модулем Vault  

Запустить модуль Vault конфигураций через утилиту kubectl в установленном minikube  
```  
root@Pappa-note-wsl:/mnt/c/lessons/clokub-homeworks# kubectl apply -f 14.2/vault-pod.yml
pod/14.2-netology-vault created
```  
Получить значение внутреннего IP пода  
```  
root@Pappa-note-wsl:/mnt/c/lessons/clokub-homeworks# kubectl get pod 14.2-netology-vault -o json | jq -c '.status.podIPs'
[{"ip":"10.244.0.3"}]
```  

Запустить второй модуль для использования в качестве клиента  
```
