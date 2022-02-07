##### 1. Попробуйте запустить playbook на окружении из test.yml, зафиксируйте какое значение имеет факт some_fact для указанного хоста при выполнении playbook'a.  
![Screenshot 2022-02-07 213005](https://user-images.githubusercontent.com/87374285/152780130-a397829c-752d-4ef2-b976-3d81d34e2baf.png)  
##### 2. Найдите файл с переменными (group_vars) в котором задаётся найденное в первом пункте значение и поменяйте его на 'all default fact'.  
![Screenshot 2022-02-07 213438](https://user-images.githubusercontent.com/87374285/152781450-bab1e780-cba4-4544-bd42-07ccffeac3e7.png)  
##### 4. Проведите запуск playbook на окружении из prod.yml. Зафиксируйте полученные значения some_fact для каждого из managed host.  
![Screenshot 2022-02-07 220052](https://user-images.githubusercontent.com/87374285/152784541-7e392947-1b80-4470-9b27-deae57ceea1b.png)  
##### 5-6. Добавьте факты в group_vars каждой из групп хостов так, чтобы для some_fact получились следующие значения: для deb - 'deb default fact', для el - 'el default fact'. Повторите запуск playbook на окружении prod.yml. Убедитесь, что выдаются корректные значения для всех хостов. #####  
![Screenshot 2022-02-07 220632](https://user-images.githubusercontent.com/87374285/152785239-8262c4a6-cf0b-4155-b877-d4791be5607f.png)  
##### 7.При помощи ansible-vault зашифруйте факты в group_vars/deb и group_vars/el с паролем netology.  
![Screenshot 2022-02-07 221147](https://user-images.githubusercontent.com/87374285/152785827-5e05b3e5-8dea-45a4-a4a4-06b6ef9a4a95.png)  
##### 8. Запустите playbook на окружении prod.yml. При запуске ansible должен запросить у вас пароль. Убедитесь в работоспособности.  
![Screenshot 2022-02-07 221340](https://user-images.githubusercontent.com/87374285/152786087-e4aedbf4-acbd-4e68-adf2-eae620c6ae9d.png)  
##### 9. Посмотрите при помощи ansible-doc список плагинов для подключения. Выберите подходящий для работы на control node.  
Огромное количество плагинов, потому что Control node - это просто сервер Linux, на котором установлен Ansible и который используется для управления удаленными хостами или узлами.  К примеру netapp_eseries.santricity.santricity_host который собирает информацию о хосте..  
##### 10-11. В prod.yml добавьте новую группу хостов с именем local, в ней разместите localhost с необходимым типом подключения. Запустите playbook на окружении prod.yml. При запуске ansible должен запросить у вас пароль. Убедитесь что факты some_fact для каждого из хостов определены из верных group_vars.  
![Screenshot 2022-02-07 225545](https://user-images.githubusercontent.com/87374285/152792134-7beec448-7b48-4b69-b6a6-549987c4689a.png)  

##### 12. Репозиторий  
https://github.com/iv-art074/ansible_base  



