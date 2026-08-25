---
title: "graph_insight"
tags:
  - API
  - Python
  - cmem-client
---

# `graph_insight` {#cmem_client.models.graph_insight}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Graph Insight models for Corporate Memory.

Graph Insight is the semspect extension, which keeps its own indexed snapshot of the
graphs it explores. The snapshots are the items of ``client.graph_insights``, keyed by
their database ID. That repository does not fetch on creation, so call ``fetch_data()``
before iterating it.

**Classes:**

- [**GraphInsightSnapshot**](#cmem_client.models.graph_insight.GraphInsightSnapshot) – A single Graph Insight snapshot from the semspect extension.

## `GraphInsightSnapshot` {#cmem_client.models.graph_insight.GraphInsightSnapshot}

Bases: <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A single Graph Insight snapshot from the semspect extension.

**Attributes:**

- [**database_id**](#cmem_client.models.graph_insight.GraphInsightSnapshot.database_id) (<code>str</code>) – Identifier of the snapshot database. This is the key of the
repository.
- [**main_graph_synced**](#cmem_client.models.graph_insight.GraphInsightSnapshot.main_graph_synced) (<code>str</code>) – IRI of the graph the snapshot was built from.
- [**all_graphs_synced**](#cmem_client.models.graph_insight.GraphInsightSnapshot.all_graphs_synced) (<code>list[str]</code>) – IRIs of every graph included in the snapshot, which covers
the main graph and the graphs it imports.
- [**update_info_timestamp**](#cmem_client.models.graph_insight.GraphInsightSnapshot.update_info_timestamp) (<code>str</code>) – When the snapshot was last updated, as reported by the
extension.
- [**status**](#cmem_client.models.graph_insight.GraphInsightSnapshot.status) (<code>str</code>) – State of the snapshot, e.g. whether it is ready or still being built.
- [**is_valid**](#cmem_client.models.graph_insight.GraphInsightSnapshot.is_valid) (<code>bool</code>) – Whether the snapshot is still in sync with the graphs it was built
from. A stale snapshot needs to be rebuilt before it is queried again.

**Functions:**

- [**get_id**](#cmem_client.models.graph_insight.GraphInsightSnapshot.get_id) – Get the snapshot ID.

### `all_graphs_synced` {#cmem_client.models.graph_insight.GraphInsightSnapshot.all_graphs_synced}

```python
all_graphs_synced: list[str] = Field(alias='allGraphsSynced')
```

### `database_id` {#cmem_client.models.graph_insight.GraphInsightSnapshot.database_id}

```python
database_id: str = Field(alias='databaseId')
```

### `get_id` {#cmem_client.models.graph_insight.GraphInsightSnapshot.get_id}

```python
get_id()
```

Get the snapshot ID.

### `is_valid` {#cmem_client.models.graph_insight.GraphInsightSnapshot.is_valid}

```python
is_valid: bool = Field(alias='isValid')
```

### `main_graph_synced` {#cmem_client.models.graph_insight.GraphInsightSnapshot.main_graph_synced}

```python
main_graph_synced: str = Field(alias='mainGraphSynced')
```

### `model_config` {#cmem_client.models.graph_insight.GraphInsightSnapshot.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `status` {#cmem_client.models.graph_insight.GraphInsightSnapshot.status}

```python
status: str
```

### `update_info_timestamp` {#cmem_client.models.graph_insight.GraphInsightSnapshot.update_info_timestamp}

```python
update_info_timestamp: str = Field(alias='updateInfoTimestamp')
```

