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

#### Задача 2 (*): Рассмотрите пример 14.5/example-network-policy.yml  
Создайте два модуля. Для первого модуля разрешите доступ к внешнему миру и ко второму контейнеру. Для второго модуля разрешите связь только с первым контейнером. Проверьте корректность настроек.  
Создаем модуль frontend без ограничений и модуль db c траффиком только на frontend  
   
```
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.5# cat deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openty2
  namespace: default
  labels:
     role: frontend
spec:
  selector:
    matchLabels:
      role: frontend
  template:
    metadata:
      labels:
         role: frontend
    spec:
      containers:
        - name: frontend
          image: praqma/network-multitool
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.5# cat deploy_db.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db
  namespace: default
  labels:
     role: db
spec:
  selector:
    matchLabels:
      role: db
  template:
    metadata:
      labels:
         role: db
    spec:
      containers:
        - name: db
          image: praqma/network-multitool

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.5# kubectl apply -f deploy.yaml
deployment.apps/openty2 created
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.5# kubectl apply -f deploy_db.yaml
deployment.apps/db created
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.5# kubectl get po -o wide
NAME                       READY   STATUS    RESTARTS   AGE     IP             NODE        NOMINATED NODE   READINESS GATES
db-6f4dc87f9b-v92ch        1/1     Running   0          2m19s   10.244.214.4   pappa-wsl   <none>           <none>
openty2-598c96bb56-2nrqm   1/1     Running   0          2m28s   10.244.214.3   pappa-wsl   <none>           <none>

# применяем политику

root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.5# cat example-network-policy.yml
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
  egress:
  - to:
    - podSelector:
        matchLabels:
          role: frontend
root@Pappa-wsl:/home/iv_art/clokub/clokub-homeworks/14.5#kubectl apply -f example-network-policy.yml
networkpolicy.networking.k8s.io/test-network-policy created
```  

входим в под db  
пингаем google - пинг не идет  
пингаем frontend - трафик идет
![image](https://user-images.githubusercontent.com/87374285/184879219-de5c0020-5791-47bd-8ccd-1a126b19ff2a.png)

проверяем под frontend  
![image](https://user-images.githubusercontent.com/87374285/184880235-c7e74835-f8ce-4870-81e7-34463d2c77ad.png)

все ок  
