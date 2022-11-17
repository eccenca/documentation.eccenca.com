---
title: "Python Plugins: Installation and Usage"
icon: material/download-circle-outline
tags:
  - Python
  - Plugin
---
# Installation and Usage of Python Plugins

Plugins are a released as parts of Python packages.
The can but do not need to be open source and published on [pypi.org](https://pypi.org/search/?q=%22cmem-plugin-%22) (a widely used Python Package Index).

## Installation

If you want to install a python plugin package, you can do this by using cmemc's [admin workspace python command group](../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

The following shell commands demonstrate the basic workflow:

```shell-session
# list all installed python packages
# Note: the list contains plugin packages as well all dependencies which they are using
$ cmemc admin workspace python list
Name                Version
------------------  -----------
certifi             2022.5.18.1
charset-normalizer  2.0.12
cmem-cmempy         22.1.1
cmem-plugin-base    1.2.0
idna                3.3
isodate             0.6.1
jep                 4.0.2
pip                 20.3.4
pyparsing           3.0.9
rdflib              6.1.1
requests            2.27.1
requests-toolbelt   0.9.1
setuptools          52.0.0
six                 1.16.0
urllib3             1.26.9
wheel               0.34.2

# Install a plugin package from pypi.org
$ cmemc admin workspace python install cmem-plugin-graphql
Install package cmem-plugin-graphql ... done

# list available plugins
$ cmemc admin workspace python list-plugins
ID                                 Type            Label
---------------------------------  --------------  -------------
cmem_plugin_graphql-GraphQLPlugin  WorkflowPlugin  GraphQL query

# uninstall the plugin package
$ cmemc admin workspace python uninstall cmem-plugin-graphql
Uninstall package cmem-plugin-graphql ... done

# validate that no plugins are installed
$ cmemc admin workspace python list-plugins
ID    Type    Label
----  ------  -------


```

You can also install specific versions of a package by using version qualifier

```shell-session
$ cmemc admin workspace python install cmem-plugin-graphql==1.0.0
Install package cmem-plugin-graphql ... done
```

And you can also install a package from a source distribution file

```shell-session
$ cmemc admin workspace python install cmem-plugin-graphql-1.0.0.tar.gz
Install package cmem-plugin-graphql ... done
```

## Usage

TODO
