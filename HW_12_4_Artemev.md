#### Задание 1: Подготовить инвентарь kubespray  
Новые тестовые кластеры требуют типичных простых настроек. Нужно подготовить инвентарь и проверить его работу. Требования к инвентарю:  

подготовка работы кластера из 5 нод: 1 мастер и 4 рабочие ноды;  
в качестве CRI — containerd;  
запуск etcd производить на мастере.  

Машины созданы  
![Screenshot 2022-06-20 154217](https://user-images.githubusercontent.com/87374285/174532785-0c47b31a-454b-4a2f-8196-6dc60493f101.jpg)  

![Screenshot 2022-06-20 154338](https://user-images.githubusercontent.com/87374285/174532937-348884c1-8bef-4b9a-8408-96aa3ced66f7.jpg)  

Кластер поднялся  
```
$ ansible-playbook -i inventory/mycluster/hosts.yaml --become --become-user=root cluster.yaml  
```  
![Screenshot 2022-06-20 165121](https://user-images.githubusercontent.com/87374285/174542093-59b0c57d-fcb1-4549-8c8e-b35b5bf73472.jpg)  

![Screenshot 2022-06-20 165335](https://user-images.githubusercontent.com/87374285/174542404-8b2f5bae-76c2-4476-8868-751b7a38f22f.jpg)  

при попытке подключения с локальной машины получил ошибку ssl.  
добавил supplementary в k8s-cluster.yml  
supplementary_addresses_in_ssl_keys: [51.250.40.3]  

Перезапустил playbook, все ок  
![Screenshot 2022-06-20 204057](https://user-images.githubusercontent.com/87374285/174585038-8db6380f-4770-4236-a284-789f18ca86a3.jpg)  






