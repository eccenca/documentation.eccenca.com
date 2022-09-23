---
tags:
  - cmemc
  - Workflow
---
# Workflow execution and orchestration

## Introduction

In some cases, you need to automate a complete graph of integration workflows, which depend on each other and can sometimes run in parallel or after each other.
Although cmemc is not a workflow orchestration tool, you can easily use it do some basic workflow orchestration.
This page describes how you can execute and orchestrate workflows together.
For simplicity all given examples do not select a specific connection (`--connection your-cmem`).
We simply assume that you selected your instance via an environment variable (`export CMEMC_CONNECTION=your-cmem`).

## Simple Execution

cmemc allows for execution of workflows with the `workflow execute` command.
To start a workflow, simply use this command:

``` shell-session title="workflow execute command"
$ cmemc workflow execute cmem:my-workflow
cmem:my-workflow ... Started
```

Workflow identifier can be extended with command-line completion on the command line but you can also get a list of workflows with the `workflow list` command:

``` shell-session title="workflow list command"
$ cmemc workflow list
cmem:my-workflow
cmem:second-workflow
```

The default working mode of the `workflow execute` command starts a workflow without waiting for a response.
In order to wait until the workflow is finished you need to use the `--wait` option:

``` shell-session title="workflow execute command with wait option"
$ cmemc workflow execute cmem:my-workflow --wait
cmem:my-workflow ... Started ... Finished (Finished in 32.931s, just now)
```

For a reference on the `workflow execute` command, have a look at the [Command Reference](../command-reference/index.md) or look at the command specific help (`cmemc workflow execute --help`).

## Retrieve Status Information

At any time, you can retrieve status information of a workflow with the `workflow status` command:

``` shell-session title="workflow status command"
$ cmemc workflow status cmem:my-workflow
cmem:my-workflow ... Finished (Finished in 32.931s, 4 minutes ago)
```

In addition to that, you can retrieve raw JSON data about a workflow, which can used for post-processing:

``` shell-session title="workflow status command with JSON output"
$ cmemc -workflow status cmem:my-workflow --raw
{
  "activity": "ExecuteLocalWorkflow",
  "runtime": 32931,
  "project": "cmem",
  "failed": false,
  "message": "Finished in 32.931s",
  "task": "my-workflow",
  "isRunning": false,
  "statusName": "Finished",
  "progress": 100,
  "cancelled": false,
  "startTime": 1593679211989,
  "exceptionMessage": null,
  "lastUpdateTime": 1593679244920
}
```

For a reference on the `workflow status` command, have a look at the [Command Reference](../command-reference/index.md)  or look at the command specific help (`cmemc workflow status --help`).

## Serial Execution

The `workflow execute` command is able to start multiple workflows in a chain, waiting for each of the workflow and exit if there is an error with one of the workflows.

To do this, use the `--wait` option and simply add more than one workflow identifier as parameter to the the command:

``` shell-session title="workflow execute command"
$ cmemc workflow execute cmem:my-workflow cmem:second-workflow --wait
cmem:my-workflow ... Started ... Finished (Finished in 30.984s, just now)
cmem:second-workflow ... Started ... Finished (Finished in 50.579s, just now)
```

!!! warning

    Starting these workflows in this way means that cmemc exits with an error code 1 in the moment the first workflow throws an error.
    All later workflows will not be executed.

## Parallel Execution

Sometimes you want to execute workflows in parallel, because they do not depend on each other and it can fasten up the overall runtime.

To do this, there is a little bit of extra scripting needed at the moment.
The main idea is, to start the parallel workflows without waiting and then poll the status information until they are not running anymore.

Here is an example script which does exactly this.

``` bash title="cmemc-parallel-workflows.sh"
#!/usr/bin/env bash
# @(#) Example: execute two workflows in parallel and wait for the results (exit 1 on failure)
# Use the unofficial bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail; export FS=$'\n\t'

# setup the used instance
export CMEMC_CONNECTION=your-cmem

# check SSL config
if [ "$(cmemc config get SSL_VERIFY 2>&1)" == True ]
then
    NUM=0
else
    NUM=1
fi

# start the given set of workflows
WORKFLOW_IDS="cmem:my-workflow cmem:second-workflow"
cmemc workflow execute $WORKFLOW_IDS

# loop until they are not running anymore
RUNNING=-1
until [ $RUNNING == $NUM ]
do
    # wait 5 seconds - polling time
    sleep 5
    # use the the filter option to show only running workflows
    RUNNING=$(cmemc workflow status $WORKFLOW_IDS --filter running 2>&1 | wc -l)
    if [ $RUNNING != $NUM ]; then
        echo "We still have $RUNNING running workflows ..."
    fi
done

# look for failed workflows
FAILED=$(cmemc workflow status $WORKFLOW_IDS --filter failed 2>&1 | wc -l)
if [ $FAILED != $NUM ]; then
    echo "Some workflows failed :-("
    exit 1
else
    echo "All workflows finished successfully :-)"
    exit 0
fi
```

