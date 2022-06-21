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
    app: hello-world
  name: hello-world
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
        - image: k8s.gcr.io/echoserver:1.4
          imagePullPolicy: IfNotPresent
          name: hello-world
      terminationGracePeriodSeconds: 30

---
apiVersion: v1
kind: Service
metadata:
  name: hello-world
  namespace: default
spec:
  ports:
    - name: hello-world
      port: 8080
  selector:
    app: hello-world
iv_art@Pappa:~/kubespray$
```  
  
![Screenshot 2022-06-21 140858](https://user-images.githubusercontent.com/87374285/174714323-e0ade5e0-7dec-47ba-931e-e02accb6dd27.jpg)  

Сервис отвечает  
```
iv_art@Pappa:~$ kubectl get services
NAME          TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
hello-world   ClusterIP   10.233.25.32   <none>        8080/TCP   11m
kubernetes    ClusterIP   10.233.0.1     <none>        443/TCP    21h

iv_art@Pappa:~$ kubectl exec hello-world-7c8458888d-btbh2 -- curl -s -m 1 hello-world:8080
CLIENT VALUES:
client_address=10.130.0.15
command=GET
real path=/
query=nil
request_version=1.1
request_uri=http://hello-world:8080/

SERVER VALUES:
server_version=nginx: 1.10.0 - lua: 10001

HEADERS RECEIVED:
accept=*/*
host=hello-world:8080
user-agent=curl/7.47.0
BODY:
-no body in request-
```  

Создаю простейшую политику на "запрет всего" и проверяю  
![Screenshot 2022-06-21 143105](https://user-images.githubusercontent.com/87374285/174716542-48bdf886-c3da-4f2b-96ea-7d06347ff63d.jpg)  

Создаем второй под - frontend из лекции и повторно проверяем на ответ  
```
iv_art@Pappa:~$ kubectl apply -f frontend.yaml
deployment.apps/frontend created
service/frontend created
iv_art@Pappa:~$ kubectl get po
NAME                           READY   STATUS              RESTARTS   AGE
frontend-c74c5646c-nchkf       0/1     ContainerCreating   0          3s
hello-world-7c8458888d-btbh2   1/1     Running             0          32m
iv_art@Pappa:~$ kubectl exec frontend-c74c5646c-nchkf -- curl -s -m 1 hello-world-7c8458888d-btbh2 hello-world:8080
command terminated with exit code 28
iv_art@Pappa:~$
```  

Создаю под него политику:
![Screenshot 2022-06-21 144752](https://user-images.githubusercontent.com/87374285/174718338-2b2e8e9a-c4ce-436f-91cb-aa077d22ce80.jpg)  

Проверяю
```
iv_art@Pappa:~$ kubectl apply -f my_policy.yaml
networkpolicy.networking.k8s.io/network-policy-front created
iv_art@Pappa:~$ kubectl get networkpolicies
NAME                   POD-SELECTOR      AGE
default-deny           <none>            20m
network-policy-front   app=hello-world   11s
```  

Отклик производится при обращении от frontend, в противном случае - нет  
![Screenshot 2022-06-21 151740](https://user-images.githubusercontent.com/87374285/174721644-b1ce940e-47c1-485f-be91-584da4a787d2.jpg)  

#### Задание 2: изучить, что запущено по умолчанию  
Самый простой способ — проверить командой calicoctl get . Для проверки стоит получить список нод, ipPool и profile. Требования:  
- установить утилиту calicoctl;  
- получить 3 вышеописанных типа в консоли.  

Calico установил, как плагин к kubectl  
```
iv_art@Pappa:~/kubespray$ kubectl-calico get nodes -o wide
NAME    ASN       IPV4             IPV6
cp1     (64512)   10.130.0.22/24
node1   (64512)   10.130.0.7/24
node2   (64512)   10.130.0.15/24

iv_art@Pappa:~/kubespray$ kubectl-calico get ippool -o wide
NAME           CIDR             NAT    IPIPMODE   VXLANMODE   DISABLED   DISABLEBGPEXPORT   SELECTOR
default-pool   10.233.64.0/18   true   Never      Always      false      false              all()

iv_art@Pappa:~/kubespray$ kubectl-calico get profile
NAME
projectcalico-default-allow
kns.default
kns.kube-node-lease
kns.kube-public
kns.kube-system
ksa.default.default
ksa.kube-node-lease.default
ksa.kube-public.default
ksa.kube-system.attachdetach-controller
ksa.kube-system.bootstrap-signer
ksa.kube-system.calico-node
ksa.kube-system.certificate-controller
ksa.kube-system.clusterrole-aggregation-controller
ksa.kube-system.coredns
ksa.kube-system.cronjob-controller
ksa.kube-system.daemon-set-controller
ksa.kube-system.default
ksa.kube-system.deployment-controller
ksa.kube-system.disruption-controller
ksa.kube-system.dns-autoscaler
ksa.kube-system.endpoint-controller
ksa.kube-system.endpointslice-controller
ksa.kube-system.endpointslicemirroring-controller
ksa.kube-system.ephemeral-volume-controller
ksa.kube-system.expand-controller
ksa.kube-system.flannel
ksa.kube-system.generic-garbage-collector
ksa.kube-system.horizontal-pod-autoscaler
ksa.kube-system.job-controller
ksa.kube-system.kube-proxy
ksa.kube-system.namespace-controller
ksa.kube-system.node-controller
ksa.kube-system.nodelocaldns
ksa.kube-system.persistent-volume-binder
ksa.kube-system.pod-garbage-collector
ksa.kube-system.pv-protection-controller
ksa.kube-system.pvc-protection-controller
ksa.kube-system.replicaset-controller
ksa.kube-system.replication-controller
ksa.kube-system.resourcequota-controller
ksa.kube-system.root-ca-cert-publisher
ksa.kube-system.service-account-controller
ksa.kube-system.service-controller
ksa.kube-system.statefulset-controller
ksa.kube-system.token-cleaner
ksa.kube-system.ttl-after-finished-controller
ksa.kube-system.ttl-controller
```









