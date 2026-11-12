---
title: "cmem-client: components.build.component module"
description: "Corporate Memory Build (DataIntegration) component."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.build.component` {#cmem_client.components.build.component}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory Build (DataIntegration) component.

The Build component bundles the operations of the Build service which are not
collections of items: the workspace feature (import and export of the whole workspace,
reload, access control configuration, marshalling plugins and the loading status) and
the log buffer feature. Each feature lives in its own module of this package.

**Classes:**

- [**Build**](#cmem_client.components.build.component.Build) – High-level interface for the Corporate Memory Build (DataIntegration) service.

## `Build` {#cmem_client.components.build.component.Build}

```python
Build(client)
```

High-level interface for the Corporate Memory Build (DataIntegration) service.

**Attributes:**

- [**workspace**](#cmem_client.components.build.component.Build.workspace) (<code>[BuildWorkspace](../../../components/build/workspace/index.md#cmem_client.components.build.workspace.BuildWorkspace)</code>) – The workspace feature, for operations on the whole DataIntegration workspace.
- [**logs**](#cmem_client.components.build.component.Build.logs) (<code>[BuildLogs](../../../components/build/logs/index.md#cmem_client.components.build.logs.BuildLogs)</code>) – The log buffer feature, for the most recent log lines of Build and the state of its buffer.

**Functions:**

- [**get_health**](#cmem_client.components.build.component.Build.get_health) – Report version and health of the Build (DataIntegration) service.

**Parameters:**

- **client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – A configured Corporate Memory client instance with
authentication and endpoint configuration.

### `get_health` {#cmem_client.components.build.component.Build.get_health}

```python
get_health()
```

Report version and health of the Build (DataIntegration) service.

Reads the service's `/version` and `/health`.

**Returns:**

- <code>[ComponentStatus](../../../models/status/index.md#cmem_client.models.status.ComponentStatus)</code> – The status of Build. An unreachable or failing service is reported DOWN with
- <code>[ComponentStatus](../../../models/status/index.md#cmem_client.models.status.ComponentStatus)</code> – the error, instead of raising.

### `logger` {#cmem_client.components.build.component.Build.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

### `logs` {#cmem_client.components.build.component.Build.logs}

```python
logs: BuildLogs = BuildLogs(client=client)
```

The in-memory log buffer of Build: the most recent lines and the state of the buffer.

### `workspace` {#cmem_client.components.build.component.Build.workspace}

```python
workspace: BuildWorkspace = BuildWorkspace(client=client)
```

Operations on the whole DataIntegration workspace: import, export, reload and status.

