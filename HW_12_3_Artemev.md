#### Задание 1: Описать требования к кластеру
Сначала проекту необходимо определить требуемые ресурсы.  
Известно, что проекту нужны база данных, система кеширования, а само приложение состоит из бекенда и фронтенда. Опишите, какие ресурсы нужны, если известно:  

- База данных должна быть отказоустойчивой. Потребляет 4 ГБ ОЗУ в работе, 1 ядро. 3 копии.  
- Кэш должен быть отказоустойчивый. Потребляет 4 ГБ ОЗУ в работе, 1 ядро. 3 копии.  
- Фронтенд обрабатывает внешние запросы быстро, отдавая статику. Потребляет не более 50 МБ ОЗУ на каждый экземпляр, 0.2 ядра. 5 копий.  
- Бекенд потребляет 600 МБ ОЗУ и по 1 ядру на копию. 10 копий.  

|Ресурсы	    |Кол-во CPU	|RAM	|Кол-во копий	|Итого требуемых ресурсов|  
|-------------|-----------|-----|-------------|------------------------|  
|База данных	|  1	      |4 Гб	|3        	  |3 CPU и 12 Гб RAM
|Кэш          |  1	      |4 Гб	|3            |3 CPU и 12 Гб RAM
|Фронтенд     |	0.2	      |50 Мб|	5           |	1 CPU и 250 Мб RAM
|Бекенд	      |1          |600 Мб|	10        |	10 CPU и 6 Гб RAM
|Control Plane|	2         |	2 Гб|	?           |	2 CPU и 2 Гб RAM 
|Рабочая нода |	1         |	1 Гб|	?           |	1 CPU и 1 Гб RAM  

Итого требования по ресурсам: 17 CPU и 31Гб RAM
Для размещения инфраструктуры требуется минимум 4 *рабочих ноды,* и 1 *контрольная,* но с учетом требований отказоустойчивости клатера в идеале:  
- для БД - 2,  
- для кэша - 2,  
- для фронта - 2,  
- для Бэка - 3,  
- количество *контрольных нод - 3*  
 
 Всего - 17+15=32 CPU и 31+15=46 Гб RAM  









PS
-----------------------------------------
Создание кластера врчучную по лекции отработал тоже:  
```  
iv_art@Pappa:/mnt/c/Users/iv_ar/Documents/GitHub/kubernetes-for-beginners-master/99-misc$ ./create-vms.sh
done (27s)
...

iv_art@Pappa:/mnt/c/Users/iv_ar/Documents/GitHub/kubernetes-for-beginners-master/99-misc$ ./list-vms.sh
+----------------------+-------+---------------+---------+---------------+-------------+
|          ID          | NAME  |    ZONE ID    | STATUS  |  EXTERNAL IP  | INTERNAL IP |
+----------------------+-------+---------------+---------+---------------+-------------+
| ef39v7ou5n8t5k6tfm05 | cp1   | ru-central1-c | RUNNING | 51.250.43.8   | 10.130.0.33 |
| ef3b3j6bg1e9s54gj28v | node1 | ru-central1-c | RUNNING | 51.250.34.97  | 10.130.0.25 |
| ef3hkiit1hhtp8n15jfo | node2 | ru-central1-c | RUNNING | 51.250.41.177 | 10.130.0.29 |
+----------------------+-------+---------------+---------+---------------+-------------+


iv_art@Pappa:/mnt/c/Users/iv_ar/Documents/GitHub/kubernetes-for-beginners-master/99-misc$ ssh yc-user@51.250.43.8
The authenticity of host '51.250.43.8 (51.250.43.8)' can't be established.
...
yc-user@cp1:~$ logout
Connection to 51.250.43.8 closed.
iv_art@Pappa:/mnt/c/Users/iv_ar/Documents/GitHub/kubernetes-for-beginners-master/99-misc$ ssh yc-user@51.250.34.97
The authenticity of host '51.250.34.97 (51.250.34.97)' can't be established.
...
yc-user@node1:~$ logout
Connection to 51.250.34.97 closed.
iv_art@Pappa:/mnt/c/Users/iv_ar/Documents/GitHub/kubernetes-for-beginners-master/99-misc$ ssh yc-user@51.250.41.177
The authenticity of host '51.250.41.177 (51.250.41.177)' can't be established.
...
yc-user@node2:~$ logout
Connection to 51.250.41.177 closed.
iv_art@Pappa:/mnt/c/Users/iv_ar/Documents/GitHub/kubernetes-for-beginners-master/99-misc$ ssh yc-user@51.250.43.8
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-117-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Sun Jun 19 07:45:18 2022 from 92.37.143.214
yc-user@cp1:~$ sudo su
# Установка
root@cp1:/home/yc-user# {
>     sudo apt-get update
>     sudo apt-get install -y apt-transport-https ca-certificates curl
>     sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
>     echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
>
>     sudo apt-get update
>     sudo apt-get install -y kubelet kubeadm kubectl containerd
>     sudo apt-mark hold kubelet kubeadm kubectl
> }
Hit:1 http://mirror.yandex.ru/ubuntu focal InRelease
...
Processing triggers for man-db (2.9.1-1) ...
kubelet set on hold.
kubeadm set on hold.
kubectl set on hold.

root@cp1:/home/yc-user# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether d0:0d:9f:9f:1e:2d brd ff:ff:ff:ff:ff:ff
    inet 10.130.0.33/24 brd 10.130.0.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::d20d:9fff:fe9f:1e2d/64 scope link
       valid_lft forever preferred_lft forever
root@cp1:/home/yc-user#

#ошибка
root@cp1:/home/yc-user# kubeadm init \
>   --apiserver-advertise-address=10.130.0.33 \
>   --pod-network-cidr 10.244.0.0/16 \
>   --apiserver-cert-extra-sans=51.250.43.8
[init] Using Kubernetes version: v1.24.2
[preflight] Running pre-flight checks
error execution phase preflight: [preflight] Some fatal errors occurred:
        [ERROR FileContent--proc-sys-net-bridge-bridge-nf-call-iptables]: /proc/sys/net/bridge/bridge-nf-call-iptables does not exist
        [ERROR FileContent--proc-sys-net-ipv4-ip_forward]: /proc/sys/net/ipv4/ip_forward contents are not set to 1
[preflight] If you know what you are doing, you can make a check non-fatal with `--ignore-preflight-errors=...`
To see the stack trace of this error execute with --v=5 or higher
root@cp1:/home/yc-user# modprobe br_netfilter
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
ecroot@cp1:/home/yc-user# echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
root@cp1:/home/yc-user# echo "net.bridge.bridge-nf-call-iptables=1" >> /etc/sysctl.conf
root@cp1:/home/yc-user# echo "net.bridge.bridge-nf-call-arptables=1" >> /etc/sysctl.conf
root@cp1:/home/yc-user# echo "net.bridge.bridge-nf-call-ip6tables=1" >> /etc/sysctl.conf
root@cp1:/home/yc-user#
root@cp1:/home/yc-user# sysctl -p /etc/sysctl.conf
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-arptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
root@cp1:/home/yc-user# kubeadm init   --apiserver-advertise-address=10.130.0.33   --pod-network-cidr 10.244.0.0/16   --apiserver-cert-extra-sans=51.250.43.8
[init] Using Kubernetes version: v1.24.2
...

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 10.130.0.33:6443 --token ks2pip.6yz36oqz9117ahz0 \
        --discovery-token-ca-cert-hash sha256:41c2f7e65f51ff804d099bbff45da7ee606aaa07672c2daf6c6cd448b516b7f3
root@cp1:/home/yc-user# {
>     mkdir -p $HOME/.kube
>     sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
>     sudo chown $(id -u):$(id -g) $HOME/.kube/config
> }

Every 2.0s: kubectl get nodes                                                              cp1: Sun Jun 19 08:29:59 2022

NAME   STATUS   ROLES           AGE   VERSION
cp1    Ready    control-plane   24m   v1.24.2

# Рабочая нода
iv_art@Pappa:~$ ssh yc-user@51.250.34.97
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-117-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Sun Jun 19 07:46:24 2022 from 92.37.143.214
yc-user@node1:~$ sudo su
root@node1:/home/yc-user# {
>     sudo apt-get update
...
This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.

root@node1:/home/yc-user#

#доступ со своей машины настроен 
iv_art@Pappa:~/.kube$ kubectl get nodes
NAME    STATUS   ROLES           AGE   VERSION
cp1     Ready    control-plane   59m   v1.24.2
node1   Ready    <none>          19m   v1.24.2
```  

