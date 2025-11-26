---
title: "cmemc: Command Group - graph insights"
description: "List, create, delete and inspect graph insight snapshots."
icon: eccenca/graph-insights
tags:
  - cmemc
---
# graph insights Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, create, delete and inspect graph insight snapshots.

Graph Insight Snapshots are identified by an ID. To get a list of existing snapshots, execute the `graph insights list` command or use tab-completion.


## graph insights list

List graph insight snapshots.

```shell-session title="Usage"
$ cmemc graph insights list [OPTIONS]
```




Graph Insights Snapshots are identified by an ID.



??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter insight snapshots by one of the following
                             filter names and a corresponding value: id, main-
                             graph, status, affected-graph, valid.
    --raw                    Outputs raw JSON response.
    --id-only                Return the snapshot IDs only. This is useful for
                             piping the IDs into other commands.
    ```

## graph insights delete

Delete a graph insight snapshot.

```shell-session title="Usage"
$ cmemc graph insights delete [OPTIONS] [SNAPSHOT_ID]
```




Graph Insight Snapshots are identified by an ID. To get a list of existing snapshots, execute the `graph insights list` command or use tab-completion.



??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter insight snapshots by one of the following
                             filter names and a corresponding value: id, main-
                             graph, status, affected-graph, valid.
    -a, --all                Delete all snapshots.
    ```

## graph insights create

Create or update a graph insight snapshot.

```shell-session title="Usage"
$ cmemc graph insights create [OPTIONS] IRI
```




Create a graph insight snapshot for a given graph. If the snapshot already exists, it is hot-swapped after re-creation. The snapshot contains only the (imported) graphs the requesting user can read.



??? info "Options"
    ```text

    --wait                          Wait until snapshot creation is done.
    --polling-interval INTEGER RANGE
                                    How many seconds to wait between status
                                    polls. Status polls are cheap, so a higher
                                    polling interval is most likely not needed.
                                    [default: 1; 0<=x<=60]
    ```

## graph insights update

Update a graph insight snapshot.

```shell-session title="Usage"
$ cmemc graph insights update [OPTIONS] [SNAPSHOT_ID]
```




After the update, the snapshot is hot-swapped.



??? info "Options"
    ```text

    --filter <TEXT TEXT>...         Filter insight snapshots by one of the
                                    following filter names and a corresponding
                                    value: id, main-graph, status, affected-
                                    graph, valid.
    -a, --all                       Delete all snapshots.
    --wait                          Wait until snapshot creation is done.
    --polling-interval INTEGER RANGE
                                    How many seconds to wait between status
                                    polls. Status polls are cheap, so a higher
                                    polling interval is most likely not needed.
                                    [default: 1; 0<=x<=60]
    ```

## graph insights inspect

Inspect the metadata of a graph insight snapshot.

```shell-session title="Usage"
$ cmemc graph insights inspect [OPTIONS] SNAPSHOT_ID
```





??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

