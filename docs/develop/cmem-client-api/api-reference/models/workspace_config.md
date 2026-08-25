---
title: "workspace_config"
tags:
  - API
  - Python
  - cmem-client
---

# `workspace_config` {#cmem_client.models.workspace_config}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory Explore workspace configuration models.

This module defines models for representing workspace configurations
managed by the DataPlatform (explore) Workspace Config Controller API.

**Classes:**

- [**LocalizedString**](#cmem_client.models.workspace_config.LocalizedString) – A language-tagged string value.
- [**WorkspaceConfig**](#cmem_client.models.workspace_config.WorkspaceConfig) – An Explore (DataPlatform) workspace configuration.

## `LocalizedString` {#cmem_client.models.workspace_config.LocalizedString}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A language-tagged string value.

**Attributes:**

- [**value**](#cmem_client.models.workspace_config.LocalizedString.value) (<code>str</code>) – Text of the string.
- [**lang**](#cmem_client.models.workspace_config.LocalizedString.lang) (<code>str</code>) – Language tag the text is written in, e.g. ``en``.

### `lang` {#cmem_client.models.workspace_config.LocalizedString.lang}

```python
lang: str
```

### `model_config` {#cmem_client.models.workspace_config.LocalizedString.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `value` {#cmem_client.models.workspace_config.LocalizedString.value}

```python
value: str
```

## `WorkspaceConfig` {#cmem_client.models.workspace_config.WorkspaceConfig}

Bases: <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

An Explore (DataPlatform) workspace configuration.

**Attributes:**

- [**id**](#cmem_client.models.workspace_config.WorkspaceConfig.id) (<code>str</code>) – ID of the configuration. This is the key of the repository.
- [**labels**](#cmem_client.models.workspace_config.WorkspaceConfig.labels) (<code>list[[LocalizedString](#cmem_client.models.workspace_config.LocalizedString)]</code>) – Names of the workspace, one per language. Use the ``label`` property to
pick one without handling the list yourself.
- [**enable_companion**](#cmem_client.models.workspace_config.WorkspaceConfig.enable_companion) (<code>bool | None</code>) – Whether the companion is enabled, or ``None`` if the
configuration does not decide it and the deployment default applies.
- [**enable_graph_insights**](#cmem_client.models.workspace_config.WorkspaceConfig.enable_graph_insights) (<code>bool | None</code>) – Whether Graph Insights is enabled, or ``None`` if the
configuration does not decide it.

**Functions:**

- [**get_id**](#cmem_client.models.workspace_config.WorkspaceConfig.get_id) – Get the ID of the workspace configuration.

### `enable_companion` {#cmem_client.models.workspace_config.WorkspaceConfig.enable_companion}

```python
enable_companion: bool | None = Field(alias='enableCompanion', default=None)
```

### `enable_graph_insights` {#cmem_client.models.workspace_config.WorkspaceConfig.enable_graph_insights}

```python
enable_graph_insights: bool | None = Field(alias='enableGraphInsights', default=None)
```

### `get_id` {#cmem_client.models.workspace_config.WorkspaceConfig.get_id}

```python
get_id()
```

Get the ID of the workspace configuration.

### `id` {#cmem_client.models.workspace_config.WorkspaceConfig.id}

```python
id: str
```

### `label` {#cmem_client.models.workspace_config.WorkspaceConfig.label}

```python
label: str
```

Get the English label, falling back to first available or the ID.

### `labels` {#cmem_client.models.workspace_config.WorkspaceConfig.labels}

```python
labels: list[LocalizedString] = Field(default=[LocalizedString(value='This is a default workspace label', lang='en')])
```

### `model_config` {#cmem_client.models.workspace_config.WorkspaceConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

