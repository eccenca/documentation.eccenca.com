---
status: new
icon: material/language-python
tags:
    - cmemc
    - Python
    - Automate
---
# cmemc - Python Scripts

## Introduction

As a more lightweight and fault-tolerant alternative to using cmempy directly, we recommend to call [cmemc commands](../../automate/cmemc-command-line-interface/command-reference/index.md) directly in your Python automation scripts.

The advantages of this approach are:

- You can test and use your calls in the command line before integrating them.
- You don't have to worry about internal details and have a well-documented and stable interface.
- Authorization is done in the same way, cmemc is doing this.

## Installation

cmemc is published as an Apache 2 licensed open source python package at [pypi.org](https://pypi.org/project/cmem-cmempy/), hence you are able to install it with a simple pip command:

``` shell
pip install cmem-cmemc
```


## Configure a connection

Assuming you have already [configured your cmemc connection](../../automate/cmemc-command-line-interface/configuration/file-based-configuration/index.md), using it in Python scripts is quite easy.

``` python
from os import environ

# use the cmemc connection
environ["CMEMC_CONNECTION"] = "my-dev-cmem"
```

This will tell cmemc to use the configured connection `my-dev-cmem`.

## Running commands

In order to execute a command and process the results, you can use this wrapper function:

``` python
import json

from click.testing import CliRunner

from cmem_cmemc.cli import cli


def cmemc(params: list[str]) -> str | list[str] | list[dict]:
    """Run a cmemc command and provide the output.

    When using the --raw option, output is a parsed list of dictionaries.
    When using the --id-only option, output is a parsed list of strings.
    Returns plain text output otherwise.

    Have a look at click API documentation for more options:
    https://click.palletsprojects.com/en/stable/api/#click.testing.CliRunner
    """
    result = CliRunner().invoke(cli, params)
    if result.exit_code != 0:
        raise RuntimeError(result.exception)
    output: str = result.stdout
    if "--id-only" in params:
        return output.splitlines()
    if "--raw" in params:
        return json.loads(output)
    return output
```

This function will use the configured connection to execute a command and return the result.
Please note that the output can bei either a multi-line string, a list of strings or a list of dictionaries.
This is because we made sure that `--raw` outputs JSON and `--id-only` only identifier.

As a last step, you can iterate and process the results:

``` python
# specify the command as a list of arguments - in this case: list all existing worflows
command = ["workflow", "list", "--raw"]

# iterate and process the output
for workflow in cmemc(command):
    project_id = workflow.get("projectId")
    workflow_id = workflow.get("id")
    print(f"Workflow '{workflow_id}' in '{project_id}'")
```

## Using a shebang to create an executable file

As a nice addon, you could extend your script with a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) to start [uv](https://docs.astral.sh/uv/).
This will also install and manage dependencies and python versions for you:

The complete script looks like this:

``` python
#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "cmem-cmemc",
# ]
# ///
import json
from os import environ

from click.testing import CliRunner

from cmem_cmemc.cli import cli


def cmemc(params: list[str]) -> str | list[str] | list[dict]:
    """Run a cmemc command and provide the output.

    When using the cmemc --raw option, output is a parsed list of dictionaries.
    When using the cmemc --id-only option, output is a parsed list of strings.

    Have a look at click API documentation for more options:
    https://click.palletsprojects.com/en/stable/api/#click.testing.CliRunner
    """
    result = CliRunner().invoke(cli, params)
    if result.exit_code != 0:
        raise RuntimeError(result.exception)
    output: str = result.stdout
    if "--id-only" in params:
        return output.splitlines()
    if "--raw" in params:
        return json.loads(output)
    return output


# use the cmemc connection
environ["CMEMC_CONNECTION"] = "my-dev-cmem"

# specify the command as a list of arguments
# in this case: list all existing worflows
command = ["workflow", "list", "--raw"]

# iterate and process the output
for workflow in cmemc(command):
    project_id = workflow.get("projectId")
    workflow_id = workflow.get("id")
    print(f"Workflow '{workflow_id}' in '{project_id}'")

```

Executing this python script will look like this:

``` shell-session
$ ./cmemc-script.py
Workflow 'input-output' in 'io'
Workflow 'input-output-replaceable' in 'io'
Workflow 'normal' in 'io'
Workflow 'only-input' in 'io'
Workflow 'only-input-included' in 'io'
Workflow 'only-input-replaceable' in 'io'
Workflow 'only-output' in 'io'
Workflow 'only-output-replaceable' in 'io'
```

