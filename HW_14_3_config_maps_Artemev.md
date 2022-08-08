## Задача 1: Работа с картами конфигураций через утилиту kubectl в установленном minikube  
Выполните приведённые команды в консоли. Получите вывод команд. Сохраните задачу 1 как справочный материал.  

#### Как создать карту конфигураций?  
```  
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl create configmap nginx-config --from-file=nginx.conf
configmap/nginx-config created
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3#
```  
#### Как просмотреть список карт конфигураций?  
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl get configmaps
NAME               DATA   AGE
kube-root-ca.crt   1      28h
nginx-config       1      83s
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl get configmap
NAME               DATA   AGE
kube-root-ca.crt   1      28h
nginx-config       1      90s
```  
#### Как просмотреть карту конфигурации?  
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl get configmap nginx-config
NAME           DATA   AGE
nginx-config   1      2m55s

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl describe configmap nginx-config
Name:         nginx-config
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
nginx.conf:
----
server {
    listen 80;
    server_name  netology.ru www.netology.ru;
    access_log  /var/log/nginx/domains/netology.ru-access.log  main;
    error_log   /var/log/nginx/domains/netology.ru-error.log info;
    location / {
        include proxy_params;
        proxy_pass http://10.10.10.10:8080/;
    }
}

BinaryData
====
Events:  <none>

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3#
```  
#### Как получить информацию в формате YAML и/или JSON?  
```  
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl get configmap nginx-config -o yaml
apiVersion: v1
data:
  nginx.conf: |
    server {
        listen 80;
        server_name  netology.ru www.netology.ru;
        access_log  /var/log/nginx/domains/netology.ru-access.log  main;
        error_log   /var/log/nginx/domains/netology.ru-error.log info;
        location / {
            include proxy_params;
            proxy_pass http://10.10.10.10:8080/;
        }
    }
kind: ConfigMap
metadata:
  creationTimestamp: "2022-08-08T11:04:25Z"
  name: nginx-config
  namespace: default
  resourceVersion: "14696"
  uid: db17fd03-343e-431f-8db4-b16cd6ff0295
  
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl get configmap nginx-config -o json
{
    "apiVersion": "v1",
    "data": {
        "nginx.conf": "server {\n    listen 80;\n    server_name  netology.ru www.netology.ru;\n    access_log  /var/log/nginx/domains/netology.ru-access.log  main;\n    error_log   /var/log/nginx/domains/netology.ru-error.log info;\n    location / {\n        include proxy_params;\n        proxy_pass http://10.10.10.10:8080/;\n    }\n}\n"
    },
    "kind": "ConfigMap",
    "metadata": {
        "creationTimestamp": "2022-08-08T11:04:25Z",
        "name": "nginx-config",
        "namespace": "default",
        "resourceVersion": "14696",
        "uid": "db17fd03-343e-431f-8db4-b16cd6ff0295"
    }
}
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3#
```  
#### Как выгрузить карту конфигурации и сохранить его в файл?  
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl get configmaps -o json > configmaps.json
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# ll
total 28
drwxr-xr-x 3 iv_art iv_art 4096 Aug  8 21:11 ./
drwxr-xr-x 7 iv_art iv_art 4096 Aug  7 16:33 ../
-rw-r--r-- 1 root   root   2786 Aug  8 21:11 configmaps.json   #-----------выгружен
-rw-r--r-- 1 iv_art iv_art  370 Aug  7 16:21 generator.py
-rw-r--r-- 1 iv_art iv_art  576 Aug  7 16:21 myapp-pod.yml
-rw-r--r-- 1 iv_art iv_art  306 Aug  7 16:21 nginx.conf
drwxr-xr-x 2 iv_art iv_art 4096 Aug  7 16:21 templates/

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl get configmap nginx-config -o yaml > nginx-config.yml
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# ll
total 32
drwxr-xr-x 3 iv_art iv_art 4096 Aug  8 21:13 ./
drwxr-xr-x 7 iv_art iv_art 4096 Aug  7 16:33 ../
-rw-r--r-- 1 root   root   2786 Aug  8 21:11 configmaps.json
-rw-r--r-- 1 iv_art iv_art  370 Aug  7 16:21 generator.py
-rw-r--r-- 1 iv_art iv_art  576 Aug  7 16:21 myapp-pod.yml
-rw-r--r-- 1 root   root    566 Aug  8 21:13 nginx-config.yml   #---------выгружен
-rw-r--r-- 1 iv_art iv_art  306 Aug  7 16:21 nginx.conf
drwxr-xr-x 2 iv_art iv_art 4096 Aug  7 16:21 templates/
```
#### Как удалить карту конфигурации?  
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl delete configmap nginx-config
configmap "nginx-config" deleted
```
#### Как загрузить карту конфигурации из файла?  
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl apply -f nginx-config.yml
configmap/nginx-config created
```
## Задача 2 (*): Работа с картами конфигураций внутри модуля  
#### Выбрать любимый образ контейнера, подключить карты конфигураций и проверить их доступность как в виде переменных окружения, так и в виде примонтированного тома  

Создаем config-map из файла index.html и выгружаем в файл   
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# cat index.html
<html>
<head>
  <title>Тестовая страница</title>
  <--<meta charset="UTF-8">-->
</head>
<body>
  <h1>Тестовая страница</h1>
  <p>Простая тестовая страница для работы 14-3">
  моём канале</a>.
  </p>
</body>
</html>

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl create configmap index-html --from-file=index.html \
> --dry-run=client -o yaml | sed '/creationTimestamp/d' > 00-index-html.yaml

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# ls
00-index-html.yaml  generator.py  index.html  myapp-pod.yml  nginx.conf  templates
```
Применяем из файла  
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl apply -f 00-index-html.yaml
configmap/index-html created
```

Запускаем под и подключаем volume через deploy   
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# cat deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openty
  namespace: default
  labels:
    app: openty
spec:
  replicas: 1
  selector:
    matchLabels:
      app: openty
  template:
    metadata:
      labels:
        app: openty
    spec:
      containers:
        - name: openty
          image: openresty/openresty:centos-rpm
          env:
            - name: NGINX_HOST
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
          volumeMounts:
            - name: index-html
              mountPath: /usr/local/openresty/nginx/html/index.html
              subPath: index.html
      volumes:
        - name: index-html
          configMap:
            name: index-html

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl apply -f deploy.yaml
deployment.apps/openty created

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.3# kubectl get po
NAME                      READY   STATUS    RESTARTS   AGE
openty-568747bbf4-79rs5   1/1     Running   0          89s
```
