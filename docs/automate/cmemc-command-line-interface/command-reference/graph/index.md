---
title: "cmemc: Command Group - graph"
description: "List, import, export, delete, count, tree or open graphs."
icon: eccenca/artefact-dataset-eccencadataplatform
tags:
  - KnowledgeGraph
  - cmemc
---

# graph Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, import, export, delete, count, tree or open graphs.

Graphs are identified by an IRI.

!!! note
    The get a list of existing graphs, execute the `graph list` command or use tab-completion.

## graph count

Count triples in graph(s).

```shell-session title="Usage"
cmemc graph count [OPTIONS] [IRIS]...
```

This command lists graphs with their triple count. Counts do not include imported graphs.

??? info "Options"
    ```text

    -a, --all        Count all graphs
    -s, --summarize  Display only a sum of all counted graphs together
    ```

## graph tree

(Hidden) Deprecated: use 'graph imports tree' instead.

```shell-session title="Usage"
cmemc graph tree [OPTIONS] [IRIS]...
```

??? info "Options"
    ```text

    -a, --all   Show tree of all (readable) graphs.
    --raw       Outputs raw JSON of the graph importTree API response.
    --id-only   Lists only graph identifier (IRIs) and no labels or other
                metadata. This is useful for piping the IRIs into other
                commands. The output with this option is a sorted, flat, de-
                duplicated list of existing graphs.
    ```

## graph list

List accessible graphs.

```shell-session title="Usage"
cmemc graph list [OPTIONS]
```

??? info "Options"
    ```text

    --raw                      Outputs raw JSON of the graphs list API response.
    --id-only                  Lists only graph identifier (IRIs) and no labels
                               or other metadata. This is useful for piping the
                               IRIs into other commands.
    --filter <CHOICE TEXT>...  Filter graphs based on effective access
                               conditions or import closure. First parameter
                               CHOICE can be 'access' or 'imported-by'. The
                               second parameter can be 'readonly' or 'writeable'
                               in case of 'access' or any readable graph in case
                               of 'imported-by'.
    ```

## graph export

Export graph(s) as NTriples to stdout (-), file or directory.

```shell-session title="Usage"
cmemc graph export [OPTIONS] [IRIS]...
```

In case of file export, data from all selected graphs will be concatenated in one file. In case of directory export, .graph and .ttl files will be created for each graph.

??? info "Options"
    ```text

    -a, --all                       Export all readable graphs.
    --include-imports               Export selected graph(s) and all graphs
                                    which are imported from these selected
                                    graph(s).
    --include-import-statements     Save graph imports information from other
                                    graphs to the exported graphs and write
                                    *.imports files.
    --create-catalog                In addition to the .ttl and .graph files,
                                    cmemc will create an XML catalog file
                                    (catalog-v001.xml) which can be used by
                                    applications such as Protégé.
    --output-dir DIRECTORY          Export to this directory.
    --output-file FILE              Export to this file.  [default: -]
    -t, --filename-template TEXT    Template for the export file name(s). Used
                                    together with --output-dir. Possible
                                    placeholders are (Jinja2): {{hash}} - sha256
                                    hash of the graph IRI, {{iriname}} - graph
                                    IRI converted to filename, {{connection}} -
                                    from the --connection option and {{date}} -
                                    the current date as YYYY-MM-DD. The file
                                    suffix will be appended. Needed directories
                                    will be created.  [default: {{hash}}]
    --mime-type [application/n-triples|text/turtle|application/rdf+xml]
                                    Define the requested mime type  [default:
                                    text/turtle]
    --compress [gzip]               Compress the exported graph files.
    ```

## graph delete

Delete graph(s) from the store.

```shell-session title="Usage"
cmemc graph delete [OPTIONS] [IRIS]...
```

??? info "Options"
    ```text

    -a, --all                    Delete all writeable graphs.
    --include-imports            Delete selected graph(s) and all writeable
                                 graphs which are imported from these selected
                                 graph(s).
    --include-import-statements  Delete import reference of deleted graphs
    ```

## graph import

Import graph(s) to the store.

```shell-session title="Usage"
cmemc graph import [OPTIONS] INPUT_PATH [IRI]
```

If input is a file, content will be uploaded to the graph identified with the IRI.

If input is a directory and NO IRI is given, it scans for file-pairs such as `xyz.ttl` and `xyz.ttl.graph`, where `xyz.ttl` is the actual triples file and `xyz.ttl.graph` contains the graph IRI in the first line: `https://mygraph.de/xyz/`.

If input is a directory AND a graph IRI is given, it scans for all `*.ttl` files in the directory and imports all content to the graph, ignoring the `*.ttl.graph` files.

If the ``--replace`` flag is set, the data in the graphs will be overwritten, if not, it will be added.

!!! note
    Directories are scanned on the first level only (not recursively).

??? info "Options"
    ```text

    --replace                    Replace / overwrite the graph(s), instead of
                                 just adding the triples to the graph.
    --skip-existing              Skip importing a file if the target graph
                                 already exists in the store. Note that the
                                 graph list is fetched once at the beginning of
                                 the process, so that you can still add multiple
                                 files to one single graph (if it does not
                                 exist).
    --include-import-statements  Use *.imports files to re-apply the graph
                                 imports of the imported graphs.
    ```

## graph open

Open / explore a graph in the browser.

```shell-session title="Usage"
cmemc graph open IRI
```
