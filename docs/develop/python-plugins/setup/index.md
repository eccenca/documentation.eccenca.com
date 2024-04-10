---
title: "Python Plugins: Setup and Configuration"
icon: material/cog-outline
tags:
    - Python
---
# Setup and Configuration

This section describes which backend components are needed on the DataIntegration server, in order to use python plugins.


## Basic Configuration and Dependencies

!!! info

    When using the official eccenca docker images, setup and basic configuration is already done.


??? note "DataIntegration Configuration"

    The following DataIntegration configuration section describes how to setup and enable the Python Plugin system.

    ```text
    #################################################
    # Plugin Configuration
    #################################################

    # this (optional) file can be used to hold python plugin specific configuration
    include "python-plugins.conf"

    com.eccenca.di.scripting = {
      python = {
        PythonPluginRegistry = {
          # Python plugins will only be loaded if 'enabled' is set to true.
          enabled = true

          # Plugins will only be loaded below the following base package.
          basePackage = "cmem"
        }

        PythonPackageManager = {
          # Python package installer executable.
          pipExecutable = "cmem-pip-wrapper.sh"
        }
      }
    }
    ```


??? note "Python Interpreter"

    An installation of the CPython distribution (at least version 3.3) is required.
    Although other distributions, such as Anaconda, should work as well, only CPython is officially supported.

    The official image ships with a tested python interpreter (currenty - 2024 - Python 3.11).

??? note "Java Embedded Python (Jep)"

    The [Jep](https://github.com/ninia/jep) package needs to be installed.

    The libraries contained in the Jep module need to be accessible from the Java Virtual Machine running DataIntegration.
    This can be achieved by setting an environment variable to the directory path where the Jep module is located:

    -   :simple-linux: **Linux**: set `LD_LIBRARY_PATH`.
    -   :simple-apple: **OS X**: set `DYLD_LIBRARY_PATH`.
    -   :simple-windows: **Windows**: set `PATH`.

    For alternative installation methods, visit [![Jep](https://img.shields.io/github/stars/ninia/jep?label=jep%20%7C%20stars&style=plastic){ .off-glb }](https://github.com/ninia/jep)

    The official image ships with a tested Jep module.

## Specific Changes from the default

### Package Index Locations

The basic setup allows for installation of packages from the [pypi.org](https://pypi.org/search/?q=%22cmem-plugin-%22) python package index, maintained by the [Python Software Foundation](https://www.python.org/psf-landing/).
In order to change the index server, from where you can install python packages, you can use the following environment variables:

-   `PIP_INDEX_URL` - Base URL of the default python package index. This should point to a repository which is compliant with [PEP 503 (the simple repository API)](https://peps.python.org/pep-0503/).
    -   Example Value: `https://pypi.eccenca.com/simple`
    -   Changing this value means, that you can install packages **only** from this repository.
-   `PIP_EXTRA_INDEX_URL` - Extra URLs of package indexes to use in addition to the default package index.
    -   Example Value: `https://pypi.eccenca.com/simple https://example.org/simple`
    -   Multiple index URLs have to be given space-separated.
    -   Changing this values means you can install packages from the given repositories **in addition** to the main index.

For individual needs, you can use additional environment variables known by `pip` (`PIP_TRUSTED_HOST`, `PIP_CERT`, ...).
Please have a look at the [pip documentation](https://pip.pypa.io/en/stable/topics/configuration/#environment-variables).

### Package Path

The basic setup provides a `/data` directory inside of the DataIntegration container, where all changed files are managed in subdirectories.
The environment variable `PYTHONPATH` defines the directory, where the user managed python packages are saved.
The default value of this variable is `/data/python-packages/`.

