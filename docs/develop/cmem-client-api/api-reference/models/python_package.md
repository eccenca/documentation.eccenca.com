---
title: "cmem-client: python_package module"
tags:
  - API
  - Python
  - cmem-client
---

# `python_package` {#cmem_client.models.python_package}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Python package models.

DataIntegration can be extended with Python packages, which ship the plugins a
workflow uses. The installed packages are the items of ``client.python_packages``,
keyed by their PyPI name.

**Classes:**

- [**PythonPackage**](#cmem_client.models.python_package.PythonPackage) – Installed python package.

**Attributes:**

- [**PipRequirementSpecifier**](#cmem_client.models.python_package.PipRequirementSpecifier) –

## `PipRequirementSpecifier` {#cmem_client.models.python_package.PipRequirementSpecifier}

```python
PipRequirementSpecifier = Annotated[str, Field(title='Pip Requirement Specifier', description="A pip requirement specifier as defined in PEP 440/508: a package name optionally followed by one or more comma-separated version constraints (e.g. 'requests', 'requests==2.27.1', 'requests>=2.0,<3.0').", pattern=_PIP_REQUIREMENT_PATTERN)]
```

## `PythonPackage` {#cmem_client.models.python_package.PythonPackage}

Bases: <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

Installed python package.

Represents a python package installed in Corporate Memory

**Attributes:**

- [**name**](#cmem_client.models.python_package.PythonPackage.name) (<code>PyPiIdentifier</code>) – PyPI name of the package. This is the key of the repository.
- [**version**](#cmem_client.models.python_package.PythonPackage.version) (<code>str | None</code>) – Installed version, or ``None`` if the deployment does not report one.

**Functions:**

- [**get_id**](#cmem_client.models.python_package.PythonPackage.get_id) – Get the package identifier.

### `get_id` {#cmem_client.models.python_package.PythonPackage.get_id}

```python
get_id()
```

Get the package identifier.

**Returns:**

- <code>str</code> – The python pypi name which uniquely identifies this package.

### `model_config` {#cmem_client.models.python_package.PythonPackage.model_config}

```python
model_config = ConfigDict(arbitrary_types_allowed=True, str_strip_whitespace=True, extra='forbid')
```

### `name` {#cmem_client.models.python_package.PythonPackage.name}

```python
name: PyPiIdentifier
```

### `version` {#cmem_client.models.python_package.PythonPackage.version}

```python
version: str | None = None
```

