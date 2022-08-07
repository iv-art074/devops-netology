## 14.2 Синхронизация секретов с внешними сервисами. Vault"  
#### Задача 1: Работа с модулем Vault  

Запустить модуль Vault конфигураций через утилиту kubectl в установленном minikube  
```  
root@Pappa-wsl:/mnt/c/lessons/clokub-homeworks# kubectl apply -f 14.2/vault-pod.yml
pod/14.2-netology-vault created
```  
Получить значение внутреннего IP пода  
```  
root@Pappa-wsl:~# kubectl get pod 14.2-netology-vault -o json | jq -c '.status.podIPs'
[{"ip":"172.17.0.4"}]
```  

Запустить второй модуль для использования в качестве клиента и Установить дополнительные пакеты  
```  
root@Pappa-wsl:~# kubectl run -i --tty fedora --image=fedora --restart=Never -- sh
If you don't see a command prompt, try pressing enter.
sh-5.1# dnf -y install pip
Fedora 36 - x86_64                                                                      2.2 MB/s |  81 MB     00:36
Fedora 36 openh264 (From Cisco) - x86_64                                                593  B/s | 2.5 kB     00:04
Fedora Modular 36 - x86_64                                                              750 kB/s | 2.4 MB     00:03
Fedora 36 - x86_64 - Updates                                                            1.4 MB/s |  25 MB     00:17
Fedora Modular 36 - x86_64 - Updates                                                    793 kB/s | 2.5 MB     00:03
Last metadata expiration check: 0:00:01 ago on Sun Aug  7 06:20:44 2022.
Dependencies resolved.
========================================================================================================================
 Package                            Architecture           Version                         Repository              Size
========================================================================================================================
Installing:
 python3-pip                        noarch                 21.3.1-2.fc36                   fedora                 1.8 M
Installing weak dependencies:
 libxcrypt-compat                   x86_64                 4.4.28-1.fc36                   fedora                  90 k
 python3-setuptools                 noarch                 59.6.0-2.fc36                   fedora                 936 k

Transaction Summary
========================================================================================================================
Install  3 Packages

Total download size: 2.8 M
Installed size: 14 M
Downloading Packages:
(1/3): libxcrypt-compat-4.4.28-1.fc36.x86_64.rpm                                         81 kB/s |  90 kB     00:01
(2/3): python3-setuptools-59.6.0-2.fc36.noarch.rpm                                      368 kB/s | 936 kB     00:02
(3/3): python3-pip-21.3.1-2.fc36.noarch.rpm                                             655 kB/s | 1.8 MB     00:02
------------------------------------------------------------------------------------------------------------------------
Total                                                                                   828 kB/s | 2.8 MB     00:03
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                1/1
  Installing       : python3-setuptools-59.6.0-2.fc36.noarch                                                        1/3
  Installing       : libxcrypt-compat-4.4.28-1.fc36.x86_64                                                          2/3
  Installing       : python3-pip-21.3.1-2.fc36.noarch                                                               3/3
  Running scriptlet: python3-pip-21.3.1-2.fc36.noarch                                                               3/3
  Verifying        : libxcrypt-compat-4.4.28-1.fc36.x86_64                                                          1/3
  Verifying        : python3-pip-21.3.1-2.fc36.noarch                                                               2/3
  Verifying        : python3-setuptools-59.6.0-2.fc36.noarch                                                        3/3

Installed:
  libxcrypt-compat-4.4.28-1.fc36.x86_64   python3-pip-21.3.1-2.fc36.noarch   python3-setuptools-59.6.0-2.fc36.noarch

Complete!
sh-5.1# pip install hvac
Collecting hvac
  Downloading hvac-0.11.2-py2.py3-none-any.whl (148 kB)
     |████████████████████████████████| 148 kB 254 kB/s
Collecting six>=1.5.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting requests>=2.21.0
  Downloading requests-2.28.1-py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 182 kB/s
Collecting idna<4,>=2.5
  Downloading idna-3.3-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 815 kB/s
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.11-py2.py3-none-any.whl (139 kB)
     |████████████████████████████████| 139 kB 1.6 MB/s
Collecting charset-normalizer<3,>=2
  Downloading charset_normalizer-2.1.0-py3-none-any.whl (39 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2022.6.15-py3-none-any.whl (160 kB)
     |████████████████████████████████| 160 kB 2.7 MB/s
Installing collected packages: urllib3, idna, charset-normalizer, certifi, six, requests, hvac
Successfully installed certifi-2022.6.15 charset-normalizer-2.1.0 hvac-0.11.2 idna-3.3 requests-2.28.1 six-1.16.0 urllib3-1.26.11
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
sh-5.1#
```  
Запустить интепретатор Python и выполнить следующий код, предварительно поменяв IP и токен  
```  
sh-5.1# python3
Python 3.10.4 (main, Mar 25 2022, 00:00:00) [GCC 12.0.1 20220308 (Red Hat 12.0.1-0)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hvac
>>> client = hvac.Client(
... url='http://172.17.0.4:8200/',
... token='aiphohTaa0eeHei'
... )
>>> client.is_authenticated()
True
>>> # Пишем секрет
>>> client.secrets.kv.v2.create_or_update_secret(
... path='hvac',
... secret=dict(netology='Big secret!!!'),
... )
{'request_id': '4576144c-17ce-c1af-e2cc-4099ccde1b79', 'lease_id': '', 'renewable': False, 'lease_duration': 0, 'data': {'created_time': '2022-08-07T06:41:21.6387945Z', 'custom_metadata': None, 'deletion_time': '', 'destroyed': False, 'version': 1}, 'wrap_info': None, 'warnings': None, 'auth': None}
>>> # Читаем секрет
>>> client.secrets.kv.v2.read_secret_version(
... path='hvac',
... )
{'request_id': '44476012-271f-84fe-13c7-5221fb0e7326', 'lease_id': '', 'renewable': False, 'lease_duration': 0, 'data': {'data': {'netology': 'Big secret!!!'}, 'metadata': {'created_time': '2022-08-07T06:41:21.6387945Z', 'custom_metadata': None, 'deletion_time': '', 'destroyed': False, 'version': 1}}, 'wrap_info': None, 'warnings': None, 'auth': None}
>>>
```  
Вид из web-интерфейса  
![image](https://user-images.githubusercontent.com/87374285/183288472-979f97cb-cf5a-479f-9803-d195878bb8dd.png)  

