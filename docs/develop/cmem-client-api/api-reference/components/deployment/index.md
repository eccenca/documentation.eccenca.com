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
DataPlatform, shapes catalog, graph store, marketplace, and Graph Insights).

**Classes:**

- [**Deployment**](#cmem_client.components.deployment.Deployment) – High-level interface for Corporate Memory deployment status.

**Attributes:**

- [**MARKETPLACE_MIN_BUILD_VERSION**](#cmem_client.components.deployment.MARKETPLACE_MIN_BUILD_VERSION) – Earliest (year, major) build (DataIntegration) version that ships the marketplace.

## `Deployment` {#cmem_client.components.deployment.Deployment}

```python
Deployment(client)
```

High-level interface for Corporate Memory deployment status.

Aggregates version and health information across all Corporate Memory
components (DataIntegration, DataPlatform, shapes catalog, graph store,
marketplace, Graph Insights), as each component reports it with its own
`get_health()`. Per-component failures are captured rather than raised, so a
partial outage still returns a populated StatusInfo for the healthy components.

**Functions:**

- [**get_status**](#cmem_client.components.deployment.Deployment.get_status) – Aggregate version and health information across all components.

**Attributes:**

- [**logger**](#cmem_client.components.deployment.Deployment.logger) –

### `get_status` {#cmem_client.components.deployment.Deployment.get_status}

```python
get_status()
```

Aggregate version and health information across all components.

Each component reports its own health; this adds the parts which depend on more
than one service: the store, which Explore describes, and whether a failing local
marketplace counts, which depends on the Build version.

**Returns:**

- <code>[StatusInfo](../../models/status/index.md#cmem_client.models.status.StatusInfo)</code> – StatusInfo with version, health, and error per component. The
- <code>[StatusInfo](../../models/status/index.md#cmem_client.models.status.StatusInfo)</code> – overall health is exposed via the StatusInfo.health property.

### `logger` {#cmem_client.components.deployment.Deployment.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

## `MARKETPLACE_MIN_BUILD_VERSION` {#cmem_client.components.deployment.MARKETPLACE_MIN_BUILD_VERSION}

```python
MARKETPLACE_MIN_BUILD_VERSION = (26, 2)
```

Earliest (year, major) build (DataIntegration) version that ships the marketplace.

