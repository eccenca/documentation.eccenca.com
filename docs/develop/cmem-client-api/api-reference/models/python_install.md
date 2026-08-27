---
title: "cmem-client: python_install module"
description: "Result models for Python package installation and plugin management operations."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.python_install` {#cmem_client.models.python_install}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Result models for Python package installation and plugin management operations.

Installing a Python package into DataIntegration runs pip inside the deployment and
then registers the plugins the package ships. Both steps can fail on their own, so the
operations of ``client.python_packages`` report the outcome with these models rather
than raising: a package can install cleanly and still contribute a plugin which does
not load.

**Classes:**

- [**PluginError**](#cmem_client.models.python_install.PluginError) – An error reported during plugin registration.
- [**PluginReloadResult**](#cmem_client.models.python_install.PluginReloadResult) – Result of a plugin reload operation.
- [**PythonInstallResult**](#cmem_client.models.python_install.PythonInstallResult) – Result of a Python package installation (by name or by file).

## `PluginError` {#cmem_client.models.python_install.PluginError}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

An error reported during plugin registration.

**Attributes:**

- [**package_name**](#cmem_client.models.python_install.PluginError.package_name) (<code>str</code>) – Name of the package whose plugin failed to register.
- [**error_message**](#cmem_client.models.python_install.PluginError.error_message) (<code>str</code>) – Message of the error.
- [**error_type**](#cmem_client.models.python_install.PluginError.error_type) (<code>str</code>) – Type of the error, as named by DataIntegration.
- [**stack_trace**](#cmem_client.models.python_install.PluginError.stack_trace) (<code>str | None</code>) – Stack trace of the error, if the deployment reports one.

### `error_message` {#cmem_client.models.python_install.PluginError.error_message}

```python
error_message: str = Field(alias='errorMessage', default='')
```

### `error_type` {#cmem_client.models.python_install.PluginError.error_type}

```python
error_type: str = Field(alias='errorType', default='')
```

### `model_config` {#cmem_client.models.python_install.PluginError.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `package_name` {#cmem_client.models.python_install.PluginError.package_name}

```python
package_name: str = Field(alias='packageName', default='')
```

### `stack_trace` {#cmem_client.models.python_install.PluginError.stack_trace}

```python
stack_trace: str | None = Field(alias='stackTrace', default=None)
```

## `PluginReloadResult` {#cmem_client.models.python_install.PluginReloadResult}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Result of a plugin reload operation.

**Attributes:**

- [**errors**](#cmem_client.models.python_install.PluginReloadResult.errors) (<code>list[[PluginError](#cmem_client.models.python_install.PluginError)]</code>) – Plugins which failed to register during the reload. An empty list means
every plugin loaded.

### `errors` {#cmem_client.models.python_install.PluginReloadResult.errors}

```python
errors: list[PluginError] = Field(default_factory=list)
```

### `model_config` {#cmem_client.models.python_install.PluginReloadResult.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `PythonInstallResult` {#cmem_client.models.python_install.PythonInstallResult}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Result of a Python package installation (by name or by file).

**Attributes:**

- [**success**](#cmem_client.models.python_install.PythonInstallResult.success) (<code>bool</code>) – Whether the installation itself succeeded. Plugins which failed to
register afterwards are reported in ``plugin_errors`` and do not clear this
flag.
- [**output**](#cmem_client.models.python_install.PythonInstallResult.output) (<code>str</code>) – Combined output of the installation.
- [**standard_output**](#cmem_client.models.python_install.PythonInstallResult.standard_output) (<code>str</code>) – What the installation wrote to stdout.
- [**error_output**](#cmem_client.models.python_install.PythonInstallResult.error_output) (<code>str</code>) – What the installation wrote to stderr.
- [**plugin_errors**](#cmem_client.models.python_install.PythonInstallResult.plugin_errors) (<code>list[[PluginError](#cmem_client.models.python_install.PluginError)]</code>) – Plugins of the installed package which failed to register.

### `error_output` {#cmem_client.models.python_install.PythonInstallResult.error_output}

```python
error_output: str = Field(alias='errorOutput', default='')
```

### `model_config` {#cmem_client.models.python_install.PythonInstallResult.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `output` {#cmem_client.models.python_install.PythonInstallResult.output}

```python
output: str = ''
```

### `plugin_errors` {#cmem_client.models.python_install.PythonInstallResult.plugin_errors}

```python
plugin_errors: list[PluginError] = Field(default_factory=list)
```

### `standard_output` {#cmem_client.models.python_install.PythonInstallResult.standard_output}

```python
standard_output: str = Field(alias='standardOutput', default='')
```

### `success` {#cmem_client.models.python_install.PythonInstallResult.success}

```python
success: bool = False
```

