---
title: "cmemc: Command Group - project variable"
description: "List, create, delete or get data from project variables."
icon: material/variable-box
tags:
  - Variables
  - cmemc
---

# project variable Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, create, delete or get data from project variables.

Project variables can be used in dataset and task parameters, and in the template transform operator. Variables are either based on a static value or based on a template. They may use templates that access globally configured variables or other preceding variables from the same project.

Variables are identified by a `VARIABLE_ID`. To get a list of existing variables, execute the list command or use tab-completion. The `VARIABLE_ID` is a concatenation of a `PROJECT_ID` and a `VARIABLE_NAME`, such as `my-project:my-variable`.

## project variable list

List available project variables.

```shell-session title="Usage"
cmemc project variable list [OPTIONS]
```

Outputs a table or a list of project variables.

??? info "Options"
    ```text

    --raw                    Outputs raw JSON.
    --id-only                Lists only variables names and no other metadata.
                             This is useful for piping the IDs into other
                             commands.
    --filter <TEXT TEXT>...  Filter project variables by one of the following
                             filter names and a corresponding value: project,
                             regex.
    ```

## project variable get

Get the value or other data of a project variable.

```shell-session title="Usage"
cmemc project variable get [OPTIONS] VARIABLE_ID
```

Use the ``--key`` option to specify which information you want to get.

!!! note
    Only the `value` key is always available on a project variable. Static value variables have no `template` key, and the `description` key is optional for both types of variables.

??? info "Options"
    ```text

    --key [value|template|description]
                                    Specify the name of the value you want to
                                    get.  [default: value]
    --raw                           Outputs raw json.
    ```

## project variable delete

Delete project variables.

```shell-session title="Usage"
cmemc project variable delete [OPTIONS] [VARIABLE_IDS]...
```

There are three selection mechanisms: with specific IDs - only those specified variables will be deleted; by using `--filter` - variables based on the filter type and value will be deleted; by using `--all`, which will delete all variables.

Variables are automatically sorted by their dependencies and deleted in the correct order (template-based variables that depend on others are deleted first, then their dependencies).

??? info "Options"
    ```text

    -a, --all                Delete all variables. This is a dangerous option,
                             so use it with care.
    --filter <TEXT TEXT>...  Filter project variables by one of the following
                             filter names and a corresponding value: project,
                             regex.
    ```

## project variable create

Create a new project variable.

```shell-session title="Usage"
cmemc project variable create [OPTIONS] VARIABLE_NAME
```

Variables need to be created with a value or a template (not both). In addition to that, a project ID and a name are mandatory.

```shell-session title="Example"
cmemc project variable create my_var --project my_project --value abc
```

!!! note
    cmemc is currently not able to manage the order of the variables in a project. This means you have to create plain value variables in advance, before you can create template based variables, which access these values.

??? info "Options"
    ```text

    --value TEXT        The value of the new project variable.
    --template TEXT     The template of the new project variable. You can use
                        Jinja template syntax, e.g. use '{{global.myVar}}' for
                        accessing global variables, or '{{project.myVar}}' for
                        accessing variables from the same project.
    --description TEXT  The optional description of the new project variable.
    --project TEXT      The project, where you want to create the variable in.
                        If there is only one project in the workspace, this
                        option can be omitted.
    ```

## project variable update

Update data of an existing project variable.

```shell-session title="Usage"
cmemc project variable update [OPTIONS] VARIABLE_ID
```

With this command you can update the value or the template, as well as the description of a project variable.

!!! note
    If you update the template of a static variable, it will be transformed to a template based variable. If you want to change the value of a template based variable, an error will be shown.

??? info "Options"
    ```text

    --value TEXT        The new value of the project variable.
    --template TEXT     The new template of the project variable. You can use
                        Jinja template syntax, e.g. use '{{global.myVar}}' for
                        accessing global variables, or '{{project.myVar}}' for
                        accessing variables from the same project.
    --description TEXT  The new description of the project variable.
    ```
