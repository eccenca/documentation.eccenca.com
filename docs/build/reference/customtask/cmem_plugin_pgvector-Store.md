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


This workflow task stores embeddings and their metadata into a collection in Postgres Vector
Store (PGVector).

The task accepts entities of any schema on its input port. Two of the incoming paths supply the
text and the embedding to store; every other path, or a fixed subset of them, is stored alongside
as metadata. The task produces no output port: it is a terminal step and hands nothing on to
later tasks in the workflow.

Use together with **Search Vector Embeddings**, which reads back the collection this task
populates.

If the incoming entities have no path configured for the text or the embedding, the task fails
before storing anything.


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



### Pre Delete Collection

If enabled, deletes any existing collection with the same name before storing, discarding its previous contents. If disabled, new vectors are added to whatever the collection already contains.

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

The name of the path to use for reading the embeddings. Its value must be a string representation of a list of floats, e.g. `[0.1, 0.2, ...]`.

- ID: `embedding_path`
- Datatype: `string`
- Default Value: `_embedding`



### Metadata Paths

The comma-separated list of path names to store as metadata. An empty value means every path except the source and embedding paths is used.

- ID: `metadata_paths`
- Datatype: `string`
- Default Value: `None`



### Batch Processing Size

The number of entries to accumulate before writing them to the database as one batch.

- ID: `batch_processing_size`
- Datatype: `Long`
- Default Value: `100`
