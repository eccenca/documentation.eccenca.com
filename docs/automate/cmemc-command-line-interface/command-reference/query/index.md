---
title: "cmemc: Command Group - query"
description: "List, execute, get status or open SPARQL queries."
icon: eccenca/application-queries
tags:
  - SPARQL
  - cmemc
---
# query Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, execute, get status or open SPARQL queries.

Queries are identified either by a file path, a URI from the query catalog or a shortened URI (qname, using a default namespace).

One or more queries can be executed one after the other with the execute command. With open command you can jump to the query editor in your browser.

Queries can use a mustache like syntax to specify placeholder for parameter values (e.g. `{{resourceUri}}`). These parameter values need to be given as well, before the query can be executed (use the`-p` option).

!!! note
    In order to get a list of queries from the query catalog, execute the `query list` command or use tab-completion.

## query execute

Execute queries which are loaded from files or the query catalog.

```shell-session title="Usage"
cmemc query execute [OPTIONS] QUERIES...
```

Queries are identified either by a file path, a URI from the query catalog, or a shortened URI (qname, using a default namespace).

If multiple queries are executed one after the other, the first failing query stops the whole execution chain.

Limitations: All optional parameters (e.g. accept, base64, ...) are provided for ALL queries in an execution chain. If you need different parameters for each query in a chain, run cmemc multiple times and use the logical operators && and || of your shell instead.

??? info "Options"
    ```text

    --catalog-graph TEXT            The used query catalog graph.  [default:
                                    https://ns.eccenca.com/data/queries/]
    --accept TEXT                   Accept header for the HTTP request(s).
                                    Setting this to 'default' means that cmemc
                                    uses an appropriate output for terminals.
                                    [default: default]
    --no-imports                    Graphs which include other graphs (using
                                    owl:imports) will be queried as merged
                                    overall-graph. This flag disables this
                                    default behaviour. The flag has no effect on
                                    update queries.
    --base64                        Enables base64 encoding of the query
                                    parameter for the SPARQL requests (the
                                    response is not touched). This can be useful
                                    in case there is an aggressive firewall
                                    between cmemc and Corporate Memory.
    -p, --parameter <TEXT TEXT>...  In case of a parameterized query
                                    (placeholders with the '{{key}}' syntax),
                                    this option fills all placeholder with a
                                    given value before the query is
                                    executed.Pairs of placeholder/value need to
                                    be given as a tuple 'KEY VALUE'. A key can
                                    be used only once.
    --limit INTEGER                 Override or set the LIMIT in the executed
                                    SELECT query. Note that this option will
                                    never give you more results than the LIMIT
                                    given in the query itself.
    --offset INTEGER                Override or set the OFFSET in the executed
                                    SELECT query.
    --distinct                      Override the SELECT query by make the result
                                    set DISTINCT.
    --timeout INTEGER               Set max execution time for query evaluation
                                    (in milliseconds).
    ```

## query list

List available queries from the catalog.

```shell-session title="Usage"
cmemc query list [OPTIONS]
```

Outputs a list of query URIs which can be used as reference for the query execute command.

??? info "Options"
    ```text

    --catalog-graph TEXT  The used query catalog graph.  [default:
                          https://ns.eccenca.com/data/queries/]
    --id-only             Lists only query identifier and no labels or other
                          metadata. This is useful for piping the ids into other
                          cmemc commands.
    ```

## query open

Open queries in the editor of the query catalog in your browser.

```shell-session title="Usage"
cmemc query open [OPTIONS] QUERIES...
```

With this command, you can open (remote) queries from the query catalog in the query editor in your browser (e.g. in order to change them). You can also load local query files into the query editor, in order to import them into the query catalog.

The command accepts multiple query URIs or files which results in opening multiple browser tabs.

??? info "Options"
    ```text

    --catalog-graph TEXT  The used query catalog graph.  [default:
                          https://ns.eccenca.com/data/queries/]
    ```

## query status

Get status information of executed and running queries.

```shell-session title="Usage"
cmemc query status [OPTIONS] [QUERY_ID]
```

With this command, you can access the latest executed SPARQL queries on the Explore backend (DataPlatform). These queries are identified by UUIDs and listed ordered by starting timestamp.

You can filter queries based on status and runtime in order to investigate slow queries. In addition to that, you can get the details of a specific query by using the ID as a parameter.

??? info "Options"
    ```text

    --id-only                Lists only query identifier and no labels or other
                             metadata. This is useful for piping the ids into
                             other cmemc commands.
    --raw                    Outputs raw JSON response of the query status API.
    --filter <TEXT TEXT>...  Filter queries by one of the following filter names
                             and a corresponding value: status, type, trace-id,
                             user, graph, slower-than, regex.
    ```

## query replay

Re-execute queries from a replay file.

```shell-session title="Usage"
cmemc query replay [OPTIONS] REPLAY_FILE
```

This command reads a `REPLAY_FILE` and re-executes the logged queries. A `REPLAY_FILE` is a JSON document which is an array of JSON objects with at least a key `queryString` holding the query text OR a key `iri` holding the IRI of the query in the query catalog. It can be created with the `query status` command.

```shell-session title="Example"
query status --raw > replay.json
```

The output of this command shows basic query execution statistics.

The queries are executed one after another in the order given in the input `REPLAY_FILE`. Query placeholders / parameters are ignored. If a query results in an error, the duration is not counted.

The optional output file is the same JSON document which is used as input, but each query object is annotated with an additional `replays` object, which is an array of JSON objects which hold values for the replay|loop|run IDs, start and end time as well as duration and other data.

??? info "Options"
    ```text

    --raw               Output the execution statistic as raw JSON.
    --loops INTEGER     Number of loops to run the replay file.  [default: 1]
    --wait INTEGER      Number of seconds to wait between query executions.
                        [default: 0]
    --output-file FILE  Save the optional output to this file. Input and output
                        of the command can be the same file. The output is
                        written at the end of a successful command execution.
                        The output can be stdout ('-') - in this case, the
                        execution statistic output is oppressed.
    --run-label TEXT    Optional label of this replay run.
    ```

## query cancel

Cancel a running query.

```shell-session title="Usage"
cmemc query cancel QUERY_ID
```

With this command, you can cancel a running query. Depending on the backend triple store, this will result in a broken result stream (stardog, neptune and virtuoso) or a valid result stream with incomplete results (graphdb)
