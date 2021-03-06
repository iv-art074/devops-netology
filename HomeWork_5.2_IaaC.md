### 1. Преимущества подхода IaaC: 
  * цена - уменьшение расходов не только финансов, но и времени на операции
  * скорость - при автоматизации уменьшается время на обычные операции, фокусируется внимание на более важных задачах, соответственно повышается скорость работы
  * уменьшение рисков - автоматизация инфраструктуры позволяет минимизировать риск возникновения человеческой ошибки. 
  Основополагающий принцип - идемпотентность, способность операций или объектов повторять один и тот же результат   
  
### 2. 
   * Чем Ansible выгодно отличается от других систем управление конфигурациями?
 Главное отличие Ansible от других - система не требует установки специального программного обеспечения на узлах, где будет работать. Контрольный механизм, настроенный в программном обеспечении Ansible, связывается с узлами через стандартные каналы SSH. 
   * Какой, на ваш взгляд, метод работы систем конфигурации более надёжный push или pull?
   Мне кажется - pull.
   Проблема с системами на основе push заключается в том, что у вас должна быть полная модель всей архитектуры на центральном push-узле. Вы не можете "толкнуть" машину, о которой не знаете. Также в «вытягивающей» системе клиенты связываются с сервером независимо друг от друга, поэтому система в целом более масштабируема, чем «выталкивающая» система. 
Но лучше, конечно, работать с универсальной системой и подстраиваться под требования конкретной ситуации.  

### 3. 
```
$ vagrant version
Installed Version: 2.2.19
Latest Version: 2.2.19

You're running an up-to-date version of Vagrant!
```
![Безымянный](https://user-images.githubusercontent.com/87374285/140631966-c83d314d-2fb6-4b4d-8614-e59d47ccdf87.png)


```
vagrant@server1:~$ ansible --version
ansible 2.9.6
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/vagrant/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 3.8.10 (default, Jun  2 2021, 10:49:15) [GCC 9.4.0]
  ```
### 4.
![Screenshot 2021-11-08 225411](https://user-images.githubusercontent.com/87374285/140745543-b7524f0a-ef45-4597-913b-843588baf842.png)
