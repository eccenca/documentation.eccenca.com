---
title: "cmem-client: repositories.graph_insights module"
description: "Repository for the Graph Insights snapshots of Corporate Memory."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.graph_insights` {#cmem_client.repositories.graph_insights}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the Graph Insights snapshots of Corporate Memory.

Provides GraphInsightsRepository for creating statistics snapshots of a graph, polling
their computation and deleting them. Graph Insights is an optional extension, so check
that it is enabled before using it.

**Examples:**

Check whether the extension is available, then create a snapshot:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> client.graph_insights.is_available()
>>> snapshot_id = client.graph_insights.create("https://ns.eccenca.com/data/config/")
>>> client.graph_insights.wait_for_completion(snapshot_id)
```

Read the snapshots and drop them again:

```pycon
>>> client.graph_insights.fetch_data()
>>> list(client.graph_insights)
>>> client.graph_insights.delete_item(snapshot_id)
```

**Classes:**

- [**GraphInsightDeleteConfig**](#cmem_client.repositories.graph_insights.GraphInsightDeleteConfig) – Graph Insight Snapshot Delete Configuration.
- [**GraphInsightUpdateConfig**](#cmem_client.repositories.graph_insights.GraphInsightUpdateConfig) – Graph Insight Snapshot Update Configuration.
- [**GraphInsightsRepository**](#cmem_client.repositories.graph_insights.GraphInsightsRepository) – Repository for the semspect Graph Insights extension.

## `GraphInsightDeleteConfig` {#cmem_client.repositories.graph_insights.GraphInsightDeleteConfig}

Bases: <code>[DeleteConfig](../../repositories/protocols/delete_item/index.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Graph Insight Snapshot Delete Configuration.

**Attributes:**

- **model_config** –

## `GraphInsightUpdateConfig` {#cmem_client.repositories.graph_insights.GraphInsightUpdateConfig}

Bases: <code>[UpdateConfig](../../repositories/protocols/update_item/index.md#cmem_client.repositories.protocols.update_item.UpdateConfig)</code>

Graph Insight Snapshot Update Configuration.

**Attributes:**

- **model_config** –

## `GraphInsightsRepository` {#cmem_client.repositories.graph_insights.GraphInsightsRepository}

```python
GraphInsightsRepository(client)
```

Bases: <code>[Repository](../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.Repository)[[GraphInsightSnapshot](../../models/graph_insight/index.md#cmem_client.models.graph_insight.GraphInsightSnapshot)]</code>, <code>[DeleteItemProtocol](../../repositories/protocols/delete_item/index.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[UpdateItemProtocol](../../repositories/protocols/update_item/index.md#cmem_client.repositories.protocols.update_item.UpdateItemProtocol)</code>

Repository for the semspect Graph Insights extension.

Does not auto-fetch on init because semspect is optional and may not be installed.
Call fetch_data() explicitly before iterating snapshots.

**Functions:**

- [**create**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.create) – Create or update a snapshot for the given graph IRI.
- [**delete_all**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.delete_all) – Delete all snapshots via the bulk DELETE endpoint.
- [**delete_item**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.delete_item) – Delete an item from the repository
- [**fetch_data**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.fetch_data) – Fetch all snapshots from the semspect status endpoint.
- [**get_status**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.get_status) – Fetch current status of a single snapshot.
- [**is_available**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.is_available) – Return True if the semspect extension is active and the user is allowed.
- [**items**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.keys) – Get the keys of the repository
- [**update_item**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.update_item) – Update an existing item in the repository.
- [**values**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.values) – Get the values of the repository
- [**wait_for_completion**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.wait_for_completion) – Poll until snapshot status is no longer ONGOING.

**Attributes:**

- [**logger**](#cmem_client.repositories.graph_insights.GraphInsightsRepository.logger) (<code>Logger</code>) – Gets the client logger

### `create` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.create}

```python
create(iri)
```

Create or update a snapshot for the given graph IRI.

**Parameters:**

- **iri** (<code>str</code>) – The graph IRI to create a snapshot for.

**Returns:**

- <code>str</code> – The snapshot ID returned by the server.

### `delete_all` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.delete_all}

```python
delete_all()
```

Delete all snapshots via the bulk DELETE endpoint.

### `delete_item` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.delete_item}

```python
delete_item(key, skip_if_missing=False, configuration=None)
```

Delete an item from the repository

**Parameters:**

- **key** (<code>str</code>) – The key of the item to delete
- **skip_if_missing** (<code>bool</code>) – If True, it is ignored if the deleted item even exists
- **configuration** (<code>DeleteItemConfig</code>) – Optional configuration for deletion

**Raises:**

- <code>[RepositoryModificationError](../../exceptions/index.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `fetch_data` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.fetch_data}

```python
fetch_data()
```

Fetch all snapshots from the semspect status endpoint.

### `get_status` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.get_status}

```python
get_status(snapshot_id)
```

Fetch current status of a single snapshot.

**Parameters:**

- **snapshot_id** (<code>str</code>) – The snapshot database ID.

**Returns:**

- <code>[GraphInsightSnapshot](../../models/graph_insight/index.md#cmem_client.models.graph_insight.GraphInsightSnapshot)</code> – A GraphInsightSnapshot with current status fields.

### `is_available` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.is_available}

```python
is_available()
```

Return True if the semspect extension is active and the user is allowed.

### `items` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `update_item` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.update_item}

```python
update_item(item, configuration=None)
```

Update an existing item in the repository.

**Parameters:**

- **item** (<code>[ItemType](../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to update in the repository.
- **configuration** (<code>[UpdateItemConfig_contra](../../repositories/protocols/update_item/index.md#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra) | None</code>) – Optional configuration for the update operation.

**Raises:**

- <code>[RepositoryModificationError](../../exceptions/index.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item does not exist or an error occurs.
- <code>HTTPError</code> – For any other HTTP error.

### `values` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.values}

```python
values()
```

Get the values of the repository

### `wait_for_completion` {#cmem_client.repositories.graph_insights.GraphInsightsRepository.wait_for_completion}

```python
wait_for_completion(snapshot_id, timeout=120.0, poll_interval=2.0)
```

Poll until snapshot status is no longer ONGOING.

**Parameters:**

- **snapshot_id** (<code>str</code>) – The snapshot database ID to wait for.
- **timeout** (<code>float</code>) – Maximum seconds to wait before raising TimeoutError.
- **poll_interval** (<code>float</code>) – Seconds between status checks.

**Returns:**

- <code>[GraphInsightSnapshot](../../models/graph_insight/index.md#cmem_client.models.graph_insight.GraphInsightSnapshot)</code> – The snapshot once it reaches a terminal state.

**Raises:**

- <code>TimeoutError</code> – if the snapshot is still ONGOING after timeout seconds.

