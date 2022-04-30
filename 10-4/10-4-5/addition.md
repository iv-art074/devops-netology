Конфиги на месте:  

![Screenshot 2022-04-30 130916](https://user-images.githubusercontent.com/87374285/166088264-05bce65a-ac0a-4678-8514-ffa7336ab06f.jpg)  
![Screenshot 2022-04-30 130519](https://user-images.githubusercontent.com/87374285/166088303-8dbbde7f-1266-4ba5-8499-548b93562b0d.jpg)  

очевидно, что FB просто не видит логов some_app  

![Screenshot 2022-04-30 130214](https://user-images.githubusercontent.com/87374285/166088314-08eba0f2-1875-4ab1-b6ef-8638ca8da098.jpg)  

я не очень силен в Linux и не понимаю, как такое может быть  

```
root@Pappa:/home/iv_art/devops-netology/10-4/10-4-5# docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED       STATUS       PORTS                              NAMES
e9041621453f   elastic/filebeat:7.16.2   "/usr/bin/tini -- /u…"   2 hours ago   Up 2 hours                                      filebeat
5febedb28d70   kibana:7.16.2             "/bin/tini -- /usr/l…"   2 hours ago   Up 2 hours   0.0.0.0:5601->5601/tcp             kibana
d51e9ae2e110   elastic/logstash:7.16.2   "/usr/local/bin/dock…"   2 hours ago   Up 2 hours   0.0.0.0:5044->5044/tcp, 9600/tcp   logstash
8d192c56c068   elasticsearch:7.16.2      "/bin/tini -- /usr/l…"   2 hours ago   Up 2 hours   0.0.0.0:9200->9200/tcp, 9300/tcp   es-hot
16ee9cc7ad37   python:3.9-alpine         "python3 /opt/run.py"    2 hours ago   Up 2 hours                                      some_app
691a0450422a   elasticsearch:7.16.2      "/bin/tini -- /usr/l…"   2 hours ago   Up 2 hours   9200/tcp, 9300/tcp                 es-warm
```
Some_app должен выгружать логи:  

```
root@Pappa:/home/iv_art/devops-netology/10-4/10-4-5# docker inspect 16ee9cc7ad37 | grep -E "LogPath"
        "LogPath": "/var/lib/docker/containers/16ee9cc7ad37f6e04827a847c51c0b2246b3de34b53e97ba52af79c0d1a132ce/16ee9cc7ad37f6e04827a847c51c0b2246b3de34b53e97ba52af79c0d1a132ce-json.log",
```
но там ничего нет  

```
root@Pappa:/home/iv_art/devops-netology/10-4/10-4-5# cat /var/lib/docker/containers/16ee9cc7ad37f6e04827a847c51c0b2246b3de34b53e97ba52af79c0d1a132ce/16ee9cc7ad37f6e04827a847c51c0b2246b3de34b53e97ba52af79c0d1a132ce-json.log
cat: /var/lib/docker/containers/16ee9cc7ad37f6e04827a847c51c0b2246b3de34b53e97ba52af79c0d1a132ce/16ee9cc7ad37f6e04827a847c51c0b2246b3de34b53e97ba52af79c0d1a132ce-json.log: No such file or directory
```
т.е. вообще ничего  

```
root@Pappa:/home/iv_art/devops-netology/10-4/10-4-5# ls -lh /var/lib/docker/containers
total 0
root@Pappa:/home/iv_art/devops-netology/10-4/10-4-5# ls -la /var/lib/docker/containers
total 8
drwxr-xr-x 2 root root 4096 Apr 30 10:33 .
drwxr-xr-x 3 root root 4096 Apr 30 00:04 ..
root@Pappa:/home/iv_art/devops-netology/10-4/10-4-5#
```
возможно, потому что WSL не поддерживает systemd:   

```
root@Pappa:/home/iv_art/devops-netology/10-4/10-4-5# journalctl
No journal files were found.
-- No entries --
```

