#### 1. ------------------------
* составьте Dockerfile-манифест для elasticsearch
* соберите docker-образ и сделайте push в ваш docker.io репозиторий
* запустите контейнер из получившегося образа и выполните запрос пути / c хост-машины
Dockerfile:
```
root@Pappa:/home/iv_art# cat dockerfile
FROM centos:7
ENV PATH=/usr/lib:/usr/lib/jvm/jre-11/bin:$PATH

RUN yum install wget -y

RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.15.2-linux-x86_64.tar.gz \
    && wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.15.2-linux-x86_64.tar.gz.sha512
RUN yum install perl-Digest-SHA -y
RUN shasum -a 512 -c elasticsearch-7.15.2-linux-x86_64.tar.gz.sha512 \
    && tar -xzf elasticsearch-7.15.2-linux-x86_64.tar.gz \
    && yum upgrade -y

ADD elasticsearch.yml /elasticsearch-7.15.2/config/
ENV ES_HOME=/elasticsearch-7.15.2
RUN groupadd elasticsearch \
    && useradd -g elasticsearch elasticsearch

RUN mkdir /var/lib/logs \
    && chown elasticsearch:elasticsearch /var/lib/logs \
    && mkdir /var/lib/data \
    && chown elasticsearch:elasticsearch /var/lib/data \
    && chown -R elasticsearch:elasticsearch /elasticsearch-7.15.2/
RUN mkdir /elasticsearch-7.15.2/snapshots &&\
    chown elasticsearch:elasticsearch /elasticsearch-7.15.2/snapshots

USER elasticsearch
CMD ["/usr/sbin/init"]
CMD ["/elasticsearch-7.15.2/bin/elasticsearch"]
```
https://hub.docker.com/layers/ivart074/my_repo_netology/latest/images/sha256-b84542317236f238fbad731f99e80a4e864f655dd62bb462d533675497133849?context=explore   
docker pull ivart074/my_repo_netology:latest  

![Screenshot 2021-12-06 011745](https://user-images.githubusercontent.com/87374285/144812881-3511caab-d695-4c8e-807f-748c282d10e8.png)  

#### 2. ------------------------
создаем индексы  
![Screenshot 2021-12-06 192608](https://user-images.githubusercontent.com/87374285/144821538-a1a09391-0d64-444d-9fb1-4465db69db4e.png)  
получаем статус  
![Screenshot 2021-12-06 192632](https://user-images.githubusercontent.com/87374285/144821564-65d4cff2-cb10-4e56-b315-fb6a3011956c.png)  
смотрим кластер и удаляем индексы  
![Screenshot 2021-12-06 192858](https://user-images.githubusercontent.com/87374285/144821578-7d47b6a0-77c9-472c-a00f-4b3a9ec8186f.png)  
индексы в "желтом" статусе, т.к. не хватает серверов для реплицирования  

#### 3. ------------------------  

Используя API зарегистрируйте данную директорию как snapshot repository c именем netology_backup.  
Приведите в ответе запрос API и результат вызова API для создания репозитория.  
![Screenshot 2021-12-06 195930](https://user-images.githubusercontent.com/87374285/144826231-722a20a1-4f89-494b-89a0-7b604433983e.png)  
Создайте индекс test с 0 реплик и 1 шардом и приведите в ответе список индексов.  
![Screenshot 2021-12-06 200711](https://user-images.githubusercontent.com/87374285/144827354-e552b77f-d1a7-4bc4-b9d0-c6ee5392fc65.png)  

Snapshot:
![Screenshot 2021-12-06 201006](https://user-images.githubusercontent.com/87374285/144827785-869e6951-18d5-4423-80f7-864629a75bde.png)  
список файлов:  
![Screenshot 2021-12-06 201949](https://user-images.githubusercontent.com/87374285/144829215-936886b6-68dd-4e9b-bb0b-a7f0e4e1f8c3.png)  
Удалите индекс test и создайте индекс test-2. Приведите в ответе список индексов.  
![Screenshot 2021-12-06 202312](https://user-images.githubusercontent.com/87374285/144829714-b93ad5f1-d750-4d95-b96d-3c19cd6f7e8f.png)  
восстанавливаем и смотрим список
![Screenshot 2021-12-06 205642](https://user-images.githubusercontent.com/87374285/144834525-ae6f29d3-5b26-4cfd-a6a5-99b8744aec31.png)  
  












