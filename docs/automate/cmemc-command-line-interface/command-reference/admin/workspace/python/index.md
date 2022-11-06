---
title: "cmemc: Command Group - admin workspace python"
description: "List, install, or uninstall python packages."
icon: material/language-python
tags:
  - Python
  - cmemc
---
# admin workspace python Command Group

List, install, or uninstall python packages.

Python packages are used to extend the DataIntegration workspace
with python plugins. To get a list of installed packages, execute the
list command.

Warning: Installing packages from unknown sources is not recommended.
Plugins are not verified for malicious code.

## admin workspace python install

Install a python package to the workspace.

This command is basically a 'pip install' in the remote python
environment.

You can install a package by uploading a source distribution
.tar.gz file, or by uploading a build distribution .whl file, or by
specifying a package name, more precisely, a pip requirement
specifier with a package name available on pypi.org
(e.g. 'requests==2.27.1').

```shell-session
$ cmemc admin workspace python install [OPTIONS] PACKAGE
```

```text
Usage: cmemc admin workspace python install [OPTIONS] PACKAGE

  Install a python package to the workspace.

  This command is basically a 'pip install' in the remote python
  environment.

  You can install a package by uploading a source distribution .tar.gz file,
  or by uploading a build distribution .whl file, or by specifying a package
  name, more precisely, a pip requirement specifier with a package name
  available on pypi.org (e.g. 'requests==2.27.1').
```
## admin workspace python uninstall

Uninstall a python package from the workspace.

This command is basically a 'pip uninstall' in the remote
python environment.

```shell-session
$ cmemc admin workspace python uninstall [OPTIONS] PACKAGE_NAME
```

```text
Usage: cmemc admin workspace python uninstall [OPTIONS] PACKAGE_NAME

  Uninstall a python package from the workspace.

  This command is basically a 'pip uninstall' in the remote python
  environment.
```
## admin workspace python list

List installed python packages.

This command is basically a 'pip list' in the remote python environment.

It outputs a table of python package identifiers with version information.

```shell-session
$ cmemc admin workspace python list [OPTIONS]
```

```text
Usage: cmemc admin workspace python list [OPTIONS]

  List installed python packages.

  This command is basically a 'pip list' in the remote python environment.

  It outputs a table of python package identifiers with version information.

Options:
  --raw       Outputs raw JSON.
  --id-only   Lists only package identifier. This is useful for piping the IDs
              into other commands.
```
## admin workspace python list-plugins

List installed workspace plugins.

This commands lists all discovered plugins.
Note that the plugin discovery is limited to specific packages.

```shell-session
$ cmemc admin workspace python list-plugins [OPTIONS]
```

```text
Usage: cmemc admin workspace python list-plugins [OPTIONS]

  List installed workspace plugins.

  This commands lists all discovered plugins. Note that the plugin discovery
  is limited to specific packages.

Options:
  --raw              Outputs raw JSON.
  --id-only          Lists only plugin identifier.
  --package-id-only  Lists only plugin package identifier.
```
