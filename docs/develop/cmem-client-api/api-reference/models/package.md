---
title: "cmem-client: package module"
description: "Marketplace package models."
tags:
  - API
  - Python
  - cmem-client
---

# `package` {#cmem_client.models.package}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Marketplace package models.

A marketplace package bundles graphs, projects and Python packages into one installable
unit. The packages installed in a deployment are the items of
``client.marketplace_packages``, keyed by their package ID, while the packages a
marketplace server offers are browsed through ``client.marketplace``.

**Classes:**

- [**Package**](#cmem_client.models.package.Package) – Installed marketplace package.
- [**PackageInstallationMetadata**](#cmem_client.models.package.PackageInstallationMetadata) – Metadata about how and when a marketplace package was installed.
- [**PackageLock**](#cmem_client.models.package.PackageLock) – Package lock.
- [**PackageMetadata**](#cmem_client.models.package.PackageMetadata) – Package metadata.

## `Package` {#cmem_client.models.package.Package}

Bases: <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

Installed marketplace package.

Represents a package installed in Corporate Memory with all its
metadata, file specifications, and version information as stored
in the marketplace catalog graph.

**Attributes:**

- [**package_version**](#cmem_client.models.package.Package.package_version) (<code>PackageVersion</code>) – Manifest and contents of the installed version. Its
``manifest.package_id`` is the key of the repository.
- [**installation_metadata**](#cmem_client.models.package.Package.installation_metadata) (<code>[PackageInstallationMetadata](#cmem_client.models.package.PackageInstallationMetadata) | None</code>) – How and when the package was installed, or ``None`` for
a package installed before this was recorded.

**Functions:**

- [**get_id**](#cmem_client.models.package.Package.get_id) – Get the package identifier.

### `get_id` {#cmem_client.models.package.Package.get_id}

```python
get_id()
```

Get the package identifier.

**Returns:**

- <code>str</code> – The package_id which uniquely identifies this package.

### `installation_metadata` {#cmem_client.models.package.Package.installation_metadata}

```python
installation_metadata: PackageInstallationMetadata | None = None
```

### `model_config` {#cmem_client.models.package.Package.model_config}

```python
model_config = ConfigDict(arbitrary_types_allowed=True, str_strip_whitespace=True, extra='forbid')
```

### `package_version` {#cmem_client.models.package.Package.package_version}

```python
package_version: PackageVersion
```

## `PackageInstallationMetadata` {#cmem_client.models.package.PackageInstallationMetadata}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Metadata about how and when a marketplace package was installed.

This metadata is stored as JSON in the RDF graph and used to determine
whether packages can be automatically removed when they are dependencies.

**Attributes:**

- [**dependency_level**](#cmem_client.models.package.PackageInstallationMetadata.dependency_level) (<code>int</code>) – Depth at which the package was pulled in. ``0`` means it was
installed directly, anything above that means it came in as a dependency
and may be removed again with the package which required it.
- [**installed_at**](#cmem_client.models.package.PackageInstallationMetadata.installed_at) (<code>datetime</code>) – When the package was installed.
- [**python_dependency_already_existed**](#cmem_client.models.package.PackageInstallationMetadata.python_dependency_already_existed) (<code>list[str]</code>) – Python dependencies of the package which
were already installed beforehand, so uninstalling must leave them alone.
- [**package_dependency_already_existed**](#cmem_client.models.package.PackageInstallationMetadata.package_dependency_already_existed) (<code>list[str]</code>) – Marketplace packages this one depends on
which were already installed beforehand.
- [**origin_type**](#cmem_client.models.package.PackageInstallationMetadata.origin_type) (<code>Literal['file', 'marketplace'] | None</code>) – Where the package came from, a ``marketplace`` server or a local
``file``. ``None`` for packages installed before this was tracked.
- [**origin_url**](#cmem_client.models.package.PackageInstallationMetadata.origin_url) (<code>str | None</code>) – URL of the marketplace server the package came from. Only set when
``origin_type`` is ``marketplace``.

### `dependency_level` {#cmem_client.models.package.PackageInstallationMetadata.dependency_level}

```python
dependency_level: int = Field(ge=0, default=0)
```

### `installed_at` {#cmem_client.models.package.PackageInstallationMetadata.installed_at}

```python
installed_at: datetime = Field(default=datetime.now(tz=UTC))
```

### `is_direct_installed` {#cmem_client.models.package.PackageInstallationMetadata.is_direct_installed}

```python
is_direct_installed: bool
```

Indicates whether this package was installed directly

### `model_config` {#cmem_client.models.package.PackageInstallationMetadata.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `origin_type` {#cmem_client.models.package.PackageInstallationMetadata.origin_type}

```python
origin_type: Literal['file', 'marketplace'] | None = None
```

### `origin_url` {#cmem_client.models.package.PackageInstallationMetadata.origin_url}

```python
origin_url: str | None = None
```

### `package_dependency_already_existed` {#cmem_client.models.package.PackageInstallationMetadata.package_dependency_already_existed}

```python
package_dependency_already_existed: list[str] = Field(default=[])
```

### `python_dependency_already_existed` {#cmem_client.models.package.PackageInstallationMetadata.python_dependency_already_existed}

```python
python_dependency_already_existed: list[str] = Field(default=[])
```

## `PackageLock` {#cmem_client.models.package.PackageLock}

Bases: <code>BaseModel</code>

Package lock.

A lock is written for the duration of an install or uninstall, so two clients do
not work on the same package at once.

**Attributes:**

- [**package_id**](#cmem_client.models.package.PackageLock.package_id) (<code>str</code>) – ID of the locked package.
- [**timestamp**](#cmem_client.models.package.PackageLock.timestamp) (<code>datetime</code>) – When the activity started.
- [**user_account**](#cmem_client.models.package.PackageLock.user_account) (<code>str</code>) – Account which started the activity.
- [**activity**](#cmem_client.models.package.PackageLock.activity) (<code>Literal['Install', 'Uninstall']</code>) – What is being done, ``Install`` or ``Uninstall``.

### `activity` {#cmem_client.models.package.PackageLock.activity}

```python
activity: Literal['Install', 'Uninstall']
```

### `package_id` {#cmem_client.models.package.PackageLock.package_id}

```python
package_id: str
```

### `timestamp` {#cmem_client.models.package.PackageLock.timestamp}

```python
timestamp: datetime
```

### `user_account` {#cmem_client.models.package.PackageLock.user_account}

```python
user_account: str
```

## `PackageMetadata` {#cmem_client.models.package.PackageMetadata}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Package metadata.

**Attributes:**

- [**name**](#cmem_client.models.package.PackageMetadata.name) (<code>str</code>) – Human readable name of the package.
- [**description**](#cmem_client.models.package.PackageMetadata.description) (<code>str</code>) – What the package provides.
- [**comment**](#cmem_client.models.package.PackageMetadata.comment) (<code>str | None</code>) – Additional remark about the package.

### `comment` {#cmem_client.models.package.PackageMetadata.comment}

```python
comment: str | None = None
```

### `description` {#cmem_client.models.package.PackageMetadata.description}

```python
description: str
```

### `model_config` {#cmem_client.models.package.PackageMetadata.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `name` {#cmem_client.models.package.PackageMetadata.name}

```python
name: str
```

