---
title: "Store Vector Embeddings"
description: "Store embeddings into Postgres Vector Store (PGVector)."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Store Vector Embeddings
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This plugin workflow store embeddings into Postgres Vector Store.

The vector embeddings and its respective metadata are going to be stored into a collection inside
the Postgres Vector Store.
It is possible to specify either the name of the attributes containing the vectors as well as the
metadata.


## Parameter

### Database Host

The hostname of the postgres database service.

- Datatype: `string`
- Default Value: `pgvector`



### Database Port

The port number of the postgres database service.

- Datatype: `Long`
- Default Value: `5432`



### Database User

The account name used to login to the postgres database service.

- Datatype: `string`
- Default Value: `pgvector`



### Database Password

The password of the database account.

- Datatype: `password`
- Default Value: `None`



### Database Name

The database name.

- Datatype: `string`
- Default Value: `pgvector`



### Collection Name

The name of the collection that will be used for search.

- Datatype: `string`
- Default Value: `None`



### Pre Delete Collection

If set to true, then the collection will removed at the beginning.

- Datatype: `boolean`
- Default Value: `true`



### Source Path

The name of the path to use for reading the embedding source.

- Datatype: `string`
- Default Value: `_embedding_source`



### Embedding Path

The name of the path to use for reading the embeddings.

- Datatype: `string`
- Default Value: `_embedding`



### Metadata Paths

The comma separated list path names to be used as metadata. Empty name means all paths (except embedding source and embedding) will be used

- Datatype: `string`
- Default Value: `None`



### Batch Processing Size

The number of entries to be processed in batch.

- Datatype: `Long`
- Default Value: `100`



