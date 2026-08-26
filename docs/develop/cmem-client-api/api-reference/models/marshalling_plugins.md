---
title: "cmem-client: marshalling_plugins module"
tags:
  - API
  - Python
  - cmem-client
---

# `marshalling_plugins` {#cmem_client.models.marshalling_plugins}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Marshalling Plugin models

A marshalling plugin defines the file format a DataIntegration workspace is written to
and read from. The plugins a deployment offers are returned by
``client.workspace.get_marshalling_plugins()``, and their ``id`` is what
``client.workspace.export_to_zip()`` and ``import_from_zip()`` expect.

**Classes:**

- [**MarshallingPlugin**](#cmem_client.models.marshalling_plugins.MarshallingPlugin) – Marshalling Plugin Model

## `MarshallingPlugin` {#cmem_client.models.marshalling_plugins.MarshallingPlugin}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Marshalling Plugin Model

**Attributes:**

- [**id**](#cmem_client.models.marshalling_plugins.MarshallingPlugin.id) (<code>str</code>) – Identifier of the plugin, e.g. ``xmlZip``, as accepted by the workspace
import and export operations.
- [**label**](#cmem_client.models.marshalling_plugins.MarshallingPlugin.label) (<code>str</code>) – Human readable name of the plugin.
- [**description**](#cmem_client.models.marshalling_plugins.MarshallingPlugin.description) (<code>str</code>) – What the plugin does and which format it produces.
- [**file_extension**](#cmem_client.models.marshalling_plugins.MarshallingPlugin.file_extension) (<code>str</code>) – File extension of the produced files, without a leading dot.
- [**media_type**](#cmem_client.models.marshalling_plugins.MarshallingPlugin.media_type) (<code>str</code>) – Media type of the produced files.

### `description` {#cmem_client.models.marshalling_plugins.MarshallingPlugin.description}

```python
description: str
```

### `file_extension` {#cmem_client.models.marshalling_plugins.MarshallingPlugin.file_extension}

```python
file_extension: str = Field(alias='fileExtension')
```

### `id` {#cmem_client.models.marshalling_plugins.MarshallingPlugin.id}

```python
id: str
```

### `label` {#cmem_client.models.marshalling_plugins.MarshallingPlugin.label}

```python
label: str
```

### `media_type` {#cmem_client.models.marshalling_plugins.MarshallingPlugin.media_type}

```python
media_type: str = Field(alias='mediaType')
```

### `model_config` {#cmem_client.models.marshalling_plugins.MarshallingPlugin.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

