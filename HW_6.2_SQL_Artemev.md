###### 1. Поднимите инстанс PostgreSQL (версию 12) c 2 volume
docker pull postgres:12  
iv_art@Pappa-note:~$ docker volume create vol2  
vol2  
iv_art@Pappa-note:~$ docker volume create vol1  
vol1  
iv_art@Pappa-note:~$ docker run --rm --name psg -e POSTGRES_PASSWORD=postgres -ti -p 9100:9100 -v vol1:/var/lib/postgresql/data -v vol2:/var/lib/postgresql postgres:12  

###### 2. В БД из предыдущего задания
*    создайте пользователя test-admin-user и БД test_db  
*    в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)  
*    предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db  
*    создайте пользователя test-simple-user  
*    предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db  

   test_db=# CREATE ROLE "test-admin-user" SUPERUSER NOINHERIT LOGIN;  
   test_db=# CREATE ROLE "test-simple-user" NOSUPERUSER NOINHERIT LOGIN;   
   
   ![Screenshot 2021-11-29 221750](https://user-images.githubusercontent.com/87374285/143866880-bbe5570c-a81a-4b82-affb-15bf0d6b334a.png)  
      
   ![Screenshot 2021-11-28 221804](https://user-images.githubusercontent.com/87374285/143767443-ff4901b3-adc6-429a-97e3-719df1492487.png)  
![Screenshot 2021-11-28 221850](https://user-images.githubusercontent.com/87374285/143767504-2f8b25bc-c55a-4c9e-9499-29b80c1f779c.png)  
![Screenshot 2021-11-28 223006](https://user-images.githubusercontent.com/87374285/143767975-8707c03a-4c65-4217-8549-a17a7cf50526.png)  
![Screenshot 2021-11-28 223412](https://user-images.githubusercontent.com/87374285/143767979-9f14eb3f-ceee-4904-9cb3-775b3320ca92.png)  

###### 3. 
* Используя SQL синтаксис - наполните таблицы
![Screenshot 2021-11-29 205103](https://user-images.githubusercontent.com/87374285/143855455-ba636832-47f2-445c-a66d-e5be4ba76d65.png) 
* вычислите количество записей для каждой таблицы  
![Screenshot 2021-11-29 205140](https://user-images.githubusercontent.com/87374285/143855487-9da63bee-de3f-4af4-8d68-e3c1d68c3f4e.png)  

###### 4. Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.  
![Screenshot 2021-11-29 212416](https://user-images.githubusercontent.com/87374285/143859702-15df9039-9af9-465e-a502-f00924eda94f.png)  

###### 5. Запрос с директивой EXPLAIN  
![Screenshot 2021-11-29 213508](https://user-images.githubusercontent.com/87374285/143861522-40d901aa-8b73-42e0-8a07-13daddd5a82b.png)  
Запрос содержит предложения WHERE, которое применено, как «фильтр» к узлу плана Seq Scan (Последовательное сканирование). Из 5 строк 2 отброшено и результат имеет минимальную стоимость и время выполнения.  

###### 6. 








