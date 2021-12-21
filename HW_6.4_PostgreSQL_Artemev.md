#### 1. 
docker pull postgres:13  
docker run --rm --name psg -e POSTGRES_PASSWORD=postgres -ti -p 5432:5432 -v vol1:/var/lib/postgresql/data -v vol2:/var/lib/postgresql postgres:13  
* вывода списка БД  
postgres-# \l  
  
* подключения к БД - \c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}  
postgres-# \c postgres  

* вывод списка таблиц  
postgres-# \dt   
* вывод описания содержимого таблиц  
postgres-# \d[S+] NAME  

* выход из psql  
postgres-# \q  

#### 2. 
postgres=# CREATE DATABASE test_database;  
iv_art@Pappa-note:/mnt/c/Users/ан/virt-homeworks-virt-11/06-db-04-postgresql/test_data$ docker cp test_dump.sql psg:/home  
psql -U postgres -f test_dump.sql test_database    
```
test_database=# ANALYZE VERBOSE public.orders;  
INFO:  analyzing "public.orders"  
INFO:  "orders": scanned 1 of 1 pages, containing 8 live rows and 0 dead rows; 8 rows in sample, 8 estimated total rows  
ANALYZE  
test_database=# select avg_width from pg_stats where tablename='orders';  
 avg_width  
-----------  
         4  
        16  
         4  
(3 rows)  
```

#### 3.  
Для проведения шардирования необходимо создать новые таблицы и заполнить данными:  
test_database=# alter table orders rename to orders_old;  
ALTER TABLE  
test_database=# create table orders (id integer, title varchar(80), price integer) partition by range(price);  
CREATE TABLE  
test_database=# create table orders_2 partition of orders for values from (0) to (499);  
CREATE TABLE  
test_database=# create table orders_1 partition of orders for values from (499) to (999999999);  
CREATE TABLE  
test_database=# insert into orders (id, title, price) select * from orders_old;  
INSERT 0 8  
test_database=#  
При проектировании базы можно было предусмотреть партицирование, через наследование к примеру.  
create table orders1 (check price>499) inherits (orders);  
create table orders2 (check price<=499) inherits (orders);  

#### 4. 
Создание копии 
pg_dump -U postgres -d test_database >test_database_copy.sql  
Для уникальности можно добавить индекс.  
CREATE UNIQUE INDEX ON orders ((lower(title)));  
