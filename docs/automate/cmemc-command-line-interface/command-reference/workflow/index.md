---
title: "cmemc: Command Group - workflow"
description: "List, execute, status or open (io) workflows."
icon: eccenca/artefact-workflow
tags:
  - Workflow
  - cmemc
---
# workflow Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, execute, status or open (io) workflows.

Workflows are identified by a `WORKFLOW_ID`. The get a list of existing workflows, execute the list command or use tab-completion. The `WORKFLOW_ID` is a concatenation of a `PROJECT_ID` and a `TASK_ID`, such as `my-project:my-workflow`.


## workflow execute

Execute workflow(s).

```shell-session title="Usage"
$ cmemc workflow execute [OPTIONS] [WORKFLOW_IDS]...
```




With this command, you can start one or more workflows at the same time or in a sequence, depending on the result of the predecessor.

Executing a workflow can be done in two ways: Without `--wait` just sends the starting signal and does not look for the workflow and its result (fire and forget). Starting workflows in this way, starts all given workflows at the same time.

The optional `--wait` option starts the workflows in the same way, but also polls the status of a workflow until it is finished. In case of an error of a workflow, the next workflow is not started.



??? info "Options"
    ```text

    -a, --all                       Execute all available workflows.
    --wait                          Wait until workflows are completed.
    --progress                      Wait until workflows are completed and show
                                    a progress bar.
    --polling-interval INTEGER RANGE
                                    How many seconds to wait between status
                                    polls. Status polls are cheap, so a higher
                                    polling interval is most likely not needed.
                                    [default: 1; 0<=x<=60]
    ```

## workflow io

Execute a workflow with file input/output.

```shell-session title="Usage"
$ cmemc workflow io [OPTIONS] WORKFLOW_ID
```




With this command, you can execute a workflow that uses replaceable datasets as input, output or for configuration. Use the input parameter to feed data into the workflow. Likewise, use output for retrieval of the workflow result. Workflows without a replaceable dataset will throw an error.

!!! note
    Regarding the input dataset configuration - the following rules apply: If autoconfig is enabled ('--autoconfig', the default), the dataset configuration is guessed. If autoconfig is disabled ('--no-autoconfig') and the type of the dataset file is the same as the replaceable dataset in the workflow, the configuration from this dataset is copied. If autoconfig is disabled and the type of the dataset file is different from the replaceable dataset in the workflow, the default config is used.




??? info "Options"
    ```text

    -i, --input FILE                From which file the input is taken. If the
                                    workflow has no defined variable input
                                    dataset, this option is not allowed.
    -o, --output FILE               To which file the result is written to. Use
                                    '-' in order to output the result to stdout.
                                    If the workflow has no defined variable
                                    output dataset, this option is not allowed.
                                    Please note that the io command will not
                                    warn you on overwriting existing output
                                    files.
    --input-mimetype [application/x-plugin-file|application/x-plugin-file|application/x-plugin-csv|application/x-plugin-json|application/x-plugin-xml|application/x-plugin-text|application/x-plugin-text|application/x-plugin-excel|application/x-plugin-multiCsv|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/json|application/xml|text/csv|application/octet-stream|guess]
                                    Which input format should be processed: If
                                    not given, cmemc will try to guess the mime
                                    type based on the file extension or will
                                    fail.
    --output-mimetype [application/x-plugin-file|application/x-plugin-file|application/x-plugin-csv|application/x-plugin-json|application/x-plugin-xml|application/x-plugin-text|application/x-plugin-text|application/x-plugin-excel|application/x-plugin-multiCsv|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/x-plugin-binaryFile|application/json|application/xml|application/n-triples|application/vnd.openxmlformats-officedocument.spreadsheetml.sheet|text/csv|application/octet-stream|guess]
                                    Which output format should be requested: If
                                    not given, cmemc will try to guess the mime
                                    type based on the file extension or will
                                    fail. In case of an output to stdout, a
                                    default mime type will be used (JSON).
    --autoconfig / --no-autoconfig  Setup auto configuration of input datasets,
                                    e.g. in order to process CSV files with
                                    semicolon- instead of comma-separation.
                                    [default: autoconfig]
    ```

## workflow list

List available workflow.

```shell-session title="Usage"
$ cmemc workflow list [OPTIONS]
```





??? info "Options"
    ```text

    --filter <TEXT TEXT>...  List workflows based on metadata. First parameter
                             --filter CHOICE can be one of ['io', 'project',
                             'regex', 'tag']. The second parameter is based on
                             CHOICE.
    --id-only                Lists only workflow identifier and no labels or
                             other metadata. This is useful for piping the IDs
                             into other commands.
    --raw                    Outputs raw JSON objects of workflow task search
                             API response.
    ```

## workflow status

Get status information of workflow(s).

```shell-session title="Usage"
$ cmemc workflow status [OPTIONS] [WORKFLOW_IDS]...
```





??? info "Options"
    ```text

    --project TEXT                  The project, from which you want to list the
                                    workflows. Project IDs can be listed with
                                    the 'project list' command.
    --raw                           Output raw JSON info.
    --filter [Idle|Not executed|Finished|Cancelled|Failed|Successful|Canceling|Running|Waiting]
                                    Show only workflows of a specific status.
    ```

## workflow open

Open a workflow in your browser.

```shell-session title="Usage"
$ cmemc workflow open WORKFLOW_ID
```





