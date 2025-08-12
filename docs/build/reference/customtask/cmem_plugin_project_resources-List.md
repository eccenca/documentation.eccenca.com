---
title: "List project files"
description: "List file resources from the project."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# List project files
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

List file resources from the current project based on a regular expression.

The project-relative path of each file of the current project is tested against a given
regular expression.
The project resource is listed in the output, if the expression matches this path.
The output entities have the following paths:

- `name` - the plain file name of the resource (example: `file.txt`)
- `fullPath` - the project-relative path including directories but no leading slash
  (example: `directory/file.txt`)
- `modified` - modified timestamp (example: `2025-03-10T15:38:41.023Z`)
- `size` - size of the file in bytes (example: `123345`)

The regular expression has to match the `fullPath` of the file and is case sensitive.

Given this list of example files of a project:

```
dataset.csv
my-dataset.xml
json/example.json
json/example_new.json
json/data.xml
```

Here are some regular expressions with the expected result:

- The regex `dataset\.csv` lists only the first file.
- The regex `json/.*` lists all files in the `json` sub-directory.
- The regex `new` lists nothing.
- The regex `.*new.*` list the file `json/example_new.json`
(and all other files with `new` in the path)

We recommend to test your regular expression before using it.
[regex101.com](https://regex101.com) is a proper service to test your regular expressions.
[This deep-link](https://regex101.com/?testString=dataset.csv%0Amy-dataset.xml%0Ajson/example.json%0Ajson/example_new.json%0Ajson/data.xml&regex=.*new.*)
provides a test bed using the example files and the last expression from the list.


## Parameter

### File matching regex

The regex for filtering the file names. The regex needs to match the full path (i.e. from beginning to end, including sub-directories) in order for the file to be deleted.

- Datatype: `string`
- Default Value: `None`



