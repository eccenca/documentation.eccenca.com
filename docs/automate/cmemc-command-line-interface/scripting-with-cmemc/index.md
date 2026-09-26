---
title: "cmemc: Scripting with cmemc"
icon: material/script-text-outline
tags:
  - Automate
  - cmemc
---
# Scripting with cmemc

## Introduction

By default, cmemc formats its output for humans: tables with headers, borders and a caption which names the instance you are working on.
This is convenient in a terminal but unsuitable as input for another program.

This page describes how to get machine-readable output out of cmemc, how to feed the output of one command into the next, and how cmemc signals failure to a calling process such as a CI pipeline.

!!! info

    This page is about **processing** what cmemc outputs.
    For narrowing down *which* objects a command outputs in the first place, refer to [Finding and Filtering Objects](../finding-and-filtering-objects/index.md).

## Identifiers only

Most `list` commands support the `--id-only` option, which suppresses labels, metadata and table decoration and outputs one identifier per line.
This is the format you want whenever the result is consumed by another command.

``` shell-session title="plain identifiers, one per line"
$ cmemc graph list --id-only
http://di.eccenca.com/project/ttt_7fba644a0fdeed82
https://ns.eccenca.com/data/ac/
https://ns.eccenca.com/data/config/
```

Since most commands accept multiple identifiers as parameters, such a list can be piped directly into another cmemc command:

``` shell-session title="count the triples of all accessible graphs"
$ cmemc graph list --id-only | xargs cmemc graph count
25 http://di.eccenca.com/project/ttt_7fba644a0fdeed82
90 https://ns.eccenca.com/data/ac/
4 https://ns.eccenca.com/data/config/
```

Combining `--id-only` with `--filter` is the basic building block of most cmemc automation: select the objects you want, then act on them.

!!! warning

    Commands which change data (such as `graph delete` or `project delete`) accept piped identifiers just as readily.
    Run the `list` part of your pipeline on its own first, and only then append the command which does the modification.

## JSON output

The `--raw` option is available on more than 40 commands and outputs the JSON as it was received from the eccenca Corporate Memory APIs.
Together with a tool such as [jq](https://jqlang.github.io/jq/), this allows for arbitrary post-processing:

``` shell-session title="IRIs of all writeable graphs"
$ cmemc graph list --raw | jq -r '.[] | select(.writeable) | .iri'
https://ns.eccenca.com/data/userinfo/
http://di.eccenca.com/project/ttt_7fba644a0fdeed82
https://ns.eccenca.com/data/queries/
```

!!! warning "Raw output is an API response, not a stable contract"

    `--raw` hands you what the backend sent.
    Fields can be added, and the type of a field can change between Corporate Memory releases.
    In `workflow status --raw` for example, `startTime` is an ISO-8601 timestamp while `lastUpdateTime` is given in milliseconds since the epoch - and `startTime` used to be given in milliseconds as well.

    Address fields by name, tolerate additional fields, and avoid assuming that a value keeps its type across an upgrade.
    Where a command offers a dedicated option for what you need (such as `--id-only` or `--key`), prefer it over parsing `--raw`.

## Capturing a single value

For a single piece of metadata, the `--key` option of the `inspect` commands is more robust than parsing JSON.
Given a complete key, cmemc outputs the plain value without any table decoration, which makes it directly usable in a shell variable:

``` shell-session title="store version into a shell variable"
$ STORE=$(cmemc admin status --key store.version)
$ echo "$STORE"
GraphDB/11.4.1 RDF4J/12
```

The `--key` option is described in detail in [Finding and Filtering Objects](../finding-and-filtering-objects/index.md#inspecting-a-single-object).

## Reproducible output

Table output adapts to the width of your terminal, which means the same command can produce differently wrapped output on your machine and on a build runner.
Set `CMEMC_CONSOLE_WIDTH` to pin the width and get identical output everywhere:

``` shell-session
export CMEMC_CONSOLE_WIDTH=100
```

In addition to that, the `--quiet` / `-q` option suppresses all non-error info messages, so progress output such as `Export project 1/1: ... done` does not end up in your logs.

## Exit codes

cmemc uses two exit codes:

| Code | Meaning |
| ---- | ------- |
| `0` | The command completed successfully. |
| `1` | The command failed. The error message is written to `stderr`. |

``` shell-session title="a failing command exits with 1"
$ cmemc project export does-not-exist
Project does-not-exist does not exist.
$ echo $?
1
```

Because of this, a shell with `set -e` stops at the first failing cmemc command, and a CI job fails without further configuration.
The same applies when several identifiers are given to one command: `workflow execute --wait` stops the chain as soon as one workflow fails.

### Turning findings into failures

Some commands complete successfully but report findings, for example a validation which produced violations, or a project which has task loading errors.
By default such findings do not change the exit code.
The `--exit-1` option makes these commands fail on findings, which is what you usually want in a pipeline:

| Command | Values | Default |
| ------- | ------ | ------- |
| `admin status --exit-1` | `never`, `error`, `always` | `never` |
| `graph validation export --exit-1` | `never`, `error` | `error` |
| `project status --exit-1` | flag, no value | off |

``` shell title="fail the pipeline if any project has task loading errors"
cmemc project status --all --exit-1
```

!!! note

    The three commands above use the same option name with different value sets and different defaults.
    Check the `--help` screen of the concrete command before relying on a specific behaviour.

For `admin status`, note that `always` does not mean "always exit 1" - it means "exit 1 on errors **and** warnings", while `error` ignores warnings.
On a healthy instance, all three values result in exit code `0`.

## Debugging failing automation

When a command fails inside a pipeline, `--debug` outputs the configuration resolution, the HTTP conversation and a full stack trace after errors:

``` shell-session
cmemc --debug graph list
```

The verbosity of the client log can be adjusted with `--log-level` (one of `trace`, `debug`, `info`, `warning`, `error`, `critical`, defaults to `debug`).
Both options can be set for a whole session using the `CMEMC_DEBUG` and `CMEMC_LOG_LEVEL` [environment variables](../configuration/environment-based-configuration/index.md).

!!! tip

    Debug output contains URLs, configuration keys and header names of your deployment.
    Secrets are not printed as values, but treat debug logs from CI jobs as sensitive nonetheless.

## Configuring cmemc from the calling process

Scripts rarely want to repeat `--connection` on every command.
All top level options, as well as the options of individual commands, can be preset with environment variables:

``` shell-session
export CMEMC_CONNECTION=my-cmem
export CMEMC_GRAPH_LIST_ID_ONLY=true
```

Refer to [Environment-based Configuration](../configuration/environment-based-configuration/index.md) for the naming scheme and the complete list of top level variables, and to [Getting Credentials from external Processes](../configuration/getting-credentials-from-external-processes/index.md) for keeping credentials out of your repository.

## Where to go from here

- [Workflow Execution and Orchestration](../workflow-execution-and-orchestration/index.md) - a complete example script which starts workflows in parallel and waits for the results.
- [Backup and Restore](../backup-and-restore/index.md) - creating and restoring backup artifacts with cmemc.
- [Using Gitlab Pipelines](../invocation/gitlab-pipeline/index.md) and [Using Github Actions](../invocation/github-action/index.md) - running cmemc on a build server.
