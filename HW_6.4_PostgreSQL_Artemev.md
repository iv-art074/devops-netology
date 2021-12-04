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
