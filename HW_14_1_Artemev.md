#### Задача 1: Работа с секретами через утилиту kubectl в установленном minikube  
Выполните приведённые ниже команды в консоли, получите вывод команд. Сохраните задачу 1 как справочный материал.  

#### Как создать секрет?  
```  
openssl genrsa -out cert.key 4096
openssl req -x509 -new -key cert.key -days 3650 -out cert.crt \
-subj '/C=RU/ST=Moscow/L=Moscow/CN=server.local'
# kubectl create secret tls domain-cert --cert=certs/cert.crt --key=certs/cert.key

root@minik:~/cri-dockerd# kubectl create secret tls domain-cert --cert=cert.crt --key=cert.key
secret/domain-cert created
root@minik:~/cri-dockerd#
```  
#### Как просмотреть список секретов?
![image](https://user-images.githubusercontent.com/87374285/183049225-b443370f-a0f4-4eba-a0dd-ad7d59a4362e.png)

#### Как просмотреть секрет?
```  
root@minik:~/cri-dockerd# kubectl get secret domain-cert
NAME          TYPE                DATA   AGE
domain-cert   kubernetes.io/tls   2      7m47s
root@minik:~/cri-dockerd# kubectl describe secret domain-cert
Name:         domain-cert
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  kubernetes.io/tls

Data
====
tls.crt:  1944 bytes
tls.key:  3243 bytes
root@minik:~/cri-dockerd#
```  

#### Как получить информацию в формате YAML и/или JSON?
```  
root@minik:~/cri-dockerd# kubectl get secret domain-cert -o yaml
apiVersion: v1
data:
  tls.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tL...
  tls.key: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLR...
kind: Secret
metadata:
  creationTimestamp: "2022-08-05T09:33:10Z"
  name: domain-cert
  namespace: default
  resourceVersion: "791"
  uid: 93e8d795-48a2-4c4c-baa6-f7067bf480ad
type: kubernetes.io/tls

root@minik:~/cri-dockerd# kubectl get secret domain-cert -o json
{
    "apiVersion": "v1",
    "data": {
        "tls.crt": "LS0tLS1CRUdJTiBDRV...
        "tls.key": "LS0tLS1CRUdJTiBSU0...
    },
    "kind": "Secret",
    "metadata": {
        "creationTimestamp": "2022-08-05T09:33:10Z",
        "name": "domain-cert",
        "namespace": "default",
        "resourceVersion": "791",
        "uid": "93e8d795-48a2-4c4c-baa6-f7067bf480ad"
    },
    "type": "kubernetes.io/tls"
}
root@minik:~/cri-dockerd#
```  

#### Как выгрузить секрет и сохранить его в файл?  

```  
root@minik:~/cri-dockerd# kubectl get secrets -o json > secrets.json
root@minik:~/cri-dockerd# kubectl get secret domain-cert -o yaml > domain-cert.yml
root@minik:~/cri-dockerd# ls
backend   cert.key  containermanager  domain-cert.yml  libdocker  Makefile  packaging     store      VERSION
bin       cmd       core              go.mod           LICENSE    metrics   README.md     streaming
cert.crt  config    cri-dockerd       go.sum           main.go    network   secrets.json  utils
root@minik:~/cri-dockerd#
```  

#### Как удалить секрет?  
```  
root@minik:~/cri-dockerd# kubectl delete secret domain-cert
secret "domain-cert" deleted
```  

#### Как загрузить секрет из файла?  
```  
root@minik:~/cri-dockerd# kubectl apply -f domain-cert.yml
secret/domain-cert created
```  

