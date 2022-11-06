---
title: "cmemc: Command Group - graph"
description: "List, import, export, delete, count, tree or open graphs."
icon: material/semantic-web
tags:
  - KnowledgeGraph
  - cmemc
---
# graph Command Group

List, import, export, delete, count, tree or open graphs.

Graphs are identified by an IRI. The get a list of existing graphs,
execute the list command or use tab-completion.

## graph count

Count triples in graph(s).

This command lists graphs with their triple count.
Counts are done without following imported graphs.

```shell-session
$ cmemc graph count [OPTIONS] [IRIS]...
```

```text
Usage: cmemc graph count [OPTIONS] [IRIS]...

  Count triples in graph(s).

  This command lists graphs with their triple count. Counts are done without
  following imported graphs.

Options:
  -a, --all        Count all graphs
  -s, --summarize  Display only a sum of all counted graphs together
```
## graph tree

Show graph tree(s) of the owl:imports hierarchy.

You can can output one or more trees of the import hierarchy.

Imported graphs which do not exists are shown as [missing: IRI].
Imported graphs which will result in an import cycle are shown as
[ignored: IRI].
Each graph is shown with label and IRI.

```shell-session
$ cmemc graph tree [OPTIONS] [IRIS]...
```

```text
Usage: cmemc graph tree [OPTIONS] [IRIS]...

  Show graph tree(s) of the owl:imports hierarchy.

  You can can output one or more trees of the import hierarchy.

  Imported graphs which do not exists are shown as [missing: IRI]. Imported
  graphs which will result in an import cycle are shown as [ignored: IRI].
  Each graph is shown with label and IRI.

Options:
  -a, --all   Show tree of all (readable) graphs.
  --raw       Outputs raw JSON of the graph importTree API response.
  --id-only   Lists only graph identifier (IRIs) and no labels or other meta
              data. This is useful for piping the IRIs into other commands.
              The output with this option is a sorted, flat, de-duplicated
              list of existing graphs.
```
## graph list

List accessible graphs.

```shell-session
$ cmemc graph list [OPTIONS]
```

```text
Usage: cmemc graph list [OPTIONS]

  List accessible graphs.

Options:
  --raw                      Outputs raw JSON of the graphs list API response.
  --id-only                  Lists only graph identifier (IRIs) and no labels
                             or other meta data. This is useful for piping the
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

In case of file export, data from all selected graphs will be concatenated
in one file.
In case of directory export, .graph and .ttl files will be created
for each graph.

```shell-session
$ cmemc graph export [OPTIONS] [IRIS]...
```

```text
Usage: cmemc graph export [OPTIONS] [IRIS]...

  Export graph(s) as NTriples to stdout (-), file or directory.

  In case of file export, data from all selected graphs will be concatenated
  in one file. In case of directory export, .graph and .ttl files will be
  created for each graph.

Options:
  -a, --all                       Export all readable graphs.
  --include-imports               Export selected graph(s) and all graphs
                                  which are imported from these selected
                                  graph(s).

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

  --mime-type [application/n-triples|text/turtle]
                                  Define the requested mime type  [default:
                                  application/n-triples]
```
## graph delete

Delete graph(s) from the store.

```shell-session
$ cmemc graph delete [OPTIONS] [IRIS]...
```

```text
Usage: cmemc graph delete [OPTIONS] [IRIS]...

  Delete graph(s) from the store.

Options:
  -a, --all          Delete all writeable graphs.
  --include-imports  Delete selected graph(s) and all writeable graphs which
                     are imported from these selected graph(s).
```
## graph import

Import graph(s) to the store.

If input is an directory, it scans for file-pairs such as xxx.ttl and
xxx.ttl.graph where xxx.ttl is the actual triples file and xxx.ttl.graph
contains the graph IRI as one string: "https://mygraph.de/xxx/".
If input is a file, content will be uploaded to IRI.
If --replace is set, the data will be overwritten,
if not, it will be added.

```shell-session
$ cmemc graph import [OPTIONS] INPUT_PATH [IRI]
```

```text
Usage: cmemc graph import [OPTIONS] INPUT_PATH [IRI]

  Import graph(s) to the store.

  If input is an directory, it scans for file-pairs such as xxx.ttl and
  xxx.ttl.graph where xxx.ttl is the actual triples file and xxx.ttl.graph
  contains the graph IRI as one string: "https://mygraph.de/xxx/". If input
  is a file, content will be uploaded to IRI. If --replace is set, the data
  will be overwritten, if not, it will be added.

Options:
  --replace        Replace / overwrite the graph - instead of just adding new
                   triples the graph.

  --skip-existing  Skip importing a file if the target graph already exists in
                   the store. Note that the graph list is fetched once at the
                   beginning of the process, so that you can still add
                   multiple files to one single graph (if it does not exist).
```
## graph open

Open / explore a graph in the browser.

```shell-session
$ cmemc graph open [OPTIONS] IRI
```

```text
Usage: cmemc graph open [OPTIONS] IRI

  Open / explore a graph in the browser.
```
