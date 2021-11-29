###### 1. Поднимите инстанс PostgreSQL (версию 12) c 2 volume
docker pull postgres:12  
iv_art@Pappa-note:~$ docker volume create vol2  
vol2  
iv_art@Pappa-note:~$ docker volume create vol1  
vol1  
iv_art@Pappa-note:~$ docker run --rm --name psg -e POSTGRES_PASSWORD=postgres -ti -p 5432:5432 -v vol1:/var/lib/postgresql/data -v vol2:/var/lib/postgresql postgres:12  

###### 2. В БД из предыдущего задания
*    создайте пользователя test-admin-user и БД test_db  
*    в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)  
*    предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db  
*    создайте пользователя test-simple-user  
*    предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db  

   test_db=# CREATE ROLE "test-admin-user" SUPERUSER NOINHERIT LOGIN;  
   test_db=# CREATE ROLE "test-simple-user" NOSUPERUSER NOINHERIT LOGIN;   
   
   ![Screenshot 2021-11-29 221750](https://user-images.githubusercontent.com/87374285/143866880-bbe5570c-a81a-4b82-affb-15bf0d6b334a.png)  
     ![Screenshot 2021-11-29 224028](https://user-images.githubusercontent.com/87374285/143869833-363258f7-345a-4fcf-9da4-c96236d32e6f.png)  
 ![Screenshot 2021-11-29 224959](https://user-images.githubusercontent.com/87374285/143871200-558675f6-3fe2-48be-b4e5-7a53f000b08d.png)  

###### 3. 
* Используя SQL синтаксис - наполните таблицы  
![Screenshot 2021-11-29 225418](https://user-images.githubusercontent.com/87374285/143871851-27e167d6-10bb-4125-b8fb-aa169c589102.png)  
 
* вычислите количество записей для каждой таблицы  
![Screenshot 2021-11-29 225437](https://user-images.githubusercontent.com/87374285/143871877-29ad8a64-1016-46bc-a2aa-a1894f2960f6.png)  
  
###### 4. Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.  
![Screenshot 2021-11-29 225702](https://user-images.githubusercontent.com/87374285/143872155-179574a5-f388-4188-9a55-90d18df272e4.png)  

###### 5. Запрос с директивой EXPLAIN  
![Screenshot 2021-11-29 225848](https://user-images.githubusercontent.com/87374285/143872398-fe5f7a06-289e-4cf0-8fbd-bf4d068d3c02.png)  
  
Запрос содержит предложения WHERE, которое применено, как «фильтр» к узлу плана Seq Scan (Последовательное сканирование). Из 5 строк 2 отброшено и результат имеет минимальную стоимость и время выполнения.  

###### 6. Создание и восстановление бэкапа
iv_art@Pappa-note:~$ docker exec -t psg pg_dump -U postgres test_db -f /var/lib/postgresql/data/dump_test.sql
iv_art@Pappa-note:~$ docker stop psg
iv_art@Pappa-note:~# docker run --rm --name psg1 -e POSTGRES_PASSWORD=postgres -ti -p 9100:9100 -v vol1:/var/lib/postgresql/data -v vol2:/var/lib/postgresql postgres:12
iv_art@Pappa-note:~$ docker exec -i psg1 psql -U postgres -d test_db -f /var/lib/postgresql/data/dump_test.sql  
![Screenshot 2021-11-30 000348](https://user-images.githubusercontent.com/87374285/143881860-9bdbd740-7e96-4057-8174-6efb491bf47e.png)  








