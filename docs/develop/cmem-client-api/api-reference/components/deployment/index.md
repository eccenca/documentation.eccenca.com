---
title: "cmem-client: components.deployment module"
description: "Corporate Memory deployment status component."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.deployment` {#cmem_client.components.deployment}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory deployment status component.

Provides the Deployment component for aggregating version and health
information across all Corporate Memory services (DataIntegration,
DataPlatform, shapes catalog, and graph store).

**Classes:**

- [**Deployment**](#cmem_client.components.deployment.Deployment) – High-level interface for Corporate Memory deployment status.

## `Deployment` {#cmem_client.components.deployment.Deployment}

```python
Deployment(client)
```

High-level interface for Corporate Memory deployment status.

Aggregates version and health information across all Corporate Memory
components (DataIntegration, DataPlatform, shapes catalog, graph store).
Per-component failures are captured rather than raised, so a partial
outage still returns a populated StatusInfo for the healthy components.

**Functions:**

- [**get_status**](#cmem_client.components.deployment.Deployment.get_status) – Aggregate version and health information across all components.

**Attributes:**

- [**logger**](#cmem_client.components.deployment.Deployment.logger) –

### `get_status` {#cmem_client.components.deployment.Deployment.get_status}

```python
get_status()
```

Aggregate version and health information across all components.

**Returns:**

- <code>[StatusInfo](../../models/status/index.md#cmem_client.models.status.StatusInfo)</code> – StatusInfo with version, health, and error per component. The
- <code>[StatusInfo](../../models/status/index.md#cmem_client.models.status.StatusInfo)</code> – overall health is exposed via the StatusInfo.health property.

### `logger` {#cmem_client.components.deployment.Deployment.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

