---
title: "cmem-client: components.graphinsights.component module"
description: "Corporate Memory Graph Insights component."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.graphinsights.component` {#cmem_client.components.graphinsights.component}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory Graph Insights component.

Graph Insights is an optional extension of Corporate Memory which computes statistics
snapshots of graphs. This component covers the extension itself; the snapshots are the
items of the [`GraphSnapshotsRepository`](../../../repositories/graph_snapshots/index.md#cmem_client.repositories.graph_snapshots.GraphSnapshotsRepository)
returned by `client.graph_snapshots`.

The component is `client.graphinsights`. Until cmem-client 2.0.0, `client.graph_insights`
still returns the snapshot repository it used to be, with a `DeprecationWarning` naming
`client.graph_snapshots`.

**Classes:**

- [**GraphInsights**](#cmem_client.components.graphinsights.component.GraphInsights) – High-level interface for the Corporate Memory Graph Insights extension.

## `GraphInsights` {#cmem_client.components.graphinsights.component.GraphInsights}

```python
GraphInsights(client)
```

High-level interface for the Corporate Memory Graph Insights extension.

Graph Insights is optional, so check `is_available()` before using its snapshots
through `client.graph_snapshots`.

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> client.graphinsights.is_available()
```

**Functions:**

- [**get_health**](#cmem_client.components.graphinsights.component.GraphInsights.get_health) – Report version and health of the Graph Insights extension.
- [**is_available**](#cmem_client.components.graphinsights.component.GraphInsights.is_available) – Tell whether the Graph Insights extension is active and the user may use it.

**Attributes:**

- [**logger**](#cmem_client.components.graphinsights.component.GraphInsights.logger) –

**Parameters:**

- **client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – A configured Corporate Memory client instance with
authentication and endpoint configuration.

### `get_health` {#cmem_client.components.graphinsights.component.GraphInsights.get_health}

```python
get_health()
```

Report version and health of the Graph Insights extension.

An extension which is not available is reported as not applicable. Otherwise the
version and health come from its `/actuator/info` and `/actuator/health`; a build
of Graph Insights without these endpoints keeps version and health UNKNOWN and
names the failing request in the error, instead of being reported DOWN.

**Returns:**

- <code>[GraphInsightsStatus](../../../models/status/index.md#cmem_client.models.status.GraphInsightsStatus)</code> – The status of the extension, without raising.

### `is_available` {#cmem_client.components.graphinsights.component.GraphInsights.is_available}

```python
is_available()
```

Tell whether the Graph Insights extension is active and the user may use it.

**Returns:**

- <code>bool</code> – True if the extension is active and the user is allowed to use it. False
- <code>bool</code> – otherwise, including when the extension cannot be reached.

### `logger` {#cmem_client.components.graphinsights.component.GraphInsights.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

