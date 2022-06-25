#### Задание 1: проверить работоспособность каждого компонента  
Для проверки работы можно использовать 2 способа: port-forward и exec. Используя оба способа, проверьте каждый компонент:  
- сделайте запросы к бекенду;  
- сделайте запросы к фронту;  
- подключитесь к базе данных.  

Опять поднял кластер и запустил фронт+бэк+бд  
![image](https://user-images.githubusercontent.com/87374285/175774532-bd4e9948-e39f-4418-819e-3339812d9c67.png)  

Проверяем frontend:  
```  
iv_art@Pappa:~/kubespray/app/prod$ kubectl port-forward service/frontend-prod 8000:8000
Forwarding from 127.0.0.1:8000 -> 80
Forwarding from [::1]:8000 -> 80  
```  
![image](https://user-images.githubusercontent.com/87374285/175773070-e3054256-885a-4350-9f51-00358d14e55c.png)  

![image](https://user-images.githubusercontent.com/87374285/175773296-cf0add4a-f7da-4145-b646-d82f9aaadeb4.png)  

Проверяем backend:  
```  
iv_art@Pappa:~/kubespray/app/prod$ kubectl port-forward service/backend-probe :80
Forwarding from 127.0.0.1:38955 -> 80
Forwarding from [::1]:38955 -> 80
Handling connection for 38955
```  
![image](https://user-images.githubusercontent.com/87374285/175774570-3170fdee-9a64-49d1-aed6-81912800c329.png)  

![image](https://user-images.githubusercontent.com/87374285/175774623-3df9d512-51d2-44dc-9930-122b4b809f9f.png)  

Проверяем БД:  
![image](https://user-images.githubusercontent.com/87374285/175774713-9b743167-e7b7-40a3-993e-55e6de7e0f19.png)  

#### Задание 2: ручное масштабирование  
При работе с приложением иногда может потребоваться вручную добавить пару копий.  
Используя команду kubectl scale, попробуйте увеличить количество бекенда и фронта до 3.  
Проверьте, на каких нодах оказались копии после каждого действия (kubectl describe, kubectl get pods -o wide).  
После уменьшите количество копий до 1.

![image](https://user-images.githubusercontent.com/87374285/175774942-8a538ba5-a24b-4b62-b534-0102d439e334.png)  

Увеличиваем и проверяем  
Но, к сожалению, рабочая нода у меня 1 из экономиии баланса YC  
![image](https://user-images.githubusercontent.com/87374285/175775003-920f459d-1f90-435d-843b-faec9f3be67a.png)  

Уменьшаем и проверяем  
![image](https://user-images.githubusercontent.com/87374285/175775024-f9775ef2-8fd2-4b47-bb96-6c6cfe576feb.png)  


