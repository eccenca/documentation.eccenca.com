---
title: "cmem-client: models.workspace_plugin module"
description: "Workspace plugin model."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.workspace_plugin` {#cmem_client.models.workspace_plugin}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Workspace plugin model.

A workspace plugin is a single plugin class DataIntegration discovered, as opposed to
the Python package shipping it. ``client.python_packages.list_plugins()`` returns the
plugins of all installed packages.

**Classes:**

- [**WorkspacePlugin**](#cmem_client.models.workspace_plugin.WorkspacePlugin) – A plugin installed in the Corporate Memory DataIntegration workspace.

## `WorkspacePlugin` {#cmem_client.models.workspace_plugin.WorkspacePlugin}

Bases: <code>[ReadRepositoryItem](../../models/base/index.md#cmem_client.models.base.ReadRepositoryItem)</code>

A plugin installed in the Corporate Memory DataIntegration workspace.

**Attributes:**

- [**id**](#cmem_client.models.workspace_plugin.WorkspacePlugin.id) (<code>str</code>) – Identifier of the plugin, unique within the deployment.
- [**module_name**](#cmem_client.models.workspace_plugin.WorkspacePlugin.module_name) (<code>str</code>) – Python module the plugin class was loaded from.
- [**plugin_type**](#cmem_client.models.workspace_plugin.WorkspacePlugin.plugin_type) (<code>str</code>) – Kind of plugin, e.g. ``WorkflowPlugin`` or ``TransformPlugin``.
- [**label**](#cmem_client.models.workspace_plugin.WorkspacePlugin.label) (<code>str</code>) – Human readable name shown in the user interface.
- [**is_registered**](#cmem_client.models.workspace_plugin.WorkspacePlugin.is_registered) (<code>bool</code>) – Whether DataIntegration registered the plugin successfully. A
plugin which failed to load is reported with ``False``.

**Functions:**

- [**get_id**](#cmem_client.models.workspace_plugin.WorkspacePlugin.get_id) – Get the plugin identifier.

### `get_id` {#cmem_client.models.workspace_plugin.WorkspacePlugin.get_id}

```python
get_id()
```

Get the plugin identifier.

### `id` {#cmem_client.models.workspace_plugin.WorkspacePlugin.id}

```python
id: str
```

### `is_registered` {#cmem_client.models.workspace_plugin.WorkspacePlugin.is_registered}

```python
is_registered: bool = Field(alias='isRegistered', default=True)
```

### `label` {#cmem_client.models.workspace_plugin.WorkspacePlugin.label}

```python
label: str
```

### `model_config` {#cmem_client.models.workspace_plugin.WorkspacePlugin.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `module_name` {#cmem_client.models.workspace_plugin.WorkspacePlugin.module_name}

```python
module_name: str = Field(alias='moduleName')
```

### `plugin_type` {#cmem_client.models.workspace_plugin.WorkspacePlugin.plugin_type}

```python
plugin_type: str = Field(alias='pluginType')
```

