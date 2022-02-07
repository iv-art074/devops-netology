##### 1. Попробуйте запустить playbook на окружении из test.yml, зафиксируйте какое значение имеет факт some_fact для указанного хоста при выполнении playbook'a.  
![Screenshot 2022-02-07 213005](https://user-images.githubusercontent.com/87374285/152780130-a397829c-752d-4ef2-b976-3d81d34e2baf.png)  
##### 2. Найдите файл с переменными (group_vars) в котором задаётся найденное в первом пункте значение и поменяйте его на 'all default fact'.  
![Screenshot 2022-02-07 213438](https://user-images.githubusercontent.com/87374285/152781450-bab1e780-cba4-4544-bd42-07ccffeac3e7.png)  
##### 4. Проведите запуск playbook на окружении из prod.yml. Зафиксируйте полученные значения some_fact для каждого из managed host.  
![Screenshot 2022-02-07 220052](https://user-images.githubusercontent.com/87374285/152784541-7e392947-1b80-4470-9b27-deae57ceea1b.png)  


