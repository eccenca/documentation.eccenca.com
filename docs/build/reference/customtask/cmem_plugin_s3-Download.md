---
title: "Download S3 objects"
description: "Download objects from a bucket in S3 or S3-compatible object storage."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Download S3 objects

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Downloads objects from a bucket into the workflow.

## Ports

Objects leave the task as file entities, written into a temporary directory of
the DataIntegration node. They are not added to the project, so anything that is
meant to be kept has to be written somewhere by a following task.

The task has two mutually exclusive shapes. With a bucket configured on it, it
selects objects itself and takes no input. With the bucket left empty, the
objects to fetch arrive on an input port instead, in the form **List S3 objects**
emits, and the settings that would narrow a selection down have nothing left to
act on - the task in front has already decided.

## Where the task sits

**List S3 objects** produces the listing this task accepts, so a workflow can
list, narrow the result down and download only what is left. **Upload files to
S3** covers the other direction, and the file entities this task emits are what
every file consuming task in the fleet accepts.

## Caveats

- **Each object is written into a numbered directory of its own**, so two keys
  ending in the same name do not overwrite each other. Only the name is kept,
  not the key's path, and a following task therefore sees the name rather than
  the key.
- **An object replaced since it was listed is refused, not fetched.** The entity
  tag from the listing is sent with the request, so the workflow downloads the
  bytes it selected or fails - it never silently downloads newer ones. An entity
  reaching the input port without an entity tag is fetched unconditionally.
- **The error handling decides whether one failure ends the run**, but the run
  ends in an error either way. Continuing only means the remaining objects are
  fetched first.
- **The downloaded files are not cleaned up by the task.** The temporary
  directory it writes into stays on the node until whatever clears its temporary
  storage does, so a workflow fetching more than the node's disk holds will fill
  it, and fetching the same bucket repeatedly accumulates copies.
- **The preview stops after ten objects**, so it can miss an object further down
  that a real run would fail on.


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

The bucket the objects are downloaded from. Leaving it empty replaces the task's own selection with an input port.

- ID: `bucket`
- Datatype: `string`
- Default Value: `None`



### Key prefix

Downloads only the objects whose key starts with this, e.g. `raw/2026/`. The service applies it. Empty means the whole bucket.

- ID: `prefix`
- Datatype: `string`
- Default Value: `None`



### Regular expression

Downloads only the objects whose key matches this regular expression, e.g. `\.csv$`. It is matched against the whole key rather than against the name alone, and it has to match somewhere in it rather than all of it. Empty means every key.

- ID: `regex`
- Datatype: `string`
- Default Value: `None`



### Top level only

If enabled, only the keys directly below the prefix are considered and everything nested deeper is folded away. The service does the folding, on a `/` delimiter.

- ID: `top_level_only`
- Datatype: `boolean`
- Default Value: `false`



### Limit

The maximum number of objects to download, or 0 for no limit. A run that stops at the limit says so in its report.

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



### On error

What happens when a single object cannot be transferred. Either way the workflow ends in an error.

- ID: `on_error`
- Datatype: `string`
- Default Value: `stop`
