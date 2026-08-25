# `queries` {#cmem_client.repositories.queries}

Repository for managing queries from the Corporate Memory query catalog.

Provides QueriesRepository class for accessing queries stored in RDF catalog graphs.
Queries are fetched using the query catalog REST API.

**Examples:**

Browse the catalog and fetch a single query:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> for url in client.queries:
...     print(url, client.queries[url].label)
>>> client.queries.get("https://ns.eccenca.com/data/queries/my-query")
```

Run a SPARQL query without storing it in the catalog:

```pycon
>>> client.queries.execute_query("SELECT ?s WHERE { ?s ?p ?o } LIMIT 10")
```

See the individual methods for executing, explaining and cancelling queries.

**Classes:**

- [**QueriesCreateConfig**](#cmem_client.repositories.queries.QueriesCreateConfig) – Configuration for creating queries.
- [**QueriesDeleteConfig**](#cmem_client.repositories.queries.QueriesDeleteConfig) – Configuration for deleting queries.
- [**QueriesExportConfig**](#cmem_client.repositories.queries.QueriesExportConfig) – Configuration for exporting queries.
- [**QueriesRepository**](#cmem_client.repositories.queries.QueriesRepository) – Repository for query catalog queries.
- [**QueriesUpdateConfig**](#cmem_client.repositories.queries.QueriesUpdateConfig) – Configuration for updating queries.

## `QueriesCreateConfig` {#cmem_client.repositories.queries.QueriesCreateConfig}

Bases: <code>[CreateConfig](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateConfig)</code>

Configuration for creating queries.

**Attributes:**

- [**catalog_graph**](#cmem_client.repositories.queries.QueriesCreateConfig.catalog_graph) (<code>str | None</code>) – URI of the query catalog graph to operate on. If None, the catalog graph
configured on the repository is used.

### `catalog_graph` {#cmem_client.repositories.queries.QueriesCreateConfig.catalog_graph}

```python
catalog_graph: str | None = None
```

### `model_config` {#cmem_client.repositories.queries.QueriesCreateConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `QueriesDeleteConfig` {#cmem_client.repositories.queries.QueriesDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Configuration for deleting queries.

**Attributes:**

- [**catalog_graph**](#cmem_client.repositories.queries.QueriesDeleteConfig.catalog_graph) (<code>str | None</code>) – URI of the query catalog graph to operate on. If None, the catalog graph
configured on the repository is used.

### `catalog_graph` {#cmem_client.repositories.queries.QueriesDeleteConfig.catalog_graph}

```python
catalog_graph: str | None = None
```

### `model_config` {#cmem_client.repositories.queries.QueriesDeleteConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `QueriesExportConfig` {#cmem_client.repositories.queries.QueriesExportConfig}

Bases: <code>[ExportConfig](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportConfig)</code>

Configuration for exporting queries.

**Attributes:**

- **model_config** –

## `QueriesRepository` {#cmem_client.repositories.queries.QueriesRepository}

```python
QueriesRepository(client, catalog_graph=None)
```

Bases: <code>[Repository](../repositories/base/abc.md#cmem_client.repositories.base.abc.Repository)</code>, <code>[CreateItemProtocol](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemProtocol)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[ExportItemProtocol](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportItemProtocol)</code>, <code>[UpdateItemProtocol](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemProtocol)</code>

Repository for query catalog queries.

This repository manages queries stored in Corporate Memory RDF catalog graphs.
Queries are described using the SHACL UI vocabulary and accessed via the
query catalog REST API endpoint.

The repository provides full CRUD operations (create, read, update, delete)
for catalog queries. For executing, explaining, or managing running queries,
use the appropriate service components.

**Attributes:**

- [**DEFAULT_CATALOG_GRAPH**](#cmem_client.repositories.queries.QueriesRepository.DEFAULT_CATALOG_GRAPH) (<code>str</code>) – Catalog graph used when neither the constructor nor an operation
configuration names one. Taken from ``Query.DEFAULT_NS``.

**Functions:**

- [**cancel_query**](#cmem_client.repositories.queries.QueriesRepository.cancel_query) – Cancel a running query.
- [**create_item**](#cmem_client.repositories.queries.QueriesRepository.create_item) – Create (add) a new item to the repository
- [**delete_all**](#cmem_client.repositories.queries.QueriesRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.queries.QueriesRepository.delete_item) – Delete an item from the repository
- [**execute_query**](#cmem_client.repositories.queries.QueriesRepository.execute_query) – Execute a SPARQL query and return results.
- [**explain_query**](#cmem_client.repositories.queries.QueriesRepository.explain_query) – Get the logical plan explanation for a SPARQL query.
- [**export_item**](#cmem_client.repositories.queries.QueriesRepository.export_item) – Export an item from the repository to a file path.
- [**fetch_data**](#cmem_client.repositories.queries.QueriesRepository.fetch_data) – Fetch queries from the catalog graph using the REST API.
- [**get**](#cmem_client.repositories.queries.QueriesRepository.get) – Get a query by its identifier.
- [**get_query_status**](#cmem_client.repositories.queries.QueriesRepository.get_query_status) – Get status of running and recently completed queries.
- [**items**](#cmem_client.repositories.queries.QueriesRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.queries.QueriesRepository.keys) – Get the keys of the repository
- [**raise_modification_error**](#cmem_client.repositories.queries.QueriesRepository.raise_modification_error) – Raise an exception if needed
- [**update_item**](#cmem_client.repositories.queries.QueriesRepository.update_item) – Update an existing item in the repository.
- [**values**](#cmem_client.repositories.queries.QueriesRepository.values) – Get the values of the repository

**Parameters:**

- **client** (<code>[Client](../index.md#cmem_client.client.Client)</code>) – The Corporate Memory client instance.
- **catalog_graph** (<code>str | None</code>) – URI of the catalog graph. If None, uses default catalog graph.

### `DEFAULT_CATALOG_GRAPH` {#cmem_client.repositories.queries.QueriesRepository.DEFAULT_CATALOG_GRAPH}

```python
DEFAULT_CATALOG_GRAPH: str = Query.DEFAULT_NS
```

### `cancel_query` {#cmem_client.repositories.queries.QueriesRepository.cancel_query}

```python
cancel_query(query_id)
```

Cancel a running query.

Attempts to cancel a query that is currently executing. The query
is identified by its execution ID (not its catalog URI).

**Parameters:**

- **query_id** (<code>str</code>) – Execution ID of the query to cancel (from get_query_status).

**Raises:**

- <code>HTTPStatusError</code> – If the cancel request fails (e.g., query
not found, already completed, or insufficient permissions).

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> [status.id for status in client.queries.get_query_status()]
```

Passing one of those IDs cancels that query. That call is described rather
than shown running: which queries are in flight depends on what the
deployment happens to be doing, and one which finishes between listing and
cancelling makes the cancel fail with a 404.

<details class="note" open markdown="1">
<summary>Note</summary>

This endpoint requires admin privileges in Corporate Memory.
Not all queries can be cancelled depending on their execution state.

</details>

### `create_item` {#cmem_client.repositories.queries.QueriesRepository.create_item}

```python
create_item(item, skip_if_existing=False, configuration=None)
```

Create (add) a new item to the repository

**Parameters:**

- **item** (<code>[ItemType](../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to add to the repository
- **skip_if_existing** (<code>bool</code>) – If true, creating already existing items will be ignored
- **configuration** (<code>[CreateItemConfig_contra](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra) | None</code>) – Optional configuration

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `delete_all` {#cmem_client.repositories.queries.QueriesRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.queries.QueriesRepository.delete_item}

```python
delete_item(key, skip_if_missing=False, configuration=None)
```

Delete an item from the repository

**Parameters:**

- **key** (<code>str</code>) – The key of the item to delete
- **skip_if_missing** (<code>bool</code>) – If True, it is ignored if the deleted item even exists
- **configuration** (<code>DeleteItemConfig</code>) – Optional configuration for deletion

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `execute_query` {#cmem_client.repositories.queries.QueriesRepository.execute_query}

```python
execute_query(query, accept=None, owl_imports_resolution=True, base64_encoded=False, distinct=False, limit=None, offset=None, timeout=None)
```

Execute a SPARQL query and return results.

Executes a SPARQL query (SELECT, ASK, DESCRIBE, CONSTRUCT) or update
operation (INSERT, DELETE, etc.) and returns the raw response.

**Parameters:**

- **query** (<code>str | [Query](../models/query_catalog.md#cmem_client.models.query_catalog.Query)</code>) – SPARQL query string or Query object to execute.
- **accept** (<code>str | None</code>) – Accept header for response format. If None, uses default based
on query type (text/csv for SELECT, text/turtle for DESCRIBE, etc.).
- **owl_imports_resolution** (<code>bool</code>) – Enable owl:imports resolution (default: True).
When enabled, graphs that import other graphs via owl:imports will

be queried as merged overall-graphs.

- **base64_encoded** (<code>bool</code>) – Enable base64 encoding of query parameter (default: False).
Useful when aggressive firewalls block SPARQL queries.
- **distinct** (<code>bool</code>) – Override SELECT query to make result set DISTINCT (default: False).
- **limit** (<code>int | None</code>) – Override or set LIMIT in SELECT query.
- **offset** (<code>int | None</code>) – Override or set OFFSET in SELECT query.
- **timeout** (<code>int | None</code>) – Max execution time in milliseconds.

**Returns:**

- <code>str</code> – Raw query results as string in the requested format.

**Raises:**

- <code>HTTPStatusError</code> – If the query execution fails.
- <code>ValueError</code> – If query text is invalid or placeholders are unfilled.

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> results = client.queries.execute_query("SELECT * WHERE { ?s ?p ?o } LIMIT 10")
>>> print(results)
```

<details class="note" open markdown="1">
<summary>Note</summary>

For parameterized queries with placeholders, use Query object with
fill_placeholders() first, or use get() to fetch from catalog.

</details>

### `explain_query` {#cmem_client.repositories.queries.QueriesRepository.explain_query}

```python
explain_query(query)
```

Get the logical plan explanation for a SPARQL query.

Calls the query catalog API to get the logical plan for a given SPARQL query,
which provides information about query optimization, execution order, and
estimated complexity.

The logical plan includes:

- Optimization groups and their evaluation order
- Collection sizes and complexity estimates
- Unique subject and object counts
- Estimated number of iterations

**Parameters:**

- **query** (<code>str | [Query](../models/query_catalog.md#cmem_client.models.query_catalog.Query)</code>) – The SPARQL query string or Query object to explain.

**Returns:**

- <code>[LogicalPlan](../models/query_catalog.md#cmem_client.models.query_catalog.LogicalPlan)</code> – A LogicalPlan object containing the formatted query execution plan.

**Raises:**

- <code>HTTPStatusError</code> – If the API request fails due to HTTP errors.
- <code>RequestError</code> – If the API request fails due to network errors.

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> plan = client.queries.explain_query("SELECT * WHERE { ?s ?p ?o }")
>>> print(plan.plan)
```

<details class="note" open markdown="1">
<summary>Note</summary>

This operation analyzes the query structure and provides an execution
plan without actually executing the query against data.

</details>

### `export_item` {#cmem_client.repositories.queries.QueriesRepository.export_item}

```python
export_item(key, path=None, replace=False, configuration=None)
```

Export an item from the repository to a file path.

**Parameters:**

- **key** (<code>str</code>) – The key identifying the item to export.
- **path** (<code>Path | None</code>) – The target file path for export. If None, a path will be generated.
- **replace** (<code>bool</code>) – Whether to replace existing files at the target path.
- **configuration** (<code>[ExportItemConfig_contra](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportItemConfig_contra) | None</code>) – Optional configuration for export behavior.

**Returns:**

- <code>Path</code> – The actual path where the item was exported.

**Raises:**

- <code>[RepositoryItemNotFoundError](../exceptions.md#cmem_client.exceptions.RepositoryItemNotFoundError)</code> – If the specified item key is not found.
- <code>[RepositoryReadError](../exceptions.md#cmem_client.exceptions.RepositoryReadError)</code> – If there's an error during export or path mismatch.

### `fetch_data` {#cmem_client.repositories.queries.QueriesRepository.fetch_data}

```python
fetch_data(catalog_graph=None, lang_pref='en')
```

Fetch queries from the catalog graph using the REST API.

**Parameters:**

- **catalog_graph** (<code>str | None</code>) – URI of the catalog graph. If None, uses the graph
specified during initialization.
- **lang_pref** (<code>str</code>) – Language preference for labels (default: "en").

**Raises:**

- <code>HTTPStatusError</code> – If fetching the catalog fails.

### `get` {#cmem_client.repositories.queries.QueriesRepository.get}

```python
get(key, default=None, catalog_graph=None)
```

Get a query by its identifier.

Supports multiple identifier formats:

- Full URI: <https://ns.eccenca.com/data/queries/myQuery>
- Short URI (qname): :myQuery (uses default namespace)

Note: File paths are not supported. For file-based queries, create a
Query object directly by reading the file content.

**Parameters:**

- **key** (<code>str</code>) – Query identifier (full URI or short URI).
- **default** (<code>[Query](../models/query_catalog.md#cmem_client.models.query_catalog.Query) | None</code>) – Value to return if the query is not found.
- **catalog_graph** (<code>str | None</code>) – URI of the catalog graph. If None, uses the graph
specified during initialization.

**Returns:**

- <code>[Query](../models/query_catalog.md#cmem_client.models.query_catalog.Query) | None</code> – The Query object if found, otherwise the default value.

### `get_query_status` {#cmem_client.repositories.queries.QueriesRepository.get_query_status}

```python
get_query_status()
```

Get status of running and recently completed queries.

Retrieves information about currently executing and recently finished
queries, including timing data, user information, and trace IDs.

**Returns:**

- <code>list[[QueryStatus](../models/query_catalog.md#cmem_client.models.query_catalog.QueryStatus)]</code> – List of QueryStatus objects for active/recent queries.

**Raises:**

- <code>HTTPStatusError</code> – If the status request fails.

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> statuses = client.queries.get_query_status()
>>> for status in statuses:
...     print(f"{status.id}: {status.status}")
```

<details class="note" open markdown="1">
<summary>Note</summary>

This endpoint requires admin privileges in Corporate Memory.

</details>

### `items` {#cmem_client.repositories.queries.QueriesRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.queries.QueriesRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.queries.QueriesRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `raise_modification_error` {#cmem_client.repositories.queries.QueriesRepository.raise_modification_error}

```python
raise_modification_error(response)
```

Raise an exception if needed

### `update_item` {#cmem_client.repositories.queries.QueriesRepository.update_item}

```python
update_item(item, configuration=None)
```

Update an existing item in the repository.

**Parameters:**

- **item** (<code>[ItemType](../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to update in the repository.
- **configuration** (<code>[UpdateItemConfig_contra](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra) | None</code>) – Optional configuration for the update operation.

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item does not exist or an error occurs.
- <code>HTTPError</code> – For any other HTTP error.

### `values` {#cmem_client.repositories.queries.QueriesRepository.values}

```python
values()
```

Get the values of the repository

## `QueriesUpdateConfig` {#cmem_client.repositories.queries.QueriesUpdateConfig}

Bases: <code>[UpdateConfig](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateConfig)</code>

Configuration for updating queries.

**Attributes:**

- [**catalog_graph**](#cmem_client.repositories.queries.QueriesUpdateConfig.catalog_graph) (<code>str | None</code>) – URI of the query catalog graph to operate on. If None, the catalog graph
configured on the repository is used.

### `catalog_graph` {#cmem_client.repositories.queries.QueriesUpdateConfig.catalog_graph}

```python
catalog_graph: str | None = None
```

### `model_config` {#cmem_client.repositories.queries.QueriesUpdateConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

