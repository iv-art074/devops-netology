##### 1.
 ```
 iv_art@Pappa-note:~$ docker pull mysql:8.0  
 iv_art@Pappa-note:~$ docker volume create vol  
 iv_art@Pappa-note:~$ docker run --rm --name mysql -ti -e MYSQL_ROOT_PASSWORD=msql -p 3306:3306 -v vol:/etc/mysql/ mysql:8.0  
 #  mysqldump -uroot -pmsql -v --all-databases > etc/mysql/dump.sql  
 iv_art@Pappa-note:~$ mysql -uroot -pmsql < /etc/test_dump.sql  
 ```  
 ![Screenshot 2021-12-01 004013](https://user-images.githubusercontent.com/87374285/144067821-8056e8b2-95c3-4b85-a8f9-957e92c2eecd.png)  

##### 2. Создайте пользователя test в БД c паролем test-pass
mysql> CREATE USER 'test'@'localhost' IDENTIFIED BY 'test-pass';
Query OK, 0 rows affected (2.26 sec)  
![Screenshot 2021-12-01 205809](https://user-images.githubusercontent.com/87374285/144222542-9ada9a27-8c66-4d4a-b820-67696f983e40.png)  

##### 3.
Смотрим движок
```
mysql> SHOW CREATE TABLE orders;
| orders | CREATE TABLE `orders` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(80) NOT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
```
меняем движок и смотрим время запросов
![Screenshot 2021-12-01 212014](https://user-images.githubusercontent.com/87374285/144225651-6916352e-b1f7-4caa-8e1b-f9c628f9ffd0.png)  

##### 4. 
![Screenshot 2021-12-01 220555](https://user-images.githubusercontent.com/87374285/144231719-72cd8aa1-a182-486e-8399-97de96800ca5.png)  
