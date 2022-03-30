#### DevOps  
В репозитории содержится код проекта на python. Проект - RESTful API сервис. Ваша задача автоматизировать сборку образа с выполнением python-скрипта:  

Образ собирается на основе centos:7  
Python версии не ниже 3.7  
Установлены зависимости: flask flask-jsonpify flask-restful  
Создана директория /python_api  
Скрипт из репозитория размещён в /python_api  
Точка вызова: запуск скрипта  
Если сборка происходит на ветке master: Образ должен пушится в docker registry вашего gitlab python-api:latest, иначе этот шаг нужно пропустить  

![Screenshot 2022-03-30 224504](https://user-images.githubusercontent.com/87374285/160845596-727efc97-c2bd-49b5-9c74-1ba7298aba00.png)  

![Screenshot 2022-03-30 232600](https://user-images.githubusercontent.com/87374285/160845348-0cd40ca7-2995-46f3-a922-1dd9977dfe29.png)  

#### Product Owner  
Вашему проекту нужна бизнесовая доработка: необходимо поменять JSON ответа на вызов метода GET /rest/api/get_info, необходимо создать Issue в котором указать:  

Какой метод необходимо исправить  
Текст с { "message": "Already started" } на { "message": "Running"}  
Issue поставить label: feature  

![Screenshot 2022-03-30 231827](https://user-images.githubusercontent.com/87374285/160843823-d9153143-576b-45ef-b895-d43cf7cddfe5.png)  

#### Developer  
Вам пришел новый Issue на доработку, вам необходимо:  

Создать отдельную ветку, связанную с этим issue  
Внести изменения по тексту из задания  
Подготовить Merge Request, влить необходимые изменения в master, проверить, что сборка прошла успешно  

![Screenshot 2022-03-30 234502](https://user-images.githubusercontent.com/87374285/160849375-7509e5bc-0cd2-420c-bdd6-edb13c0de687.png)  
Сборка успешна
![Screenshot 2022-03-30 235051](https://user-images.githubusercontent.com/87374285/160850649-d42b3df2-4bf6-47bf-be03-550f11c9c925.png)  

#### Tester  
Разработчики выполнили новый Issue, необходимо проверить валидность изменений:  

Поднять докер-контейнер с образом python-api:latest и проверить возврат метода на корректность  
Закрыть Issue с комментарием об успешности прохождения, указав желаемый результат и фактически достигнутый  
![Screenshot 2022-03-30 234516](https://user-images.githubusercontent.com/87374285/160849415-fed08c89-4aca-4bb4-b80a-123c83c09723.png)  

Ссылка на проект  
https://gitlab.com/prospero_iv/homework_9-6.git  



