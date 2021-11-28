###### 1. Поднимите инстанс PostgreSQL (версию 12) c 2 volume
docker pull postgres:12
iv_art@Pappa-note:~$ docker volume create vol2
vol2
iv_art@Pappa-note:~$ docker volume create vol1
vol1
iv_art@Pappa-note:~$ docker run --rm --name psg -e POSTGRES_PASSWORD=postgres -ti -p 5432:5432 -v vol1:/var/lib/postgresql/data -v vol2:/var/lib/postgresql postgres:12  

![Screenshot 2021-11-28 204128](https://user-images.githubusercontent.com/87374285/143764530-f5dbaf07-9066-4420-bd9e-4173dd15d165.png)

