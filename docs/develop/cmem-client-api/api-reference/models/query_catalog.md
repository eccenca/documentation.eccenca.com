---
title: "cmem-client: query_catalog module"
description: "Models for query catalog operations."
tags:
  - API
  - Python
  - cmem-client
---

# `query_catalog` {#cmem_client.models.query_catalog}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Models for query catalog operations.

This module provides data models for query catalog operations including
query explanation, execution, status tracking, and catalog management.

The queries stored in the catalog are the items of ``client.queries``, keyed by their
URL. A query carries its own text, so it knows its type and its ``{{placeholder}}``
parameters without asking the server, and the same model is used for a query which was
never in the catalog at all, read from a file or built from a string.

**Classes:**

- [**LogicalPlan**](#cmem_client.models.query_catalog.LogicalPlan) – Logical plan explanation for a SPARQL query.
- [**Query**](#cmem_client.models.query_catalog.Query) – A SPARQL query with metadata and placeholder support.
- [**QueryOrigin**](#cmem_client.models.query_catalog.QueryOrigin) – Origin of a query.
- [**QueryStatus**](#cmem_client.models.query_catalog.QueryStatus) – Status information for a running or completed query.
- [**QueryType**](#cmem_client.models.query_catalog.QueryType) – SPARQL query type enumeration.

## `LogicalPlan` {#cmem_client.models.query_catalog.LogicalPlan}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Logical plan explanation for a SPARQL query.

Represents the query execution plan returned by the query catalog API,
which provides information about query optimization, execution order,
and estimated complexity.

**Attributes:**

- [**plan**](#cmem_client.models.query_catalog.LogicalPlan.plan) (<code>str</code>) – The formatted query execution plan showing optimization groups,
collection sizes, complexity estimates, and iteration counts.

### `model_config` {#cmem_client.models.query_catalog.LogicalPlan.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `plan` {#cmem_client.models.query_catalog.LogicalPlan.plan}

```python
plan: str
```

The formatted query execution plan as a string.

## `Query` {#cmem_client.models.query_catalog.Query}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A SPARQL query with metadata and placeholder support.

Represents a SPARQL query with support for parameterization using
mustache-like syntax ({{placeholder}}). Includes query type detection,
placeholder management, and execution configuration.

**Attributes:**

- [**text**](#cmem_client.models.query_catalog.Query.text) (<code>str</code>) – The SPARQL query text, potentially containing placeholders.
- [**url**](#cmem_client.models.query_catalog.Query.url) (<code>str</code>) – URI identifying this query in the query catalog (auto-generated if not provided).
- [**label**](#cmem_client.models.query_catalog.Query.label) (<code>str | None</code>) – Optional human-readable label for the query.
- [**query_type**](#cmem_client.models.query_catalog.Query.query_type) (<code>[QueryType](#cmem_client.models.query_catalog.QueryType)</code>) – The detected or specified query type (SELECT, UPDATE, etc.).
- [**description**](#cmem_client.models.query_catalog.Query.description) (<code>str | None</code>) – Optional description of the query's purpose.
- [**origin**](#cmem_client.models.query_catalog.Query.origin) (<code>[QueryOrigin](#cmem_client.models.query_catalog.QueryOrigin)</code>) – Where the query came from (remote, file, text).
- [**short_url**](#cmem_client.models.query_catalog.Query.short_url) (<code>str | None</code>) – Shortened URL with default namespace prefix (e.g., :uuid).

**Functions:**

- [**detect_query_type**](#cmem_client.models.query_catalog.Query.detect_query_type) – Detect the query type by parsing the query text.
- [**fill_placeholders**](#cmem_client.models.query_catalog.Query.fill_placeholders) – Replace placeholders with provided values.
- [**generate_url_if_missing**](#cmem_client.models.query_catalog.Query.generate_url_if_missing) – Generate a URL if none provided.
- [**get_default_accept_header**](#cmem_client.models.query_catalog.Query.get_default_accept_header) – Get the default Accept header for this query type.
- [**get_editor_url**](#cmem_client.models.query_catalog.Query.get_editor_url) – Get the Corporate Memory query editor URL for this query.
- [**get_id**](#cmem_client.models.query_catalog.Query.get_id) – Get the query URL as its identifier.
- [**get_placeholder_keys**](#cmem_client.models.query_catalog.Query.get_placeholder_keys) – Get all placeholder keys from the query text.

### `DEFAULT_NS` {#cmem_client.models.query_catalog.Query.DEFAULT_NS}

```python
DEFAULT_NS: str = 'https://ns.eccenca.com/data/queries/'
```

### `description` {#cmem_client.models.query_catalog.Query.description}

```python
description: str | None = None
```

### `detect_query_type` {#cmem_client.models.query_catalog.Query.detect_query_type}

```python
detect_query_type(text=None)
```

Detect the query type by parsing the query text.

Uses rdflib's SPARQL parser to determine if this is a SELECT, ASK,
DESCRIBE, CONSTRUCT, or UPDATE query.

**Parameters:**

- **text** (<code>str | None</code>) – Optional query text to parse. If None, uses self.text.

**Returns:**

- <code>[QueryType](#cmem_client.models.query_catalog.QueryType)</code> – Detected QueryType, or QueryType.UNKNOWN if detection fails.

**Examples:**

```pycon
>>> query = Query(text="SELECT * { ?s ?p ?o }")
>>> query.detect_query_type()
<QueryType.SELECT: 'SELECT'>
```

### `fill_placeholders` {#cmem_client.models.query_catalog.Query.fill_placeholders}

```python
fill_placeholders(placeholders)
```

Replace placeholders with provided values.

**Parameters:**

- **placeholders** (<code>dict[str, str]</code>) – Dictionary mapping placeholder keys to values.

**Returns:**

- <code>str</code> – Query text with all placeholders replaced.

**Raises:**

- <code>ValueError</code> – If not all placeholders are filled.

**Examples:**

```pycon
>>> query = Query(text="SELECT * { ?s ?p {{value}} }")
>>> query.fill_placeholders({"value": '"test"'})
'SELECT * { ?s ?p "test" }'
```

### `generate_url_if_missing` {#cmem_client.models.query_catalog.Query.generate_url_if_missing}

```python
generate_url_if_missing(v)
```

Generate a URL if none provided.

### `get_default_accept_header` {#cmem_client.models.query_catalog.Query.get_default_accept_header}

```python
get_default_accept_header()
```

Get the default Accept header for this query type.

Returns appropriate MIME type based on query type, biased towards
formats suitable for command-line display.

**Returns:**

- <code>str</code> – Accept header string (e.g., "text/csv", "text/turtle").

**Examples:**

```pycon
>>> query = Query(text="SELECT * { ?s ?p ?o }", query_type=QueryType.SELECT)
>>> query.get_default_accept_header()
'text/csv'
```

### `get_editor_url` {#cmem_client.models.query_catalog.Query.get_editor_url}

```python
get_editor_url(base_url, graph=None)
```

Get the Corporate Memory query editor URL for this query.

Generates a URL to open the query in Corporate Memory's web-based
SPARQL query editor.

**Parameters:**

- **base_url** (<code>str</code>) – Base URL of Corporate Memory instance (required).
- **graph** (<code>str | None</code>) – Catalog graph URI for remote queries (default: DEFAULT_NS).

**Returns:**

- <code>str</code> – URL string to open query in the web editor.

**Examples:**

```pycon
>>> query = Query(text="SELECT * { ?s ?p ?o }", origin=QueryOrigin.TEXT)
>>> url = query.get_editor_url(base_url="https://cmem.example.com")
>>> "queryString" in url
True
```

### `get_id` {#cmem_client.models.query_catalog.Query.get_id}

```python
get_id()
```

Get the query URL as its identifier.

**Returns:**

- <code>str</code> – The query URL (IRI) that uniquely identifies this query in the catalog.

### `get_placeholder_keys` {#cmem_client.models.query_catalog.Query.get_placeholder_keys}

```python
get_placeholder_keys(text=None)
```

Get all placeholder keys from the query text.

Placeholders use mustache-like syntax: {{placeholder_name}}

**Parameters:**

- **text** (<code>str | None</code>) – Optional text to scan. If None, uses self.text.

**Returns:**

- <code>set[str]</code> – Set of placeholder key names found in the text.

**Examples:**

```pycon
>>> query = Query(text="SELECT * { ?s ?p {{value}} }")
>>> query.get_placeholder_keys()
{'value'}
```

### `label` {#cmem_client.models.query_catalog.Query.label}

```python
label: str | None = None
```

### `model_config` {#cmem_client.models.query_catalog.Query.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `origin` {#cmem_client.models.query_catalog.Query.origin}

```python
origin: QueryOrigin = QueryOrigin.UNKNOWN
```

### `query_type` {#cmem_client.models.query_catalog.Query.query_type}

```python
query_type: QueryType = QueryType.UNKNOWN
```

### `short_url` {#cmem_client.models.query_catalog.Query.short_url}

```python
short_url: str | None = None
```

### `text` {#cmem_client.models.query_catalog.Query.text}

```python
text: str
```

### `url` {#cmem_client.models.query_catalog.Query.url}

```python
url: str = ''
```

## `QueryOrigin` {#cmem_client.models.query_catalog.QueryOrigin}

Bases: <code>StrEnum</code>

Origin of a query.

Indicates where the query came from for tracking and editor URL generation.

**Attributes:**

- [**FILE**](#cmem_client.models.query_catalog.QueryOrigin.FILE) –
- [**REMOTE**](#cmem_client.models.query_catalog.QueryOrigin.REMOTE) –
- [**TEXT**](#cmem_client.models.query_catalog.QueryOrigin.TEXT) –
- [**UNKNOWN**](#cmem_client.models.query_catalog.QueryOrigin.UNKNOWN) –

### `FILE` {#cmem_client.models.query_catalog.QueryOrigin.FILE}

```python
FILE = 'file'
```

### `REMOTE` {#cmem_client.models.query_catalog.QueryOrigin.REMOTE}

```python
REMOTE = 'remote'
```

### `TEXT` {#cmem_client.models.query_catalog.QueryOrigin.TEXT}

```python
TEXT = 'text'
```

### `UNKNOWN` {#cmem_client.models.query_catalog.QueryOrigin.UNKNOWN}

```python
UNKNOWN = 'unknown'
```

## `QueryStatus` {#cmem_client.models.query_catalog.QueryStatus}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Status information for a running or completed query.

Represents the execution status of a query including timing information,
user context, and trace identifiers for debugging.

The API returns camelCase field names which are automatically converted to
snake_case Python attributes using Pydantic field aliases.

**Attributes:**

- [**id**](#cmem_client.models.query_catalog.QueryStatus.id) (<code>str | None</code>) – Unique identifier for this query execution.
- [**query_string**](#cmem_client.models.query_catalog.QueryStatus.query_string) (<code>str | None</code>) – The query text that was executed.
- [**graph**](#cmem_client.models.query_catalog.QueryStatus.graph) (<code>str | None</code>) – Graph URI the query was executed against.
- [**user**](#cmem_client.models.query_catalog.QueryStatus.user) (<code>str | None</code>) – User who executed the query.
- [**trace_id**](#cmem_client.models.query_catalog.QueryStatus.trace_id) (<code>str | None</code>) – Trace identifier for debugging.
- [**start_time**](#cmem_client.models.query_catalog.QueryStatus.start_time) (<code>int | None</code>) – When the query started execution (milliseconds).
- [**execution_time**](#cmem_client.models.query_catalog.QueryStatus.execution_time) (<code>int | None</code>) – How long the query took to execute (milliseconds).
- [**affected_graphs**](#cmem_client.models.query_catalog.QueryStatus.affected_graphs) (<code>list[str] | None</code>) – Graph URIs an update query wrote to. Empty for a read query.
- [**status**](#cmem_client.models.query_catalog.QueryStatus.status) (<code>str | None</code>) – Current status (e.g., "running", "completed").

### `affected_graphs` {#cmem_client.models.query_catalog.QueryStatus.affected_graphs}

```python
affected_graphs: list[str] | None = Field(default=None, alias='affectedGraphs')
```

### `execution_time` {#cmem_client.models.query_catalog.QueryStatus.execution_time}

```python
execution_time: int | None = Field(default=None, alias='executionTime')
```

### `graph` {#cmem_client.models.query_catalog.QueryStatus.graph}

```python
graph: str | None = None
```

### `id` {#cmem_client.models.query_catalog.QueryStatus.id}

```python
id: str | None = None
```

### `model_config` {#cmem_client.models.query_catalog.QueryStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `query_string` {#cmem_client.models.query_catalog.QueryStatus.query_string}

```python
query_string: str | None = Field(default=None, alias='queryString')
```

### `start_time` {#cmem_client.models.query_catalog.QueryStatus.start_time}

```python
start_time: int | None = Field(default=None, alias='startTime')
```

### `status` {#cmem_client.models.query_catalog.QueryStatus.status}

```python
status: str | None = None
```

### `trace_id` {#cmem_client.models.query_catalog.QueryStatus.trace_id}

```python
trace_id: str | None = Field(default=None, alias='traceId')
```

### `user` {#cmem_client.models.query_catalog.QueryStatus.user}

```python
user: str | None = None
```

## `QueryType` {#cmem_client.models.query_catalog.QueryType}

Bases: <code>StrEnum</code>

SPARQL query type enumeration.

Categorizes queries into read operations (SELECT, ASK, DESCRIBE, CONSTRUCT)
and update operations (UPDATE, DELETE, INSERT, etc.).

**Functions:**

- [**is_read_query**](#cmem_client.models.query_catalog.QueryType.is_read_query) – Check if this is a read query type.
- [**is_update_query**](#cmem_client.models.query_catalog.QueryType.is_update_query) – Check if this is an update query type.
- [**read_types**](#cmem_client.models.query_catalog.QueryType.read_types) – Get all read query types (SELECT, ASK, DESCRIBE, CONSTRUCT).
- [**update_types**](#cmem_client.models.query_catalog.QueryType.update_types) – Get all update query types.

**Attributes:**

- [**ADD**](#cmem_client.models.query_catalog.QueryType.ADD) –
- [**ASK**](#cmem_client.models.query_catalog.QueryType.ASK) –
- [**CLEAR**](#cmem_client.models.query_catalog.QueryType.CLEAR) –
- [**CONSTRUCT**](#cmem_client.models.query_catalog.QueryType.CONSTRUCT) –
- [**COPY**](#cmem_client.models.query_catalog.QueryType.COPY) –
- [**CREATE**](#cmem_client.models.query_catalog.QueryType.CREATE) –
- [**DELETE**](#cmem_client.models.query_catalog.QueryType.DELETE) –
- [**DESCRIBE**](#cmem_client.models.query_catalog.QueryType.DESCRIBE) –
- [**DROP**](#cmem_client.models.query_catalog.QueryType.DROP) –
- [**FAULTY**](#cmem_client.models.query_catalog.QueryType.FAULTY) –
- [**INSERT**](#cmem_client.models.query_catalog.QueryType.INSERT) –
- [**LOAD**](#cmem_client.models.query_catalog.QueryType.LOAD) –
- [**MOVE**](#cmem_client.models.query_catalog.QueryType.MOVE) –
- [**SELECT**](#cmem_client.models.query_catalog.QueryType.SELECT) –
- [**UNKNOWN**](#cmem_client.models.query_catalog.QueryType.UNKNOWN) –
- [**UPDATE**](#cmem_client.models.query_catalog.QueryType.UPDATE) –

### `ADD` {#cmem_client.models.query_catalog.QueryType.ADD}

```python
ADD = 'ADD'
```

### `ASK` {#cmem_client.models.query_catalog.QueryType.ASK}

```python
ASK = 'ASK'
```

### `CLEAR` {#cmem_client.models.query_catalog.QueryType.CLEAR}

```python
CLEAR = 'CLEAR'
```

### `CONSTRUCT` {#cmem_client.models.query_catalog.QueryType.CONSTRUCT}

```python
CONSTRUCT = 'CONSTRUCT'
```

### `COPY` {#cmem_client.models.query_catalog.QueryType.COPY}

```python
COPY = 'COPY'
```

### `CREATE` {#cmem_client.models.query_catalog.QueryType.CREATE}

```python
CREATE = 'CREATE'
```

### `DELETE` {#cmem_client.models.query_catalog.QueryType.DELETE}

```python
DELETE = 'DELETE'
```

### `DESCRIBE` {#cmem_client.models.query_catalog.QueryType.DESCRIBE}

```python
DESCRIBE = 'DESCRIBE'
```

### `DROP` {#cmem_client.models.query_catalog.QueryType.DROP}

```python
DROP = 'DROP'
```

### `FAULTY` {#cmem_client.models.query_catalog.QueryType.FAULTY}

```python
FAULTY = 'FAULTY'
```

### `INSERT` {#cmem_client.models.query_catalog.QueryType.INSERT}

```python
INSERT = 'INSERT'
```

### `LOAD` {#cmem_client.models.query_catalog.QueryType.LOAD}

```python
LOAD = 'LOAD'
```

### `MOVE` {#cmem_client.models.query_catalog.QueryType.MOVE}

```python
MOVE = 'MOVE'
```

### `SELECT` {#cmem_client.models.query_catalog.QueryType.SELECT}

```python
SELECT = 'SELECT'
```

### `UNKNOWN` {#cmem_client.models.query_catalog.QueryType.UNKNOWN}

```python
UNKNOWN = 'UNKNOWN'
```

### `UPDATE` {#cmem_client.models.query_catalog.QueryType.UPDATE}

```python
UPDATE = 'UPDATE'
```

### `is_read_query` {#cmem_client.models.query_catalog.QueryType.is_read_query}

```python
is_read_query()
```

Check if this is a read query type.

### `is_update_query` {#cmem_client.models.query_catalog.QueryType.is_update_query}

```python
is_update_query()
```

Check if this is an update query type.

### `read_types` {#cmem_client.models.query_catalog.QueryType.read_types}

```python
read_types()
```

Get all read query types (SELECT, ASK, DESCRIBE, CONSTRUCT).

### `update_types` {#cmem_client.models.query_catalog.QueryType.update_types}

```python
update_types()
```

Get all update query types.

