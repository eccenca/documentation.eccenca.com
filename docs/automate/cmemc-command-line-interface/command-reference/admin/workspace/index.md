---
title: "cmemc: Command Group - admin workspace"
description: "Import, export and reload the project workspace."
icon: material/folder-multiple-outline
tags:
  - cmemc
---

# admin workspace Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Import, export and reload the project workspace.

## admin workspace export

Export the complete workspace (all projects) to a ZIP file.

```shell-session title="Usage"
$ cmemc admin workspace export [OPTIONS] [FILE]
```

Depending on the requested export type, this ZIP file contains either one Turtle file per project (type `rdfTurtle`) or a substructure of resource files and XML descriptions (type `xmlZip`).

The file name is optional and will be generated with by the template if absent.

??? info "Options"
    ```text

    --replace                     Replace existing files. This is a dangerous
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

```shell-session title="Usage"
cmemc admin workspace import [OPTIONS] FILE
```

??? info "Options"
    ```text

    --type TEXT  Type of the exported workspace file.  [default: xmlZip]
    ```

## admin workspace reload

Reload the workspace from the backend.

```shell-session title="Usage"
cmemc admin workspace reload
```

