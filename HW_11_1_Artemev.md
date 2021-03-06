### Домашнее задание к занятию "11.1. Введение в микросервисы"  
#### Задача 1: Интернет Магазин   
Руководство крупного интернет магазина у которого постоянно растёт пользовательская база и количество заказов рассматривает возможность переделки своей внутренней ИТ системы на основе микросервисов.  
Вас пригласили в качестве консультанта для оценки целесообразности перехода на микросервисную архитектуру.  
Опишите какие выгоды может получить компания от перехода на микросервисную архитектуру и какие проблемы необходимо будет решить в первую очередь.  
Ответ:  

Выгоды:  
1. В распределенной системе снижается зависимость между компонентами.  
2. Возможность оперативно наращивать мощности за счет горизонтального масштабирования и обратно, сокращать объем системы при снижении нагрузки.  
3. Снижаются риски деградации системы и полного отказа, за счет отсутствия единой точки отказа, повышается работоспособность.  
4. Возможность использования разных технологий в разных сервисах, а так же применение оптимального стека технологий для новых сервисов.  
5. Снижение зависимости от одного разработчика (отдельные микросервисы могут разрабатывать разные компании).  
6. Повышение возможности делать более частые релизы , т.е. быстрее выводить новые функции и фичи, сюда же можно отнести возможность автоматизации CI/CD,   
   ускорение тестирования - тестирование отдельных сервисов, а не монолитной системы с регресс-тестированием при модификации какой-либо части.  
7. Повышение надежности и безопасности (сбой одного микросервиса, как правило, не ведет к выходу из строя всей системы, и может быть устранен в меньшие сроки).  
   
Проблемы:  
1. Микросервисы не являются панацеей, и решать проблемы вычислительных мощностей и инфраструктуры также придется.  
2. Необходимо развивать дополнительные компетенции службы технической поддержки и сопровождения.  
3. Необходимо повышать квалификацию разработчиков и расширять функциональные обязанности (документирование, версионирование).    
4. Введение дополнительных служб (возможно внтурикоманндного распределение обязанностей)  
