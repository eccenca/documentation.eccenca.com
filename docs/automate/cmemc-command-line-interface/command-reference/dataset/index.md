---
title: "cmemc: Command Group - dataset"
description: "List, create, delete, inspect, up-/download or open datasets."
icon: material/database-outline
tags:
  - cmemc
---
# dataset Command Group

List, create, delete, inspect, up-/download or open datasets.

This command group allows for managing workspace datasets as well as
dataset file resources. Datasets can be created and deleted.
File resources can be uploaded and downloaded.
Details of dataset parameter can be listed with inspect.

Datasets are identified with a combined key of the project ID and the
project internal dataset ID (e.g: my-project:my-dataset). To get a list
of datasets, use the list command.

## dataset list

List available datasets.

Outputs a list of datasets IDs which can be used as reference for
the dataset create and delete commands.

```shell-session
$ cmemc dataset list [OPTIONS]
```

```text
Usage: cmemc dataset list [OPTIONS]

  List available datasets.

  Outputs a list of datasets IDs which can be used as reference for the
  dataset create and delete commands.

Options:
  --filter <TEXT TEXT>...  List datasets based on meta data. First parameter
                           --filter CHOICE can be one of ['project', 'regex',
                           'tag', 'type']. The second parameter is based on
                           CHOICE.

  --raw                    Outputs raw JSON objects of dataset search API
                           response.

  --id-only                Lists only dataset identifier and no labels or
                           other meta data. This is useful for piping the ids
                           into other cmemc commands.
```
## dataset delete

Delete datasets.

This deletes existing datasets in integration projects from Corporate
Memory. Datasets will be deleted without prompting!
Dataset resources will not be deleted.

Example: cmemc dataset delete my_project:my_dataset

Datasets can be listed by using the 'cmemc dataset list' command.

```shell-session
$ cmemc dataset delete [OPTIONS] [DATASET_IDS]...
```

```text
Usage: cmemc dataset delete [OPTIONS] [DATASET_IDS]...

  Delete datasets.

  This deletes existing datasets in integration projects from Corporate
  Memory. Datasets will be deleted without prompting! Dataset resources will
  not be deleted.

  Example: cmemc dataset delete my_project:my_dataset

  Datasets can be listed by using the 'cmemc dataset list' command.

Options:
  -a, --all                Delete all datasets. This is a dangerous option, so
                           use it with care.

  --project TEXT           In combination with the '--all' flag, this option
                           allows for deletion of all datasets of a certain
                           project. The behaviour is similar to the 'dataset
                           list --project' command.

  --filter <TEXT TEXT>...  Delete datasets based on meta data. First parameter
                           --filter CHOICE can be one of ['project', 'regex',
                           'tag', 'type']. The second parameter is based on
                           CHOICE.
```
## dataset download

Download the resource file of a dataset.

This command downloads the file resource of a dataset to your local
file system or to standard out (-).
Note that this is not possible for dataset types such as
Knowledge Graph (eccencaDataplatform) or SQL endpoint (sqlEndpoint).

Without providing an output path, the output file name will be the
same as the remote file resource.

Datasets can be listed by using the 'cmemc dataset list' command.

```shell-session
$ cmemc dataset download [OPTIONS] DATASET_ID OUTPUT_PATH
```

```text
Usage: cmemc dataset download [OPTIONS] DATASET_ID OUTPUT_PATH

  Download the resource file of a dataset.

  This command downloads the file resource of a dataset to your local file
  system or to standard out (-). Note that this is not possible for dataset
  types such as Knowledge Graph (eccencaDataplatform) or SQL endpoint
  (sqlEndpoint).

  Without providing an output path, the output file name will be the same as
  the remote file resource.

  Datasets can be listed by using the 'cmemc dataset list' command.

Options:
  --replace   Replace existing files. This is a dangerous option, so use it
              with care.
```
## dataset upload

Upload a resource file to a dataset.

This command uploads a file to a dataset.
The content of the uploaded file replaces the remote file resource.
The name of the remote file resource is not changed.

Warning: If the remote file resource is used in more than one dataset,
the other datasets are also affected by this command.

Warning: The content of the uploaded file is not tested, so uploading
a json file to an xml dataset will result in errors.

Datasets can be listed by using the 'cmemc dataset list' command.

Example: cmemc dataset upload cmem:my-dataset new-file.csv

```shell-session
$ cmemc dataset upload [OPTIONS] DATASET_ID INPUT_PATH
```

```text
Usage: cmemc dataset upload [OPTIONS] DATASET_ID INPUT_PATH

  Upload a resource file to a dataset.

  This command uploads a file to a dataset. The content of the uploaded file
  replaces the remote file resource. The name of the remote file resource is
  not changed.

  Warning: If the remote file resource is used in more than one dataset, the
  other datasets are also affected by this command.

  Warning: The content of the uploaded file is not tested, so uploading a
  json file to an xml dataset will result in errors.

  Datasets can be listed by using the 'cmemc dataset list' command.

  Example: cmemc dataset upload cmem:my-dataset new-file.csv
```
## dataset inspect

Display meta data of a dataset.

```shell-session
$ cmemc dataset inspect [OPTIONS] DATASET_ID
```

```text
Usage: cmemc dataset inspect [OPTIONS] DATASET_ID

  Display meta data of a dataset.

Options:
  --raw       Outputs raw JSON.
```
## dataset create

Create a dataset.

Datasets are created in projects and can have associated file
resources. Each dataset has a type (such as 'csv') and a list of
parameter which can change or specify the dataset behaviour.

To get more information on possible dataset types and parameter on these
types, use the '--help-types' and '--help-parameter' options.

Example: cmemc dataset create --project my-project --type csv my-file.csv

```shell-session
$ cmemc dataset create [OPTIONS] [DATASET_FILE]
```

```text
Usage: cmemc dataset create [OPTIONS] [DATASET_FILE]

  Create a dataset.

  Datasets are created in projects and can have associated file resources.
  Each dataset has a type (such as 'csv') and a list of parameter which can
  change or specify the dataset behaviour.

  To get more information on possible dataset types and parameter on these
  types, use the '--help-types' and '--help-parameter' options.

  Example: cmemc dataset create --project my-project --type csv my-file.csv

Options:
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

With this command, you can open a dataset in the workspace in
your browser.

The command accepts multiple dataset IDs which results in
opening multiple browser tabs.

```shell-session
$ cmemc dataset open [OPTIONS] DATASET_IDS...
```

```text
Usage: cmemc dataset open [OPTIONS] DATASET_IDS...

  Open datasets in the browser.

  With this command, you can open a dataset in the workspace in your
  browser.

  The command accepts multiple dataset IDs which results in opening multiple
  browser tabs.
```
