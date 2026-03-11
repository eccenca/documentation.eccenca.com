---
title: "cmemc: Command Group - dataset"
description: "List, create, delete, inspect, up-/download or open datasets."
icon: eccenca/artefact-dataset
tags:
  - cmemc
---

# dataset Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, create, delete, inspect, up-/download or open datasets.

This command group allows for managing workspace datasets as well as dataset file resources. Datasets can be created and deleted. File resources can be uploaded and downloaded. Details of dataset parameters can be listed with inspect.

Datasets are identified by a combined key of the `PROJECT_ID` and a `DATASET_ID` (e.g: `my-project:my-dataset`).

!!! note
    To get a list of existing datasets, execute the `dataset list` command or use tab-completion.

## dataset list

List available datasets.

```shell-session title="Usage"
$ cmemc dataset list [OPTIONS]
```

Output and filter a list of available datasets. Each dataset is listed with its ID, type and label.

??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter datasets by one of the following filter
                             names and a corresponding value: project, regex,
                             type, tag.
    --raw                    Outputs raw JSON objects of the dataset search API
                             response.
    --id-only                Lists only dataset IDs and no labels or other
                             metadata. This is useful for piping the IDs into
                             other cmemc commands.
    ```

## dataset delete

Delete datasets.

```shell-session title="Usage"
$ cmemc dataset delete [OPTIONS] [DATASET_IDS]...
```

This command deletes existing datasets in integration projects from Corporate Memory. The corresponding dataset resources will not be deleted.

!!! warning
    Datasets will be deleted without prompting.

!!! note
    Datasets can be listed by using the `dataset list` command.

??? info "Options"
    ```text

    -a, --all                Delete all datasets. This is a dangerous option, so
                             use it with care.
    --filter <TEXT TEXT>...  Filter datasets by one of the following filter
                             names and a corresponding value: project, regex,
                             type, tag.
    ```

## dataset download

Download the resource file of a dataset.

```shell-session title="Usage"
$ cmemc dataset download [OPTIONS] DATASET_ID OUTPUT_PATH
```

This command downloads the file resource of a dataset to your local file system or to standard out (`-`). Note that this is not possible for dataset types such as Knowledge Graph (`eccencaDataplatform`) or SQL endpoint (`sqlEndpoint`).

Without providing an output path, the output file name will be the same as the remote file resource.

!!! note
    Datasets can be listed by using the `dataset list` command.

??? info "Options"
    ```text

    --replace   Replace existing files. This is a dangerous option, so use it
                with care!
    ```

## dataset upload

Upload a resource file to a dataset.

```shell-session title="Usage"
$ cmemc dataset upload DATASET_ID INPUT_PATH
```

This command uploads a file to a dataset. The content of the uploaded file replaces the remote file resource. The name of the remote file resource will not be changed.

!!! warning
    If the remote file resource is used in more than one dataset, all of these datasets are affected by this command.

!!! warning
    The content of the uploaded file is not tested, so uploading a JSON file to an XML dataset will result in errors.

!!! note
    Datasets can be listed by using the `dataset list` command.

```shell-session title="Example"
$ cmemc dataset upload cmem:my-dataset new-file.csv
```

## dataset inspect

Display metadata of a dataset.

```shell-session title="Usage"
$ cmemc dataset inspect [OPTIONS] DATASET_ID
```

!!! note
    Datasets can be listed by using the `dataset list` command.

??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

## dataset create

Create a dataset.

```shell-session title="Usage"
$ cmemc dataset create [OPTIONS] [DATASET_FILE]
```

Datasets are created in projects and can have associated file resources. Each dataset has a type (such as `csv`) and a list of parameters which can alter or specify the dataset behaviour.

To get more information about available dataset types and associated parameters, use the `--help-types` and `--help-parameter` options.

```shell-session title="Example"
$ cmemc dataset create --project my-project --type csv my-file.csv
```

??? info "Options"
    ```text

    -t, --type TEXT                 The dataset type of the dataset to create.
                                    Example types are 'csv','json' and
                                    'eccencaDataPlatform' (-> Knowledge Graph).
    --project TEXT                  The project, where you want to create the
                                    dataset in. If there is only one project in
                                    the workspace, this option can be omitted.
    -p, --parameter <TEXT TEXT>...  A set of key/value pairs. Each dataset type
                                    has different parameters (such as charset,
                                    arraySeparator, ignoreBadLines, ...). In
                                    order to get a list of possible parameter,
                                    use the'--help-parameter' option.
    --replace                       Replace remote file resources in case there
                                    already exists a file with the same name.
    --id TEXT                       The dataset ID of the dataset to create. The
                                    dataset ID will be automatically created in
                                    case it is not present.
    --help-types                    Lists all possible dataset types on given
                                    Corporate Memory instance. Note that this
                                    option already needs access to the instance.
    --help-parameter                Lists all possible (optional and mandatory)
                                    parameter for a dataset type. Note that this
                                    option already needs access to the instance.
    ```

## dataset open

Open datasets in the browser.

```shell-session title="Usage"
$ cmemc dataset open DATASET_IDS...
```

With this command, you can open a dataset in the workspace in your browser.

The command accepts multiple dataset IDs which results in opening multiple browser tabs.

## dataset update

Update a dataset.

```shell-session title="Usage"
$ cmemc dataset update [OPTIONS] DATASET_ID
```

With this command, you can update the configuration of an existing dataset. Similar to the `dataset create` command, you need to use configuration key/value pairs on the ``--parameter`` option.

To get more information about the available configuration parameters on a dataset, use the ``--help-parameter`` option.

```shell-session title="Example"
$ cmemc dataset update my-project:my-csv -p separator ";"
```

??? info "Options"
    ```text

    -p, --parameter <TEXT TEXT>...  A configuration parameter key/value pair.
                                    Each dataset type has different parameters
                                    (such as charset, arraySeparator,
                                    ignoreBadLines, ...). In order to get a list
                                    of possible parameter, use the'--help-
                                    parameter' option.
    --help-parameter                Lists all possible (optional and mandatory)
                                    configuration parameter for a given dataset.
                                    Note that this option already needs access
                                    to the instance.
    ```
