---
title: "cmemc: Command Group - project file"
description: "List, inspect, up-/download or delete project file resources."
icon: eccenca/artefact-file
tags:
  - Files
  - cmemc
---
# project file Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, inspect, up-/download or delete project file resources.

File resources are identified with a `RESOURCE_ID` which is a concatenation of its project ID and its relative path, e.g. `my-project:path-to/table.csv`.

!!! note
    To get a list of existing file resources, execute the `project file list` command or use tab-completion.



## project file list

List available file resources.

```shell-session title="Usage"
$ cmemc project file list [OPTIONS]
```




Outputs a table or a list of file resources.



??? info "Options"
    ```text

    --raw                    Outputs raw JSON.
    --id-only                Lists only resource IDs and no other metadata. This
                             is useful for piping the IDs into other commands.
    --filter <TEXT TEXT>...  Filter file resources by one of the following
                             filter names and a corresponding value: project,
                             regex.
    ```

## project file delete

Delete file resources.

```shell-session title="Usage"
$ cmemc project file delete [OPTIONS] [RESOURCE_IDS]...
```




There are three selection mechanisms: with specific IDs - only those specified resources will be deleted; by using `--filter` - resources based on the filter type and value will be deleted; by using `--all`, which will delete all resources.



??? info "Options"
    ```text

    --force                  Delete resource even if in use by a task.
    -a, --all                Delete all resources. This is a dangerous option,
                             so use it with care.
    --filter <TEXT TEXT>...  Filter file resources by one of the following
                             filter names and a corresponding value: project,
                             regex.
    ```

## project file download

Download file resources to the local file system.

```shell-session title="Usage"
$ cmemc project file download [OPTIONS] [RESOURCE_IDS]...
```




This command downloads one or more file resources from projects to your local file system. Files are saved with their resource names in the output directory.

Resources are identified by their IDs in the format `PROJECT_ID`:`RESOURCE_NAME`.

```shell-session title="Example"
$ cmemc project file download my-proj:my-file.csv
```


```shell-session title="Example"
$ cmemc project file download my-proj:file1.csv my-proj:file2.csv --output-dir /tmp
```




??? info "Options"
    ```text

    --output-dir DIRECTORY  The directory where the downloaded files will be
                            saved. If this directory does not exist, it will be
                            created.  [default: .]
    --replace               Replace existing files. This is a dangerous option,
                            so use it with care!
    ```

## project file upload

Upload a file to a project.

```shell-session title="Usage"
$ cmemc project file upload [OPTIONS] INPUT_PATH
```




This command uploads a file to a project as a file resource.

!!! note
    If you want to create a dataset from your file, the `dataset create` command is maybe the better option.


```shell-session title="Example"
$ cmemc project file upload my-file.csv --project my-project
```




??? info "Options"
    ```text

    --project TEXT  The project where you want to upload the file. If there is
                    only one project in the workspace, this option can be
                    omitted.
    --path TEXT     The path/name of the file resource in the project (e.g.,
                    'data/file.csv'). If not specified, the local file name will
                    be used.
    --replace       Replace existing file resource. This is a dangerous option,
                    so use it with care!
    ```

## project file inspect

Display all metadata of a file resource.

```shell-session title="Usage"
$ cmemc project file inspect [OPTIONS] RESOURCE_ID
```





??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

## project file usage

Display all usage data of a file resource.

```shell-session title="Usage"
$ cmemc project file usage [OPTIONS] RESOURCE_ID
```





??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

