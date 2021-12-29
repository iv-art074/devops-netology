#### Задача 2. Написать серверный конфиг для атлантиса.

servers.yaml
```
#repos lists the config for specific repos.
repos:
  
- id: github.com/iv-art074/devops-netology

  apply_requirements: [mergeable]
  
  workflow: custom
  
  allowed_overrides: [workflow]

  allowed_workflows: [custom]

  allow_custom_workflows: true
  
workflows:
  # It's important that this is "default".
  default:
    plan:
      steps:
      - init
      - plan:
          extra_args: ["-lock=false"]
```

atlantis.yaml
```
version: 3
automerge: true
delete_source_branch_on_merge: true
projects:
- name: project1
  dir: .
  workspace: stage
    autoplan:
    when_modified: ["*.tf"]
    enabled: true
  workspace: prod
    autoplan:
    when_modified: ["*.tf"]
    enabled: true
  apply_requirements: [mergeable]
  workflow: myworkflow
workflows:
  myworkflow:
    plan:
      steps:
      - init
      - plan:
          extra_args: ["-lock", "false"]
    apply:
      steps:
      - apply
```
#### Задача 3. Знакомство с каталогом модулей.

Модули удобно использовать для сложной инфраструктуры с сотнями строк конфигураций, они снижают вероятность ошибок с повторениями кода, названий ресурсов. Оптимизируется время при повторном использовании конфигурации, применение модулей обеспечивает большую безопасность, т.к. включают передовые методы конфигурирования. 


