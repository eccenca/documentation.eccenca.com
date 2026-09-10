---
title: "cmemc: Finding and Filtering Objects"
icon: material/filter-outline
tags:
  - cmemc
---
# Finding and Filtering Objects

## Introduction

Almost every `list` command in cmemc accepts a `--filter` option, and the `inspect` commands accept a `--key` option.
Together they are the main tools to narrow down what cmemc shows you, which becomes essential as soon as an instance holds more than a handful of graphs, projects or datasets.

This page describes how these options work in general.
The [Command Reference](../command-reference/index.md) documents which options a concrete command supports.

!!! info

    This page is about **finding** the objects you are interested in.
    For getting the result into another program - as identifiers, as JSON, or as a single value - refer to [Scripting with cmemc](../scripting-with-cmemc/index.md).

## The filter grammar

The `--filter` option takes **two** parameters: a filter name and a value.

``` shell title="list only writeable graphs"
cmemc graph list --filter access writeable
```

This is a common source of confusion, since many other command line tools expect a single `name=value` parameter instead.
In cmemc, filter name and value are two separate parameters, so they are separated by a space.

## Filter names depend on the command

There is no global set of filter names.
Each command provides the filters which make sense for the objects it lists, so `graph list` and `dataset list` accept completely different filter names.

The quickest way to see the available filter names of a command is to provide an invalid one:

``` shell-session title="cmemc lists the valid filter names in the error message"
$ cmemc graph list --filter nonsense value
Usage: cmemc graph list [OPTIONS]
Try 'cmemc graph list --help' for help.

Error: Invalid filter name - use one of access, imported-by, iris
```

The following table gives an impression of how different these name sets are:

| Command | Filter names |
| ------- | ------------ |
| `graph list` | `access`, `imported-by`, `iris` |
| `project list` | `ids`, `regex`, `tag` |
| `dataset list` | `project`, `regex`, `type`, `tag`, `ids`, `combinedIds` |
| `workflow list` | `io`, `project`, `regex`, `tag` |
| `query list` | `id`, `type`, `placeholder`, `regex`, `ids` |

!!! tip

    With [command-line completion](../configuration/completion-setup/index.md) enabled, you do not need to remember any of this.
    Pressing ++tab++ after `--filter` offers the filter names of the current command, and pressing ++tab++ again often completes the values as well, taken live from your Corporate Memory instance.

## Combining filters

The `--filter` option can be given more than once.
The filters are then combined, so only objects which match **all** given filters are listed.

``` shell-session title="datasets of a project which also carry a specific tag"
$ cmemc dataset list \
  --filter project crm-graph \
  --filter tag velocity-daily
```

Most filter values are matched exactly.
The `regex` filter, which is available on several commands, is the exception and matches the object label or identifier against a regular expression.

## Inspecting a single object

While `list` commands give you an overview, the `inspect` commands output the metadata of a single object as a Key/Value table.

``` shell-session title="all metadata of a dataset"
$ cmemc dataset inspect my-project:my-dataset
```

Such a table can be long, so the `inspect` commands - as well as `admin status` - accept a `--key` option to reduce it:

- Given a **complete key**, cmemc outputs the plain value without any table decoration.
- Given a **prefix of several keys**, the table is reduced to the matching keys.
- Given the special value `all`, the complete table is output.

``` shell-session title="a single value, without table decoration"
$ cmemc admin status --key store.version
GraphDB/11.4.1 RDF4J/12
```

Since a plain value is easy to process further, this is the recommended way to fetch single pieces of metadata in scripts.
Refer to [Scripting with cmemc](../scripting-with-cmemc/index.md#capturing-a-single-value) for how to use this in a shell variable.

!!! warning

    `--key` and `--raw` can not be combined.
    Up to cmemc v26.1, `--key` was silently ignored when both options were given; since v26.2 this combination results in an error.

## Where to go from here

- [Scripting with cmemc](../scripting-with-cmemc/index.md) - how to get identifiers, JSON and single values out of cmemc.
- [Command-Line Completion](../configuration/completion-setup/index.md) - how to avoid typing filter names and values at all.
- [Command Reference](../command-reference/index.md) - the options of each concrete command.
