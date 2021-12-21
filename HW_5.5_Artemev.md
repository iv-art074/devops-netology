### 1. Вопросы:
* Отличия replicated от global
  Для реплицированного сервиса вы указываете, сколько идентичных задач хотите запустить. Например, вы решили развернуть сервис HTTP с тремя репликами, каждая из которых обслуживает один и тот же контент.  
  Глобальный сервис — это сервис, который запускает одну задачу на каждой ноде. Предварительно заданного количества задач нет.
* Для выбора лидера в Docker Swarm кластере используется алгоритм Raft.
* Overlay Network - логическая сеть, создаваемая поверх другой сети.

### 2.Docker Swarm кластер в Яндекс.Облаке
![Screenshot 2021-11-20 151930](https://user-images.githubusercontent.com/87374285/142715492-3d0f54a5-34f1-4bbd-94fb-5cc4d08866a6.png)  

### 3. Кластер мониторинга, состоящий из стека микросервисов.  
![Screenshot 2021-11-20 153324](https://user-images.githubusercontent.com/87374285/142716845-b2c02906-90fb-4ac2-a1d2-8d2c19416ac1.png)

### 4. 
Команда docker swarm update --autolock=true инициирует блокировку ключей TLS и ключей обмена в swarm защитной шифрацией с генерирумым ключом, который надо будет ввести при разблокировке. 
 ```
 # docker swarm update --autolock=true

Swarm updated.
To unlock a swarm manager after it restarts, run the `docker swarm unlock`
command and provide the following key:

    SWMKEY-1-+MrE8NgAyKj5r3NcR4FiQMdgu+7W72urH0EZeSmP/0Y

Please remember to store this key in a password manager, since without it you
will not be able to restart the manager
 ```
