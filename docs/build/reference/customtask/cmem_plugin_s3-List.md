---
title: "List S3 objects"
description: "List the objects of a bucket in S3 or S3-compatible object storage."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# List S3 objects

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Lists the objects of a bucket, together with the metadata the service reports for
them.

## Ports

The task takes no input. It emits one entity per object, carrying the `bucket` it
was found in, its full `key`, the `name` that key ends in, its `size` in bytes,
its `etag`, the `last_modified` timestamp and the `storage_class`. Keys ending in
a slash are folder markers rather than content and are left out.

## Where the task sits

**Download S3 objects** accepts these entities on its input port, so a workflow
can list first, narrow the result down with transformations in between, and fetch
only what is left. The `etag` travels with each entity and is what lets the
download notice an object that changed in the meantime.

Listing is also a way to write an inventory of a bucket into a Knowledge Graph
without moving any of its content.

## Caveats

- **The listing streams.** Entities are produced while the service is still being
  paged through, so a bucket with millions of keys does not have to be held in
  memory - but neither is the total known in advance, and the entity count in the
  report grows as the run proceeds.
- **A regular expression is applied after the fact.** The key prefix is the only
  filter the service itself applies; everything the expression rejects has
  already been listed and paid for.
- **The preview stops after ten objects.** It therefore never reaches an object
  further down that a real run would reject or fail on.
- **An object's size and timestamp are the service's.** They are written down as
  reported, not checked against the bytes.


## Parameter

### Endpoint URL

The address of the service, e.g. `https://minio.example.org`. Leave empty for Amazon S3, which is then addressed by region.

- ID: `endpoint_url`
- Datatype: `string`
- Default Value: `None`



### Region

The region the bucket lives in. Amazon S3 needs the bucket's own region; most other implementations accept any value and ignore it.

- ID: `region`
- Datatype: `string`
- Default Value: `us-east-1`



### Credentials

Where the credentials come from.

- ID: `credentials`
- Datatype: `string`
- Default Value: `explicit`



### Access key ID

The access key to sign requests with.

- ID: `access_key_id`
- Datatype: `string`
- Default Value: `None`



### Secret access key

The secret belonging to the access key.

- ID: `secret_access_key`
- Datatype: `password`
- Default Value: `None`



### Bucket

The bucket whose objects are listed.

- ID: `bucket`
- Datatype: `string`
- Default Value: `None`



### Key prefix

Lists only the objects whose key starts with this, e.g. `raw/2026/`. The service applies it, so it is the cheapest way to narrow a large bucket down. Empty means the whole bucket.

- ID: `prefix`
- Datatype: `string`
- Default Value: `None`



### Regular expression

Lists only the objects whose key matches this regular expression, e.g. `\.csv$`. It is matched against the whole key rather than against the name alone, and it has to match somewhere in it rather than all of it. Empty means every key.

- ID: `regex`
- Datatype: `string`
- Default Value: `None`



### Top level only

If enabled, only the keys directly below the prefix are considered and everything nested deeper is folded away. The service does the folding, on a `/` delimiter.

- ID: `top_level_only`
- Datatype: `boolean`
- Default Value: `false`



### Limit

The maximum number of objects to list, or 0 for no limit. A run that stops at the limit says so in its report.

- ID: `limit`
- Datatype: `Long`
- Default Value: `0`

## Advanced Parameter

### Session token

The session token of a temporary credential. Needed only for keys issued by a token service, which expire.

- ID: `session_token`
- Datatype: `password`
- Default Value: `None`



### Bucket addressing style

How the bucket is named in a request.

- ID: `addressing_style`
- Datatype: `string`
- Default Value: `auto`



### Verify TLS connection

If enabled, the certificate of the service is verified. Disable only when connecting to a service with a self-signed or otherwise untrusted certificate.

- ID: `ssl_verify`
- Datatype: `boolean`
- Default Value: `true`
