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

### Pre Delete Collection

If set to true, then the collection will removed at the beginning.

- ID: `pre_delete_collection`
- Datatype: `boolean`
- Default Value: `true`

## Advanced Parameter

### Source Path

The name of the path to use for reading the embedding source.

- ID: `source_path`
- Datatype: `string`
- Default Value: `_embedding_source`

### Embedding Path

The name of the path to use for reading the embeddings.

- ID: `embedding_path`
- Datatype: `string`
- Default Value: `_embedding`

### Metadata Paths

The comma separated list path names to be used as metadata. Empty name means all paths (except embedding source and embedding) will be used

- ID: `metadata_paths`
- Datatype: `string`
- Default Value: `None`

### Batch Processing Size

The number of entries to be processed in batch.

- ID: `batch_processing_size`
- Datatype: `Long`
- Default Value: `100`
