--disable-repo-locking  
#Stops atlantis locking projects and or workspaces when running terraform  

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
projects:
- dir: project1
  autoplan:
    when_modified: ["*.tf*"]
  workspace: stage
- dir: project1
  workspace: prod
 
