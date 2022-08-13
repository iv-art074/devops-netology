## Домашнее задание к занятию "14.4 Сервис-аккаунты"  
#### Задача 1: Работа с сервис-аккаунтами через утилиту kubectl в установленном minikube  
Выполните приведённые команды в консоли. Получите вывод команд. Сохраните задачу 1 как справочный материал.  

Как создать сервис-аккаунт?  
```
root@Pappa-wsl:~# kubectl create serviceaccount netology
serviceaccount/netology created
```  

Как просмотреть список сервис-акаунтов?  
```
root@Pappa-wsl:~# kubectl get serviceaccounts
NAME       SECRETS   AGE
default    1         5d20h
netology   1         73s
root@Pappa-wsl:~# kubectl get serviceaccount
NAME       SECRETS   AGE
default    1         5d20h
netology   1         84s
```
Как получить информацию в формате YAML и/или JSON?  
```
root@Pappa-wsl:~# kubectl get serviceaccount netology -o yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: "2022-08-13T02:21:00Z"
  name: netology
  namespace: default
  resourceVersion: "27700"
  uid: 72f016a8-7a8a-4d37-8189-5428d60677b9
secrets:
- name: netology-token-7rpqx
root@Pappa-wsl:~# kubectl get serviceaccount default -o json
{
    "apiVersion": "v1",
    "kind": "ServiceAccount",
    "metadata": {
        "creationTimestamp": "2022-08-07T06:17:06Z",
        "name": "default",
        "namespace": "default",
        "resourceVersion": "462",
        "uid": "817195c2-7803-4bd1-a915-05209097892f"
    },
    "secrets": [
        {
            "name": "default-token-p2k2l"
        }
    ]
}
```
Как выгрузить сервис-акаунты и сохранить его в файл?  
```
root@Pappa-wsl:~# kubectl get serviceaccounts -o json > serviceaccounts.json
root@Pappa-wsl:~# kubectl get serviceaccount netology -o yaml > netology.yml
root@Pappa-wsl:~# ll
total 84
drwx------ 11 root root 4096 Aug 13 12:25 ./
drwxr-xr-x 19 root root 4096 Aug 13 12:00 ../
-rw-------  1 root root 9699 Aug  9 22:49 .bash_history
-rw-r--r--  1 root root 3423 Jun  4 15:34 .bashrc
drwx------  4 root root 4096 Jun 20 15:07 .cache/
drwx------  4 root root 4096 Jun  4 15:34 .config/
drwxr-xr-x  4 root root 4096 Apr 29 22:08 .docker/
-rw-r--r--  1 root root  143 May  1 22:17 .gitconfig
drwxr-xr-x  3 root root 4096 Aug  7 16:16 .kube/
drwx------  3 root root 4096 Apr 29 07:05 .local/
drwxr-xr-x 10 root root 4096 Aug  7 16:13 .minikube/
-rw-r--r--  1 root root    0 Aug 13 12:20 .motd_shown
-rw-r--r--  1 root root  161 Dec  6  2019 .profile
-rw-r--r--  1 root root   72 Apr 29 07:19 .selected_editor
drwx------  2 root root 4096 Jun  4 15:41 .ssh/
-rw-r--r--  1 root root  179 Aug  7 15:56 .wget-hsts
-rw-r--r--  1 root root  237 Aug 13 12:25 netology.yml                #---------файл
-rw-r--r--  1 root root 1121 Aug 13 12:24 serviceaccounts.json        #---------файл
drwx------  3 root root 4096 Aug  7 16:04 snap/
drwxr-xr-x  4 root root 4096 Jun  4 15:34 yandex-cloud/
```
Как удалить сервис-акаунт?  
```
root@Pappa-wsl:~# kubectl delete serviceaccount netology
serviceaccount "netology" deleted
```
Как загрузить сервис-акаунт из файла?  
```
root@Pappa-wsl:~# kubectl apply -f netology.yml
serviceaccount/netology created
root@Pappa-wsl:~# kubectl get sa
NAME       SECRETS   AGE
default    1         5d20h
netology   2         3m54s
```
