--disable-repo-locking  
#Stops atlantis locking projects and or workspaces when running terraform  

```
#repos lists the config for specific repos.
repos:
  # id can either be an exact repo ID or a regex.
  # If using a regex, it must start and end with a slash.
  # Repo ID's are of the form {VCS hostname}/{org}/{repo name}, ex.
  # github.com/runatlantis/atlantis.
- id: github.com/iv-art074/devops-netology

# apply_requirements sets the Apply Requirements for all repos that match.
  apply_requirements: [mergeable]

  # workflow sets the workflow for all repos that match.
  # This workflow must be defined in the workflows section.
  workflow: custom

  # allowed_workflows specifies which workflows the repos that match 
  # are allowed to select.
  allowed_workflows: [custom]

  # allow_custom_workflows defines whether this repo can define its own
  # workflows. If false (default), the repo can only use server-side defined
  # workflows.
  allow_custom_workflows: true

  # pre_workflow_hooks defines arbitrary list of scripts to execute before workflow execution.
  pre_workflow_hooks: 
    - run: my-pre-workflow-hook-command arg1

  # id can also be an exact match.
- id: github.com/iv-art074/devops-netology

# workflows lists server-side custom workflows
workflows:
  custom:
    plan:
      steps:
      - run: my-custom-command arg1 arg2
      - init
      - plan:
          extra_args: ["-lock", "false"]
      - run: my-custom-command arg1 arg2
    apply:
      steps:
      - run: echo hi
      - apply
      ```
      
