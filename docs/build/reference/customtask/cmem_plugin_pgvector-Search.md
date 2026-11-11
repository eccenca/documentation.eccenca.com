---
title: "Search Vector Embeddings"
description: "Search for the top-k nearest matches to a query embedding in Postgres Vector Store (PGVector)."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Search Vector Embeddings

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow task searches for the top-k nearest vectors stored in a collection in Postgres
Vector Store (PGVector).

Each incoming entity supplies a query embedding on the single input path. The task compares it
against the vectors in the configured collection and attaches the top-k nearest matches to the
entity as a JSON array on an additional output path, together with each match's metadata, its
stored embedding source, and its distance to the query.

The result is structured like this:

``` json
[
{
   "id": "...",
   "metadata": "..",
   "_embedding_source": "..",
   "distance": ".."
}
...
]
```

Use together with **Store Vector Embeddings**, which populates the collection this task searches.


## Parameter

### Database Host

The hostname of the postgres database service.

- ID: `host`
- Datatype: `string`
- Default Value: `pgvector`



### Database Port

The port number of the postgres database service.

- ID: `port`
- Datatype: `Long`
- Default Value: `5432`



### Database User

The account name used to login to the postgres database service.

- ID: `user`
- Datatype: `string`
- Default Value: `pgvector`



### Database Password

The password of the database account.

- ID: `password`
- Datatype: `password`
- Default Value: `None`



### Database Name

The database name.

- ID: `database`
- Datatype: `string`
- Default Value: `pgvector`



### Collection Name

The name of the collection in Postgres Vector Store (PGVector).

- ID: `collection_name`
- Datatype: `string`
- Default Value: `None`



### Search Result Path

The path containing the search result in the output entities.

- ID: `search_result_path`
- Datatype: `string`
- Default Value: `_search_result`



### Embedding Query Path

The path containing the query embedding to search with. Its value must be a string representation of a list of floats, e.g. `[0.1, 0.2, ...]`; the task fails if it cannot be parsed as one.

- ID: `embedding_query_path`
- Datatype: `string`
- Default Value: `_embedding`



### Top-k

The number of entries to be returned in the search result.

- ID: `top_k`
- Datatype: `Long`
- Default Value: `10`

## Advanced Parameter

### Distance Strategy

The distance strategy used to rank search matches.

- ID: `distance_strategy`
- Datatype: `enumeration`
- Default Value: `COSINE`
