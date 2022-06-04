### Задача 1. Установил minikube
 
![Screenshot 2022-06-04 143541](https://user-images.githubusercontent.com/87374285/172003340-1abe2cff-9893-4414-85d5-4f9ce2350625.jpg)  
 
![Screenshot 2022-06-04 161723](https://user-images.githubusercontent.com/87374285/172003334-217ec527-3f6b-47f8-ad00-93dcf9019737.jpg)  

### Задача 2: Запуск Hello World  
После установки Minikube требуется его проверить. Для этого подойдет стандартное приложение hello world. А для доступа к нему потребуется ingress.  
развернуть через Minikube тестовое приложение по туториалу  

![Screenshot 2022-06-04 225719](https://user-images.githubusercontent.com/87374285/172003326-d73b19dd-f39c-4cec-bd23-d5aea81c6f87.jpg)  


![Screenshot 2022-06-04 230653](https://user-images.githubusercontent.com/87374285/172003308-064d7a36-ae26-431b-97d2-c7ac4b512ddd.jpg)  

установить аддоны ingress и dashboard  
```  
root@servr:~# minikube addons list
|-----------------------------|----------|--------------|--------------------------------|
|         ADDON NAME          | PROFILE  |    STATUS    |           MAINTAINER           |
|-----------------------------|----------|--------------|--------------------------------|
| ambassador                  | minikube | disabled     | third-party (ambassador)       |
| auto-pause                  | minikube | disabled     | google                         |
| csi-hostpath-driver         | minikube | disabled     | kubernetes                     |
| dashboard                   | minikube | enabled ✅   | kubernetes                     |
| default-storageclass        | minikube | enabled ✅   | kubernetes                     |
| efk                         | minikube | disabled     | third-party (elastic)          |
| freshpod                    | minikube | disabled     | google                         |
| gcp-auth                    | minikube | disabled     | google                         |
| gvisor                      | minikube | disabled     | google                         |
| helm-tiller                 | minikube | disabled     | third-party (helm)             |
| ingress                     | minikube | enabled ✅   | unknown (third-party)          |
| ingress-dns                 | minikube | disabled     | google                         |
| istio                       | minikube | disabled     | third-party (istio)            |
| istio-provisioner           | minikube | disabled     | third-party (istio)            |
| kong                        | minikube | disabled     | third-party (Kong HQ)          |
| kubevirt                    | minikube | disabled     | third-party (kubevirt)         |
| logviewer                   | minikube | disabled     | unknown (third-party)          |
| metallb                     | minikube | disabled     | third-party (metallb)          |
| metrics-server              | minikube | disabled     | kubernetes                     |
| nvidia-driver-installer     | minikube | disabled     | google                         |
| nvidia-gpu-device-plugin    | minikube | disabled     | third-party (nvidia)           |
| olm                         | minikube | disabled     | third-party (operator          |
|                             |          |              | framework)                     |
| pod-security-policy         | minikube | disabled     | unknown (third-party)          |
| portainer                   | minikube | disabled     | portainer.io                   |
| registry                    | minikube | disabled     | google                         |
| registry-aliases            | minikube | disabled     | unknown (third-party)          |
| registry-creds              | minikube | disabled     | third-party (upmc enterprises) |
| storage-provisioner         | minikube | enabled ✅   | google                         |
| storage-provisioner-gluster | minikube | disabled     | unknown (third-party)          |
| volumesnapshots             | minikube | disabled     | kubernetes                     |
|-----------------------------|----------|--------------|--------------------------------|
root@servr:~#
```  
### Задача 3: Установить kubectl  
Подготовить рабочую машину для управления корпоративным кластером. Установить клиентское приложение kubectl.  
подключиться к minikube, проверить работу приложения из задания 2, запустив port-forward до кластера  

скопировал содержимое admin.conf с сервера в локальный файл .kube/config  
Kubectl работает. Видно - сервис функционирует.  

```  
root@Pappa:~/.minikube/config# kubectl get nodes
NAME    STATUS   ROLES                  AGE   VERSION
servr   Ready    control-plane,master   98m   v1.23.3
root@Pappa:~/.minikube/config# kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
hello-node   1/1     1            1           76m
root@Pappa:~/.minikube/config# kubectl get pods
NAME                          READY   STATUS    RESTARTS       AGE
hello-node-6b89d599b9-hmsv8   1/1     Running   1 (9m7s ago)   76m
root@Pappa:~/.minikube/config# kubectl get services
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
hello-node   LoadBalancer   10.100.49.24   <pending>     8080:30872/TCP   76m
kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          101m
root@Pappa:~/.minikube/config#
```  
