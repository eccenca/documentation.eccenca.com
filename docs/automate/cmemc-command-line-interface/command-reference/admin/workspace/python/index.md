---
title: "cmemc: Command Group - admin workspace python"
description: "List, install, or uninstall python packages."
icon: material/language-python
tags:
  - Python
  - cmemc
---
# admin workspace python Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, install, or uninstall python packages.

Python packages are used to extend the DataIntegration workspace with python plugins. To get a list of installed packages, execute the list command.

!!! warning
    Installing packages from unknown sources is not recommended. Plugins are not verified for malicious code.



## admin workspace python install

Install a python package to the workspace.

```shell-session title="Usage"
$ cmemc admin workspace python install PACKAGE
```




This command is essentially a `pip install` in the remote python environment.

You can install a package by uploading a source distribution .tar.gz file, by uploading a build distribution .whl file, or by specifying a package name, i.e., a pip requirement specifier with a package name available on pypi.org (e.g. `requests==2.27.1`).



## admin workspace python uninstall

Uninstall a python package from the workspace.

```shell-session title="Usage"
$ cmemc admin workspace python uninstall PACKAGE_NAME
```




This command is essentially a `pip uninstall` in the remote python environment.



## admin workspace python list

List installed python packages.

```shell-session title="Usage"
$ cmemc admin workspace python list [OPTIONS]
```




This command is essentially a `pip list` in the remote python environment.

It outputs a table of python package identifiers with version information.



??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    --id-only   Lists only package identifier. This is useful for piping the IDs
                into other commands.
    ```

## admin workspace python list-plugins

List installed workspace plugins.

```shell-session title="Usage"
$ cmemc admin workspace python list-plugins [OPTIONS]
```




This commands lists all discovered plugins.

!!! note
    The plugin discovery is restricted to package prefix (`cmem-`).




??? info "Options"
    ```text

    --raw              Outputs raw JSON.
    --id-only          Lists only plugin identifier.
    --package-id-only  Lists only plugin package identifier.
    ```

