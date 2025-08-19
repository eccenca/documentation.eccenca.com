---
title: "Search Vector Embeddings"
description: "Search for top-k metadata stored in Postgres Vector Store (PGVector)."
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


This workflow task search for the top-k metadata stored into Postgres Vector Store.

The incoming embedding entities are used to retrieve the nearest top-k
vectors in the collection stored in the Postgres Vector Store.
It is possible to specify which paths are going to be used for searching as well as which Postgres
Vector Store and collection name.

The task uses the embeddings from the path configured with the Embedding Query Path
parameter (`embedding_query_path`, default value: `_embedding`) to search over the collection.
The results are provided in the output path configured with the Search Result Path parameter
(`search_result_path`, default value: `_search_result`).

The results in this output are structured like this:

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

The name of the collection that will be used for search.

- ID: `collection_name`
- Datatype: `string`
- Default Value: `None`



### Search Result Path

The path containing the search result in the output entities.

- ID: `search_result_path`
- Datatype: `string`
- Default Value: `_search_result`



### Embedding Query Path

The path containing the embedding to be used for searching.

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

The distance strategy to use. (default: COSINE)

- ID: `distance_strategy`
- Datatype: `enumeration`
- Default Value: `COSINE`



