##### 1.
 ```
 iv_art@Pappa-note:~$ docker pull mysql:8.0  
 iv_art@Pappa-note:~$ docker volume create vol  
 iv_art@Pappa-note:~$ docker run --rm --name mysql -ti -e MYSQL_ROOT_PASSWORD=msql -p 3306:3306 -v vol:/etc/mysql/ mysql:8.0  
 #  mysqldump -uroot -pmsql -v --all-databases > etc/mysql/dump.sql  
 iv_art@Pappa-note:~$ mysql -uroot -pmsql < /etc/test_dump.sql  
 ```  
 ![Screenshot 2021-12-01 004013](https://user-images.githubusercontent.com/87374285/144067821-8056e8b2-95c3-4b85-a8f9-957e92c2eecd.png)  
