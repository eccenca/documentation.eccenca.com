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
    --wait                          Wait until all executed workflows are
                                    completed.
  
    --polling-interval INTEGER RANGE
                                    How many seconds to wait between status
                                    polls. Status polls are cheap, so a higher
                                    polling interval is most likely not needed.
                                    [default: 1]
    ```

## workflow io

Execute a workflow with file input/output.

```shell-session title="Usage"
$ cmemc workflow io [OPTIONS] WORKFLOW_ID
```




With this command, you can execute a workflow that uses variable datasets as input, output or for configuration. Use the input parameter to feed data into the workflow. Likewise, use output for retrieval of the workflow result. Workflows without a variable dataset will throw an error.



??? info "Options"
    ```text

    -i, --input FILE                From which file the input is taken: note
                                    that the maximum file size to upload is
                                    limited to a server configured value. If the
                                    workflow has no defined variable input
                                    dataset, this can be ignored.
  
    -o, --output FILE               To which file the result is written to: use
                                    '-' in order to output the result to stdout.
                                    If the workflow has no defined variable
                                    output dataset, this can be ignored. Please
                                    note that the io command will not warn you
                                    on overwriting existing output files.
  
    --input-mimetype [guess|application/xml|application/json|text/csv]
                                    Which input format should be processed: If
                                    not given, cmemc will try to guess the mime
                                    type based on the file extension or will
                                    fail
  
    --output-mimetype [guess|application/xml|application/json|application/n-triples|application/vnd.openxmlformats-officedocument.spreadsheetml.sheet|text/csv]
                                    Which output format should be requested: If
                                    not given, cmemc will try to guess the mime
                                    type based on the file extension or will
                                    fail. In case of an output to stdout, a
                                    default mime type will be used (currently
                                    xml).
  
    --autoconfig / --no-autoconfig  Setup auto configuration of input datasets,
                                    e.g. in order to process CSV files with
                                    semicolon- instead of comma-separation.
                                    [default: True]
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





