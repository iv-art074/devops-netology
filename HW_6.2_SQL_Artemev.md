###### 1. Поднимите инстанс PostgreSQL (версию 12) c 2 volume
docker pull postgres:12  
iv_art@Pappa-note:~$ docker volume create vol2  
vol2  
iv_art@Pappa-note:~$ docker volume create vol1  
vol1  
iv_art@Pappa-note:~$ docker run --rm --name psg -e POSTGRES_PASSWORD=postgres -ti -p 9100:9100 -v vol1:/var/lib/postgresql/data -v vol2:/var/lib/postgresql postgres:12  

###### 2. 
*    создайте пользователя test-admin-user и БД test_db  
*    в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)  
*    предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db  
*    создайте пользователя test-simple-user  
*    предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db  

   postgres=# CREATE ROLE "test-admin-user" SUPERUSER NOINHERIT LOGIN;  
   postgres=# CREATE ROLE "test-simple-user" NOSUPERUSER NOINHERIT LOGIN;   
   
   ![Screenshot 2021-11-28 220611](https://user-images.githubusercontent.com/87374285/143767522-2679ed37-7ef1-4b88-b6bc-2e07c8292add.png)  

   
   ![Screenshot 2021-11-28 221804](https://user-images.githubusercontent.com/87374285/143767443-ff4901b3-adc6-429a-97e3-719df1492487.png)  
![Screenshot 2021-11-28 221850](https://user-images.githubusercontent.com/87374285/143767504-2f8b25bc-c55a-4c9e-9499-29b80c1f779c.png)  
![Screenshot 2021-11-28 223006](https://user-images.githubusercontent.com/87374285/143767975-8707c03a-4c65-4217-8549-a17a7cf50526.png)  
![Screenshot 2021-11-28 223412](https://user-images.githubusercontent.com/87374285/143767979-9f14eb3f-ceee-4904-9cb3-775b3320ca92.png)  



