#### Задание 1: Запуск пода из образа в деплойменте  
создавал в Yandex Cloud  

```
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
root@kuberserv:~/.kube# minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

root@kuberserv:~/.kube# kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4 --replicas=2
deployment.apps/hello-node created
root@kuberserv:/home/jean# kubectl get deploy
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
hello-node   2/2     2            2           11m
root@kuberserv:/home/jean# kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-6b89d599b9-frvjj   1/1     Running   0          11m
hello-node-6b89d599b9-mhlwb   1/1     Running   0          11m
root@kuberserv:/home/jean#
```  

#### Задание 2: Просмотр логов для разработки  
Разработчикам крайне важно получать обратную связь от штатно работающего приложения и, еще важнее, об ошибках в его работе. Требуется создать пользователя и выдать ему доступ на чтение конфигурации и логов подов в app-namespace.  


аналогично https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources создал пользователя jean, сгенерировал сертификат
```
openssl genrsa -out jean.key 2048
openssl req -new -key jean.key -out jean.csr -subj "/CN=jean"
openssl x509 -req -in jean.csr -CA ~/minikube/ca.crt -CAkey ~/minikube/ca.key -CAcreateserial -out jean.crt -days 500
```  
(брал отсюда https://habr.com/ru/company/flant/blog/470503/)  

Создал пользователя внутри Kubernetes:  

kubectl config set-credentials jean --client-certificate=/home/jean/.certs/jean.crt --client-key=/home/jean/.certs/jean.key  

Задал контекст для пользователя:   

kubectl config set-context jean-context --cluster=kubernetes --user=jean  

и прописал роли  kubectl create -f role.yaml  
![Screenshot 2022-06-09 001158](https://user-images.githubusercontent.com/87374285/172638582-315e6ab1-7b73-4094-a8c5-1ea0c7da4d81.jpg)   

привязал kubectl create -f role_binding.yaml  
![Screenshot 2022-06-09 001810](https://user-images.githubusercontent.com/87374285/172639857-f92d6182-1109-4839-9865-b2af3b880dcb.jpg)  

получил итого конфиг  
![Screenshot 2022-06-09 002127](https://user-images.githubusercontent.com/87374285/172640643-d5532148-6e36-42f8-9c1d-a71cd59dc83b.jpg)  

проверил  
![Screenshot 2022-06-09 002255](https://user-images.githubusercontent.com/87374285/172641014-a8f8a9de-2942-4839-9680-b63ff71b9264.jpg)  

#### Задание 3: Изменение количества реплик  
Поработав с приложением, вы получили запрос на увеличение количества реплик приложения для нагрузки. Необходимо изменить запущенный deployment, увеличив количество реплик до 5. Посмотрите статус запущенных подов после увеличения реплик.  

![Screenshot 2022-06-09 002436](https://user-images.githubusercontent.com/87374285/172641698-78fa512b-2318-4f9e-a7e6-4ba16d6d62ae.jpg)  

