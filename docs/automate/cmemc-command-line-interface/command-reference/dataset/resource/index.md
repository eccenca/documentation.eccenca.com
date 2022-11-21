---
title: "cmemc: Command Group - dataset resource"
description: "List, inspect or delete dataset file resources."
icon: eccenca/artefact-file
tags:
  - cmemc
---
# dataset resource Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, inspect or delete dataset file resources.

File resources are identified by its name and project ID.


## dataset resource list

List available file resources.

```shell-session title="Usage"
$ cmemc dataset resource list [OPTIONS]
```




Outputs a table or a list of dataset resources (files).



??? info "Options"
    ```text

    --raw                    Outputs raw JSON.
    --id-only                Lists only resource names and no other meta data.
                             This is useful for piping the IDs into other
                             commands.
  
    --filter <TEXT TEXT>...  Filter file resources based on a meta data. First
                             parameter CHOICE can be one of ['project',
                             'regex']. The second parameter is based on CHOICE,
                             e.g. a project ID or a regular expression string.
    ```

## dataset resource delete

Delete file resources.

```shell-session title="Usage"
$ cmemc dataset resource delete [OPTIONS] [RESOURCE_IDS]...
```




You have three selection mechanisms: with specific IDs, you will delete only these resources; by using `--filter` your will delete resources based on the filter type and value; by using `--all` will delete all resources.



??? info "Options"
    ```text

    --force                  Delete resource even if in use by a task.
    -a, --all                Delete all resources. This is a dangerous option,
                             so use it with care.
  
    --filter <TEXT TEXT>...  Filter file resources based on a meta data. First
                             parameter CHOICE can be one of ['project',
                             'regex']. The second parameter is based on CHOICE,
                             e.g. a project ID or a regular expression string.
    ```

## dataset resource inspect

Display all meta data of a file resource.

```shell-session title="Usage"
$ cmemc dataset resource inspect [OPTIONS] RESOURCE_ID
```





??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

## dataset resource usage

Display all usage data of a file resource.

```shell-session title="Usage"
$ cmemc dataset resource usage [OPTIONS] RESOURCE_ID
```





??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

