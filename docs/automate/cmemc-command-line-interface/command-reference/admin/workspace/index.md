---
title: "cmemc: Command Group - admin workspace"
description: "Import, export and reload the project workspace."
icon: octicons/project-24
tags:
  - cmemc
---
# admin workspace Command Group

Import, export and reload the project workspace.

## admin workspace export

Export the complete workspace (all projects) to a ZIP file.

Depending on the requested type, this ZIP contains either a turtle file
for each project (type rdfTurtle) or a substructure of resource files and
XML descriptions (type xmlZip).

The file name is optional and will be generated with by
the template if absent.

```shell-session
$ cmemc admin workspace export [OPTIONS] [FILE]
```

```text
Usage: cmemc admin workspace export [OPTIONS] [FILE]

  Export the complete workspace (all projects) to a ZIP file.

  Depending on the requested type, this ZIP contains either a turtle file
  for each project (type rdfTurtle) or a substructure of resource files and
  XML descriptions (type xmlZip).

  The file name is optional and will be generated with by the template if
  absent.

Options:
  -o, --overwrite               Overwrite existing files. This is a dangerous
                                option, so use it with care.

  --type TEXT                   Type of the exported workspace file.
                                [default: xmlZip]

  -t, --filename-template TEXT  Template for the export file name. Possible
                                placeholders are (Jinja2): {{connection}}
                                (from the --connection option) and {{date}}
                                (the current date as YYYY-MM-DD). The file
                                suffix will be appended. Needed directories
                                will be created.  [default:
                                {{date}}-{{connection}}.workspace]
```
## admin workspace import

Import the workspace from a file.

```shell-session
$ cmemc admin workspace import [OPTIONS] FILE
```

```text
Usage: cmemc admin workspace import [OPTIONS] FILE

  Import the workspace from a file.

Options:
  --type TEXT  Type of the exported workspace file.  [default: xmlZip]
```
## admin workspace reload

Reload the workspace from the backend.

```shell-session
$ cmemc admin workspace reload [OPTIONS]
```

```text
Usage: cmemc admin workspace reload [OPTIONS]

  Reload the workspace from the backend.
```
