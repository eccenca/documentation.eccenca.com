---
title: "cmemc: Command Group - graph imports"
description: "List, create, delete and show graph imports."
icon: material/family-tree
tags:
  - KnowledgeGraph
  - cmemc
---
# graph imports Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, create, delete and show graph imports.

Graphs are identified by an IRI. Statement imports are managed by creating owl:imports statements such as '`FROM_GRAPH` owl:imports `TO_GRAPH`' in the `FROM_GRAPH`. All statements in the `TO_GRAPH` are then available in the `FROM_GRAPH`.

!!! note
    The get a list of existing graphs, execute the `graph list` command or use tab-completion.



## graph imports tree

Show graph tree(s) of the imports statement hierarchy.

```shell-session title="Usage"
$ cmemc graph imports tree [OPTIONS] [IRIS]...
```




You can output one or more trees of the import hierarchy.

Imported graphs which do not exist are shown as `[missing: IRI]`. Imported graphs which will result in an import cycle are shown as `[ignored: IRI]`. Each graph is shown with label and IRI.



??? info "Options"
    ```text

    -a, --all   Show tree of all (readable) graphs.
    --raw       Outputs raw JSON of the graph importTree API response.
    --id-only   Lists only graph identifier (IRIs) and no labels or other
                metadata. This is useful for piping the IRIs into other
                commands. The output with this option is a sorted, flat, de-
                duplicated list of existing graphs.
    ```

## graph imports list

List accessible graph imports statements.

```shell-session title="Usage"
$ cmemc graph imports list [OPTIONS]
```




Graphs are identified by an IRI. Statement imports are managed by creating owl:imports statements such as "`FROM_GRAPH` owl:imports `TO_GRAPH`" in the `FROM_GRAPH`. All statements in the `TO_GRAPH` are then available in the `FROM_GRAPH`.



??? info "Options"
    ```text

    --raw                    Outputs raw JSON response.
    --filter <TEXT TEXT>...  Filter imports by one of the following filter names
                             and a corresponding value: from-graph, to-graph.
    ```

## graph imports create

Add statement to import a TO_GRAPH into a FROM_GRAPH.

```shell-session title="Usage"
$ cmemc graph imports create FROM_GRAPH TO_GRAPH
```




Graphs are identified by an IRI. Statement imports are managed by creating owl:imports statements such as "`FROM_GRAPH` owl:imports `TO_GRAPH`" in the `FROM_GRAPH`. All statements in the `TO_GRAPH` are then available in the `FROM_GRAPH`.

!!! note
    The get a list of existing graphs, execute the `graph list` command or use tab-completion.




## graph imports delete

Delete statement to import a TO_GRAPH into a FROM_GRAPH.

```shell-session title="Usage"
$ cmemc graph imports delete FROM_GRAPH TO_GRAPH
```




Graphs are identified by an IRI. Statement imports are managed by creating owl:imports statements such as "`FROM_GRAPH` owl:imports `TO_GRAPH`" in the `FROM_GRAPH`. All statements in the `TO_GRAPH` are then available in the `FROM_GRAPH`.

!!! note
    The get a list of existing graph imports, execute the `graph imports list` command or use tab-completion.




