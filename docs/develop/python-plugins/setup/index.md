---
status: new
title: "Python Plugins: Setup and Configuration"
icon: material/cog-outline
tags:
    - Python
---
# Setup and Configuration

This section describes which backend components are needed on the Build (DataIntegration) server, in order to use python plugins.


## Basic Configuration and Dependencies

!!! info

    When using the official eccenca docker images, setup and basic configuration is already done.


??? note "Build (DataIntegration) Configuration"

    The following Build (DataIntegration) configuration section describes how to setup and enable the Python Plugin system.

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

    The official image ships with a tested python interpreter (currently - 2025 - Python 3.13).

??? note "Java Embedded Python (Jep)"

    The [Jep](https://github.com/ninia/jep) package needs to be installed.

    The libraries contained in the Jep module need to be accessible from the Java Virtual Machine running Build (DataIntegration).
    This can be achieved by setting an environment variable to the directory path where the Jep module is located:

    -   :simple-linux: **Linux**: set `LD_LIBRARY_PATH`.
    -   :simple-apple: **OS X**: set `DYLD_LIBRARY_PATH`.
    -   :simple-windows: **Windows**: set `PATH`.

    For alternative installation methods, visit [![Jep](https://img.shields.io/github/stars/ninia/jep?label=jep%20%7C%20stars&style=plastic){ .off-glb }](https://github.com/ninia/jep)

    The official image ships with a tested Jep module.

## Specific Changes from the default

### Package Index Locations

The basic setup allows for installation of packages from the [pypi.org](https://pypi.org/search/?q=%22cmem-plugin-%22) python package index, maintained by the [Python Software Foundation](https://www.python.org/psf-landing/).
In order to change the remote index server, from where you can install python packages, you need to set the following environment variables in the data integration container:

-   `PIP_INDEX_URL` - Base URL of the default python package index Base URL. This should point to a repository which is compliant with [PEP 503 (the simple repository API)](https://peps.python.org/pep-0503/). If this variable is not set, the [official Python Package Index](https://pypi.python.org/simple) is used.
    -   Example Value: `https://pypi.eccenca.com/simple` (the eccenca Python Package Index holds only published Corporate Memory Python Plugins and respective dependencies)
    -   Changing this value means, that you can install packages **only** from this repository.
-   `PIP_EXTRA_INDEX_URL` - Extra URLs of package indexes to use in addition to the default package index.
    -   Example Value: `https://pypi.eccenca.com/simple https://example.org/simple`
    -   Multiple index URLs have to be given space-separated.
    -   Changing this values means you can install packages from the given repositories **in addition** to the main index.

For individual needs, you can use additional environment variables known by `pip` (`PIP_TRUSTED_HOST`, `PIP_CERT`, ...).
Please have a look at the [pip documentation](https://pip.pypa.io/en/stable/topics/configuration/#environment-variables).

### Local Packages only

In cases, where you have limited or disabled network capabilities to the internet, you can disable package retrieval and provide the packages in a local directory.
To do so, you need to set the following environment variables in the data integration container:

-   `PIP_NO_INDEX` - set the value as `true` to disable the package retrieval completely.
-   `PIP_FIND_LINKS` - set to a container internal directory, where the packages and its dependencies will be provided.
    -   Example Value: `/data/downloaded-packages`

This setup will allow installation of packages and its dependencies ONLY from the given directory.

As a next step, you need to provide the needed packages in this directory.
To do so, use the [`pip download`](https://pip.pypa.io/en/stable/cli/pip_download/) command and copy or mount the downloaded files in your container.

??? note "Example shell session showing the usage of `pip download`"

    ```
    $ cat requirements.txt
    cmem-plugin-validation
    cmem-plugin-graphql
    cmem-plugin-kafka
    cmem-plugin-yaml

    $ pip download --only-binary=:all: -r requirements.txt --platform manylinux2014_x86_64
    Collecting cmem-plugin-validation (from -r requirements.txt (line 1))
    ...
    Saved ./six-1.16.0-py2.py3-none-any.whl
    Successfully downloaded cmem-plugin-validation ...
    ```

    Please note the `--platform` identifier. This is only needed in case you prepare the downloaded package directory
    on a machine with a different platform compared to you server (e.g. on a Mac).

### Package Path

The basic setup provides a `/data` directory inside of the Build (DataIntegration) container, where all changed files are managed in subdirectories.
The environment variable `PYTHONPATH` defines the directory, where the user-managed python packages are saved.
This directory shall be persisted between restarts of Build (DataIntegration).
The default value of this variable is `/data/python-packages/`.
DataIntegration won't start if the directory defined by `PYTHONPATH` is not present and can't be created.
In addition Build (DataIntegration) needs write access to that folder.
This is tested on Build (DataIntegration) startup.

!!! info
    By setting environment variable `PYTHONPATH_FAILURE` (default: `true`) to other values than `true` this behavior can be skipped.
    However this might effect the usability of python plugins.
