### 1.Опубликовать образ сайта в репо Docker
https://hub.docker.com/layers/177091780/ivart074/my_repo_netology/index_workin/images/sha256-ddcc6314157ca071326118ff606382101ec1c0d614ac89f6e9f52722f72e87ea?context=repo
```
PS C:\WINDOWS\system32> docker run --name static-site -d -p 8880:80 ivart074/my_repo_netology:index_workin nginx
```
![Снимок экрана 2021-11-12 234512](https://user-images.githubusercontent.com/87374285/141476954-c4e87334-8e44-4c96-9055-d2ce81a4ce78.png)
