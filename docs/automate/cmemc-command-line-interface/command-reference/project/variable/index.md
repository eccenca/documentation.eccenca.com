---
title: "cmemc: Command Group - project variable"
description: "List, create, delete or get data from project and execution variables."
icon: material/variable-box
tags:
  - Variables
  - cmemc
---

# project variable Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, create, delete or get data from project and execution variables.

Project variables can be used in dataset and task parameters, and in the template transform operator. Execution variables are declared on a single task of a project, such as a workflow or a dataset. Global variables are defined in the configuration of Corporate Memory. They are listed and can be read, but not changed. Variables are either based on a static value or based on a template. They may use templates that access globally configured variables or other preceding variables from the same project.

Variables are identified by a `VARIABLE_ID`. To get a list of existing variables, execute the list command or use tab-completion. The `VARIABLE_ID` of a project variable is a concatenation of a `PROJECT_ID` and a `VARIABLE_NAME`, such as `my-project:my-variable`. The `VARIABLE_ID` of an execution variable adds the `TASK_ID`, such as `my-project:my-task:my-variable`. The `VARIABLE_ID` of a global variable is its `VARIABLE_NAME`.

!!! note
    Variables can be flagged as sensitive. Corporate Memory does not hand out the value and the template of such a variable, they are only available to other sensitive variables of the same scope and to task parameters which accept sensitive variables, such as password parameters.


!!! note
    The default value of an execution variable can be overridden for a single run with the `--parameter` option of the `workflow execute` and `workflow io` commands. Workflows started by a scheduler can not take such overrides, they always use the default values.



## project variable list

List available project, execution and global variables.

```shell-session title="Usage"
cmemc project variable list [OPTIONS]
```




Outputs a table or a list of project variables, the execution variables of tasks and the global variables. The table states the scope of each variable (project, execution or global) and, for execution variables, the label of the task they are declared on.

Sensitive variables are marked and listed without their value and template, since Corporate Memory does not hand them out.

Errors of single variables, such as a template which can not be resolved, are shown as warnings below the table.



??? info "Options"
    ```text

    --raw                    Outputs raw JSON.
    --id-only                Lists only variables names and no other metadata.
                             This is useful for piping the IDs into other
                             commands.
    --filter <TEXT TEXT>...  Filter variables by one of the following filter
                             names and a corresponding value: project, scope,
                             sensitive, type, task, regex.
    ```

## project variable get

Get the value or other data of a project, execution or global variable.

```shell-session title="Usage"
cmemc project variable get [OPTIONS] VARIABLE_ID
```




Use the ``--key`` option to specify which information you want to get.

!!! note
    Only the `value` key is always available on a project variable. Static value variables have no `template` key, and the `description` key is optional for both types of variables. Use `--raw` to access all fields.


The value and the template of a sensitive variable can not be read, only its description is available.



??? info "Options"
    ```text

    --key [value|template|description]
                                    Specify the name of the value you want to
                                    get.  [default: value]
    --raw                           Outputs raw json.
    ```

## project variable delete

Delete project and execution variables.

```shell-session title="Usage"
cmemc project variable delete [OPTIONS] [VARIABLE_IDS]...
```




There are three selection mechanisms: with specific IDs - only those specified variables will be deleted; by using `--filter` - variables based on the filter type and value will be deleted; by using `--all`, which will delete all variables.

Variables are automatically sorted by their dependencies and deleted in the correct order (template-based variables that depend on others are deleted first, then their dependencies).

Global variables can not be deleted. If `--all` or `--filter` select them, they are skipped.

An execution variable of a workflow is deleted even if tasks of the workflow still use it. In this case, a warning names these tasks, since a run of the workflow then needs the variable as parameter.



??? info "Options"
    ```text

    -a, --all                Delete all variables. This is a dangerous option,
                             so use it with care.
    --filter <TEXT TEXT>...  Filter variables by one of the following filter
                             names and a corresponding value: project, scope,
                             sensitive, type, task, regex.
    ```

## project variable create

Create a new project or execution variable.

```shell-session title="Usage"
cmemc project variable create [OPTIONS] VARIABLE_NAME
```




Variables need to be created with a value or a template (not both). In addition to that, a project ID and a name are mandatory. Use the ``--task`` option to create an execution variable on a task instead of a project variable. The task is given as `PROJECT_ID`:`TASK_ID`, so the ``--project`` option is not used then.

```shell-session title="Example"
cmemc project variable create my_var --project my_project --value abc
```


```shell-session title="Example"
cmemc project variable create my_var --task my_project:my_workflow --value abc
```


!!! note
    cmemc is currently not able to manage the order of the variables in a project. This means you have to create plain value variables in advance, before you can create template based variables, which access these values.




??? info "Options"
    ```text

    --value TEXT        The value of the new variable.
    --template TEXT     The template of the new variable. You can use Jinja
                        template syntax, e.g. use '{{global.myVar}}' for
                        accessing global variables, or '{{project.myVar}}' for
                        accessing variables from the same project.
    --description TEXT  The optional description of the new variable.
    --sensitive         Flag the new variable as sensitive. The value and the
                        template of a sensitive variable can not be read back,
                        they are only available to other sensitive variables and
                        to task parameters which accept sensitive variables.
    --project TEXT      The project, where you want to create the project
                        variable in. If there is only one project in the
                        workspace, this option can be omitted.
    --task TEXT         The task, where you want to create an execution variable
                        on, given as PROJECT_ID:TASK_ID. Without this option, a
                        project variable is created.
    ```

## project variable update

Update data of an existing project or execution variable.

```shell-session title="Usage"
cmemc project variable update [OPTIONS] VARIABLE_ID
```




With this command you can update the value or the template, as well as the description and the sensitive flag of a variable.

!!! note
    If you update the template of a static variable, it will be transformed to a template based variable. If you want to change the value of a template based variable, an error will be shown.


!!! note
    The value and the template of a sensitive variable can not be read. An update which does not set them keeps the stored ones. Since it is not known whether a sensitive variable is template based, a new value or template replaces whatever it had. Removing the sensitive flag with `--no-sensitive` needs a new `--value` or `--template`.




??? info "Options"
    ```text

    --value TEXT                  The new value of the project variable.
    --template TEXT               The new template of the project variable. You
                                  can use Jinja template syntax, e.g. use
                                  '{{global.myVar}}' for accessing global
                                  variables, or '{{project.myVar}}' for
                                  accessing variables from the same project.
    --description TEXT            The new description of the project variable.
    --sensitive / --no-sensitive  Flag the variable as sensitive, or remove the
                                  flag. Without this option, the flag stays as
                                  it is. Removing the flag needs a new value or
                                  template.
    ```
