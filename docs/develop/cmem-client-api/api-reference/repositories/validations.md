---
title: "cmem-client: validations module"
description: "Repository for the SHACL validation batches of Corporate Memory."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.validations` {#cmem_client.repositories.validations}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the SHACL validation batches of Corporate Memory.

Provides ValidationsRepository for starting a validation of a context graph against a
shape graph, for polling the batches which are running or finished, and for reading
their aggregated or detailed results.

**Examples:**

Start a validation and read its result:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> batch_id = client.validations.start(
...     context_graph="https://ns.eccenca.com/data/config/"
... )
>>> client.validations.get_aggregation(batch_id)
>>> client.validations.get_result(batch_id)
```

List the known batches and cancel a running one:

```pycon
>>> client.validations.fetch_data()
>>> list(client.validations)
>>> client.validations.cancel(batch_id)
```

**Classes:**

- [**ValidationsRepository**](#cmem_client.repositories.validations.ValidationsRepository) – Repository for managing SHACL batch validation processes.

## `ValidationsRepository` {#cmem_client.repositories.validations.ValidationsRepository}

```python
ValidationsRepository(client)
```

Bases: <code>[PlainListRepository](../repositories/base/plain_list.md#cmem_client.repositories.base.plain_list.PlainListRepository)[[ValidationAggregation](../models/validation.md#cmem_client.models.validation.ValidationAggregation)]</code>

Repository for managing SHACL batch validation processes.

The dict is keyed by batch ID and insertion order reflects execution start time.
Not auto-fetched on init — call fetch_data() explicitly to populate.
Use get_aggregation() to refresh the state of a single validation process,
e.g. when polling a running process.

**Functions:**

- [**cancel**](#cmem_client.repositories.validations.ValidationsRepository.cancel) – Cancel a running validation process.
- [**fetch_data**](#cmem_client.repositories.validations.ValidationsRepository.fetch_data) – Fetch simple list from a JSON endpoint via a type adapter
- [**get_aggregation**](#cmem_client.repositories.validations.ValidationsRepository.get_aggregation) – Fetch the aggregation summary of a single validation process fresh from the server.
- [**get_result**](#cmem_client.repositories.validations.ValidationsRepository.get_result) – Get the full result of a validation process including all violations.
- [**items**](#cmem_client.repositories.validations.ValidationsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.validations.ValidationsRepository.keys) – Get the keys of the repository
- [**start**](#cmem_client.repositories.validations.ValidationsRepository.start) – Start a new batch validation process.
- [**values**](#cmem_client.repositories.validations.ValidationsRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.validations.ValidationsRepository.logger) (<code>Logger</code>) – Gets the client logger

### `cancel` {#cmem_client.repositories.validations.ValidationsRepository.cancel}

```python
cancel(batch_id)
```

Cancel a running validation process.

**Parameters:**

- **batch_id** (<code>str</code>) – The batch validation process identifier.

### `fetch_data` {#cmem_client.repositories.validations.ValidationsRepository.fetch_data}

```python
fetch_data()
```

Fetch simple list from a JSON endpoint via a type adapter

Use this method to fetch data when your result set is an array of objects.

### `get_aggregation` {#cmem_client.repositories.validations.ValidationsRepository.get_aggregation}

```python
get_aggregation(batch_id)
```

Fetch the aggregation summary of a single validation process fresh from the server.

**Parameters:**

- **batch_id** (<code>str</code>) – The batch validation process identifier.

**Returns:**

- <code>[ValidationAggregation](../models/validation.md#cmem_client.models.validation.ValidationAggregation)</code> – The aggregation summary for the given process.

**Raises:**

- <code>[RepositoryReadError](../exceptions.md#cmem_client.exceptions.RepositoryReadError)</code> – if an error occurs while fetching the aggregation.

### `get_result` {#cmem_client.repositories.validations.ValidationsRepository.get_result}

```python
get_result(batch_id)
```

Get the full result of a validation process including all violations.

**Parameters:**

- **batch_id** (<code>str</code>) – The batch validation process identifier.

**Returns:**

- <code>[ValidationResult](../models/validation.md#cmem_client.models.validation.ValidationResult)</code> – The full validation result with all resource results and violations.

### `items` {#cmem_client.repositories.validations.ValidationsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.validations.ValidationsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.validations.ValidationsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `start` {#cmem_client.repositories.validations.ValidationsRepository.start}

```python
start(context_graph, shape_graph=None, query=None, result_graph=None, replace=False, ignore_graph=None)
```

Start a new batch validation process.

**Parameters:**

- **context_graph** (<code>str</code>) – IRI of the data graph to validate.
- **shape_graph** (<code>str | None</code>) – IRI of the shape catalog graph.
- **query** (<code>str | None</code>) – SPARQL query to select resources for validation.
- **result_graph** (<code>str | None</code>) – IRI of a graph to write validation results to.
- **replace** (<code>bool</code>) – Whether to replace the result graph instead of appending.
- **ignore_graph** (<code>list[str] | None</code>) – Graph IRIs excluded from resource selection.

**Returns:**

- <code>str</code> – The batch ID of the newly created validation process.

### `values` {#cmem_client.repositories.validations.ValidationsRepository.values}

```python
values()
```

Get the values of the repository

