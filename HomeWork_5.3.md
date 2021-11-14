### 1. Посмотрите на сценарий ниже и ответьте на вопрос: "Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

* Высоконагруженное монолитное java веб-приложение;
  физический сервер предпочтительнее, т.к. монолитное и на микросервисы сложно разбить. к тому же высоконагруженное -  необходим прямой доступ к ресурсам

* Nodejs веб-приложение;
  это веб приложение и может размещаться в docker, для таких приложений достаточно докера, противопоказаний для контейнерной реализации не вижу.
 микросервисы смогут обеспечить хорошее функционирование.

* Мобильное приложение c версиями для Android и iOS;
  VM или bare metal сервера -  приложение в Docker не имеет GUI. 

* Шина данных на базе Apache Kafka;
  зависит от передаваемых данных или контура (тест/прод), для прода и критичности данных лучше VM.
   
* Elastic stack для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
  сам Elasticsearvh лучше на VM, отказоустойчивость решается на уровне кластера, кибану и логсташ можно вынести в докер контейнер.
   существуют разные решения, использование Docker имеет свои преимущества, можно перезаливать машину каждый месяц и получать опять полную функциональность

* Мониторинг-стек на базе prometheus и grafana;
  так как сами системы не хранят как таковых данных и возможно разделение на микросервисы, можно развернуть на Docker.
   
* Mongodb, как основное хранилище данных для java-приложения;
  можно использовать на Виртуальных машинах, как хранилище данных. Если высоконагруженное то на физических серверах.
   В контейнерах хранение данных не функционально.
   
* Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry
  Возможно Docker хранить в Docker и репозитории также, т.к. структура позволяет мультимодальность.


### 2.Опубликовать образ сайта в репо Docker и разместить ссылку
https://hub.docker.com/layers/177091780/ivart074/my_repo_netology/index_workin/images/sha256-ddcc6314157ca071326118ff606382101ec1c0d614ac89f6e9f52722f72e87ea?context=repo
```
PS C:\WINDOWS\system32> docker run --name static-site -d -p 8880:80 ivart074/my_repo_netology:index_workin nginx
```
![Снимок экрана 2021-11-12 234512](https://user-images.githubusercontent.com/87374285/141476954-c4e87334-8e44-4c96-9055-d2ce81a4ce78.png)


```
iv_art@Pappa-note:~$ docker run -v /data:/data -it --name container centos 
iv_art@Pappa-note:~$ docker run -v /data:/data -it --name container1 debian
iv_art@Pappa-note:~$ docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS          PORTS     NAMES
5104657a5fab   debian    "/bin/bash"   About a minute ago   Up 11 seconds             container1
108410ccf890   centos    "/bin/bash"   16 minutes ago       Up 14 minutes             container
iv_art@Pappa-note:~$ docker exec -it container /bin/bash
```
1й контейнер
```
[root@108410ccf890 /]# touch /data/file1.txt
```
Хост
```
iv_art@Pappa-note:/home$ cd ..
iv_art@Pappa-note:/$ cd data
iv_art@Pappa-note:/data$ ls -lh
total 0
-rw-r--r-- 1 root root 0 Nov 13 18:51 file1.txt
iv_art@Pappa-note:/data$ sudo touch file2.txt
iv_art@Pappa-note:/data$ ls -lh
total 0
-rw-r--r-- 1 root root 0 Nov 13 18:51 file1.txt
-rw-r--r-- 1 root root 0 Nov 13 18:55 file2.txt
```
2й контейнер

![Снимок экрана 2021-11-13 185905](https://user-images.githubusercontent.com/87374285/141612808-d2ed90b9-eb27-4932-aee0-65d932238899.png)
