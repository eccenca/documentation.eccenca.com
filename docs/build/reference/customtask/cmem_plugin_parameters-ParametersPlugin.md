---
title: "Set or Overwrite parameters"
description: "Connect this task to a config port of another task in order to set or overwrite the parameter values of this task."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Set or Overwrite parameters
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

Connect this task to a config port of another task in order to set
or overwrite the parameter values of this task.

To configure this task, add one `key: value` pair per line to the Parameter
Configuration multiline field (YAML syntax). `key` is the ID of the parameter
you want to set or update, `value` is the new value to set.

You can also use multiline values with `|`
(be aware of the correct indentation with spaces, not tabs).

Example parameter configuration:

```
url: http://example.org
method: GET
query: |
    SELECT ?s
    WHERE {{
      ?s ?p ?o
    }}
execute_once: True
limit: 5

```


## Parameter

### Parameter Configuration

Your parameter configuration in YAML Syntax. One 'parameter: value' pair per line. url: http://example.org method: GET query: | SELECT ?s WHERE {{ ?s ?p ?o }} execute_once: True limit: 5

- ID: `parameters`
- Datatype: `code-yaml`
- Default Value:
``` yaml
url: http://example.org
method: GET
query: |
    SELECT ?s
    WHERE {{
      ?s ?p ?o
    }}
execute_once: True
limit: 5

```





## Advanced Parameter

`None`