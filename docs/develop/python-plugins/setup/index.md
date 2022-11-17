---
title: "Python Plugins: Setup and Configuration"
icon: material/cog-outline
tags:
    - Python
---
# Setup and Configuration

This section describes which backend components are needed on the DataIntegration server.
When using our official docker images, these components are already installed and configured.

## Configuration

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
      # pipExecutable = "pip"
      pipExecutable = "cmem-pip-wrapper.sh"
    }
  }
}
```

## Python Interpreter

An installation of the CPython distribution (at least version 3.3) is required.
While other distributions, such as Anaconda, should be working as well, only CPython is officially supported.

## Java Embedded Python (Jep)

The [Jep](https://github.com/ninia/jep) package needs to be installed.

The libraries contained in the Jep module need to be accessible from the Java Virtual Machine running DataIntegration.
This can be achieved by setting an environment variable to the directory path where the Jep module is located:

-   :simple-linux: **Linux**: set `LD_LIBRARY_PATH`.
-   :simple-apple: **OS X**: set `DYLD_LIBRARY_PATH`.
-   :simple-windows: **Windows**: set `PATH`.

For alternative installation methods, visit [![Jep](https://img.shields.io/github/stars/ninia/jep?label=jep%20%7C%20stars&style=plastic){ .off-glb }](https://github.com/ninia/jep)

