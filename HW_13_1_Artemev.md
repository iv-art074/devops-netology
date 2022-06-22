#### Задание 1: подготовить тестовый конфиг для запуска приложения  
Для начала следует подготовить запуск приложения в stage окружении с простыми настройками. Требования:  

- под содержит в себе 2 контейнера — фронтенд, бекенд;  
- регулируется с помощью deployment фронтенд и бекенд;  
- база данных — через statefulset.  

манифест front+back  
```
iv_art@Pappa:~/kubespray/app$ cat fr-b.yaml
# Config Stage env
apiVersion: apps/v1
kind: Deployment
metadata:
  name: front-back-pod
  labels:
    app: front-back-app
spec:
  selector:
    matchLabels:
      app: front-back-app
  template:
    metadata:
      labels:
        app: front-back-app
    spec:
    # Config Containers
      containers:
      - name: frontend
        image: nginx:1.14.2
        ports:
        - containerPort: 80
      - name: backend
        image: debian
        command: ["sleep", "600"]
---
# Config Service
apiVersion: v1
kind: Service
metadata:
  name: front-back-service
  labels:
    app: front-back-app
spec:
  type: NodePort
  ports:
  - port: 80
    nodePort: 30080
  selector:
    app: front-back-appiv_art@Pappa:~/kubespray/app$
```  
создаем БД  
```
iv_art@Pappa:~/kubespray/app$ kubectl apply -f db.yaml
statefulset.apps/postgres created
service/postgres created
```  
Манифест
```
iv_art@Pappa:~/kubespray/app$ cat db.yaml
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  labels:
    app: postgres
  namespace: default
spec:
  serviceName: postgres
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:13-alpine
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 5432
        volumeMounts:
          - name: db-volume
            mountPath: "/var/lib/postgresql/data"
        env:
          - name: POSTGRES_PASSWORD
            value: postgres
          - name: POSTGRES_USER
            value: postgres
          - name: POSTGRES_DB
            value: news
      volumes:
        - name: db-volume
          emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: postgres
  namespace: default
spec:
  selector:
    app: postgres
  ports:
    - name: postgres
      protocol: TCP
      port: 5432
      targetPort: 5432
  type: ClusterIP
```  
Результат  
```
iv_art@Pappa:~/kubespray/app$ kubectl get po
NAME                              READY   STATUS              RESTARTS      AGE
front-back-pod-759947cb5b-jk95n   2/2     Running             1 (20s ago)   10m
postgres-0                        0/1     ContainerCreating   0             13s
iv_art@Pappa:~/kubespray/app$ kubectl get sts
NAME       READY   AGE
postgres   1/1     23s
iv_art@Pappa:~/kubespray/app$ kubectl get svc
NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
front-back-service   NodePort    10.233.3.14    <none>        80:30080/TCP   11m
kubernetes           ClusterIP   10.233.0.1     <none>        443/TCP        45h
postgres             ClusterIP   10.233.10.24   <none>        5432/TCP       49s
iv_art@Pappa:~/kubespray/app$ kubectl get deploy
NAME             READY   UP-TO-DATE   AVAILABLE   AGE
front-back-pod   1/1     1            1           11m
iv_art@Pappa:~/kubespray/app$ kubectl describe deploy front-back-pod
Name:                   front-back-pod
Namespace:              default
CreationTimestamp:      Wed, 22 Jun 2022 14:10:32 +1000
Labels:                 app=front-back-app
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=front-back-app
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=front-back-app
  Containers:
   frontend:
    Image:        nginx:1.14.2
    Port:         80/TCP
    Host Port:    0/TCP
    Environment:  <none>
    Mounts:       <none>
   backend:
    Image:      debian
    Port:       <none>
    Host Port:  <none>
    Command:
      sleep
      600
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Progressing    True    NewReplicaSetAvailable
  Available      True    MinimumReplicasAvailable
OldReplicaSets:  <none>
NewReplicaSet:   front-back-pod-759947cb5b (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  13m   deployment-controller  Scaled up replica set front-back-pod-759947cb5b to 1
iv_art@Pappa:~/kubespray/app$
```  

#### Задание 2: подготовить конфиг для production окружения  
Следующим шагом будет запуск приложения в production окружении. Требования сложнее:  

- каждый компонент (база, бекенд, фронтенд) запускаются в своем поде, регулируются отдельными deployment’ами;  
- для связи используются service (у каждого компонента свой);  
- в окружении фронта прописан адрес сервиса бекенда;  
- в окружении бекенда прописан адрес сервиса базы данных.  

Чистим для наглядности  
```  
iv_art@Pappa:~/kubespray$ kubectl delete -f ./app
statefulset.apps "postgres" deleted
service "postgres" deleted
deployment.apps "front-back-pod" deleted
service "front-back-service" deleted
iv_art@Pappa:~/kubespray$ kubectl get deploy
No resources found in default namespace.
iv_art@Pappa:~/kubespray$ kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.233.0.1   <none>        443/TCP   46h
iv_art@Pappa:~/kubespray$ kubectl get sts
No resources found in default namespace.
iv_art@Pappa:~/kubespray$
```  
Конфиги front&back  
```
iv_art@Pappa:~/kubespray/app/prod$ cat back-prod.yaml
# Config Stage env
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-prod
  labels:
    app: backend-prod-app
spec:
  selector:
    matchLabels:
      app: backend-prod-app
  template:
    metadata:
      labels:
        app: backend-prod-app
    spec:
    # Config Containers
      containers:
      - name: backend
        image: debian
        command: ["sleep", "600"]
        env:
          - name: DATABASE_URL
            value: postgres://postgres:postgres@postgres:5432/news # адрес сервиса БД
---
# Config Service
apiVersion: v1
kind: Service
metadata:
  name: backend-prod-svc
  namespace: default
spec:
  selector:
    app: backend-prod-app
  ports:
    - name: backend-prod
      protocol: TCP
      port: 9000
      targetPort: 9000


iv_art@Pappa:~/kubespray/app/prod$ cat front-prod.yaml
# Front pod 4 prod
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-prod
  labels:
    app: frontend-prod
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend-prod
  template:
    metadata:
      labels:
        app: frontend-prod
    spec:
      containers:
      - name: client
        image: nginx:1.19
        ports:
        - containerPort: 80
        env:                                  #Параметры backend
          - name: BASE_URL
            value: backend-prod:9000

---
apiVersion: v1
kind: Service
metadata:
  name: frontend-prod
  namespace: default
spec:
  selector:
    app: frontend-prod
  ports:
    - name: frontend-prod
      protocol: TCP
      port: 8000
      targetPort: 80
  type: ClusterIP
```  
Запуск  

```  
iv_art@Pappa:~/kubespray/app/prod$ kubectl apply -f .
deployment.apps/backend-prod created
service/backend-prod-svc created
statefulset.apps/postgres created
service/postgres created
deployment.apps/frontend-prod created
service/frontend-prod-svc created
```  

Проверяем  
![Screenshot 2022-06-22 152500](https://user-images.githubusercontent.com/87374285/174951064-e94674b4-8f5d-4df2-9f94-89a52def4d47.jpg)

дополнительно для проверки запускаю тестовый под  
```   
iv_art@Pappa:~/kubespray$ kubectl apply -f hello.yaml
deployment.apps/hello-world created
service/hello-world created
```  
тестируем отклик фронта  
![image](https://user-images.githubusercontent.com/87374285/174953413-53ddc328-8040-4423-9ed1-75135e3e9afe.png)





    
    
