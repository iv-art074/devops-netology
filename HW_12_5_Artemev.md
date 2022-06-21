#### Задание 1: установить в кластер CNI плагин Calico
Для проверки других сетевых решений стоит поставить отличный от Flannel плагин — например, Calico. Требования:  
- установка производится через ansible/kubespray;  
- после применения следует настроить политику доступа к hello-world извне. Инструкции kubernetes.io, Calico  

Использую кластер, развернутый в 12/4  
Устанавливаем Hello-world
```
iv_art@Pappa:~/kubespray$ cat hello.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: hello-node
  name: hello-node
  namespace: kube-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-node
  template:
    metadata:
      labels:
        app: hello-node
    spec:
      containers:
        - image: k8s.gcr.io/echoserver:1.4
          imagePullPolicy: IfNotPresent
          name: hello-node
      terminationGracePeriodSeconds: 30

---
apiVersion: v1
kind: Service
metadata:
  name: hello-node
  namespace: default
spec:
  ports:
    - name: hello-node
      port: 8080
  selector:
    app: hello-nodeiv_art@Pappa:~/kubespray$
    ```
    ![Screenshot 2022-06-21 133206](https://user-images.githubusercontent.com/87374285/174710535-2de66d5a-ff83-4011-9a7e-331d2ca030d5.jpg)  
    
