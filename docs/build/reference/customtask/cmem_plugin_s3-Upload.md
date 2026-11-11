---
title: "Upload files to S3"
description: "Upload files to a bucket in S3 or S3-compatible object storage."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Upload files to S3

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Writes the files that arrive on its input port into a bucket.

## Ports

Files arrive on the input port, which is what a task in front of this one is
for - a download task, a task that produced a file, or anything else emitting
file entities. The task emits one entity per file it dealt with, carrying the
`bucket` and the `key` it wrote, the `name` the key ends in, the `size`, the
`etag` the service assigned and whether the file was `uploaded` or `skipped`.

That entity tag is a checksum of what now sits in the bucket, so a workflow can
write it into a Knowledge Graph next to whatever else it records about the file.

## Where the task sits

**Download S3 objects** and every other download task in the fleet produce the
file entities this task accepts, which is how a workflow copies from one system
into object storage. **List S3 objects** reads a bucket back afterwards.

## Caveats

- **The key is the prefix plus the file's name**, and the name is all that a
  file entity carries - the key an object came from is not part of it. Two files
  with the same name therefore resolve to the same key. The second one is
  reported as a failure rather than written over the first.
- **A large file is written in parts** and never held in memory as a whole. A
  file the project holds is first fetched to a temporary directory of the
  DataIntegration node, so the node needs room for it.
- **Skip and Fail ask the service whether the key is taken** before writing, one
  request per file, and something writing that key in between is not noticed.
  Replace asks nothing and simply writes.
- **The error handling decides whether one failure ends the run**, but the run
  ends in an error either way. Continuing only means the remaining files are
  written first.


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

The bucket the files are written to. It has to exist already.

- ID: `bucket`
- Datatype: `string`
- Default Value: `None`



### Key prefix

Written in front of each file's name to make the key, e.g. `incoming/`. Empty writes the names to the top of the bucket.

- ID: `prefix`
- Datatype: `string`
- Default Value: `None`



### When the key is already taken

What happens to an object the bucket already holds under the key this task would write. Replacing is what makes a repeated run leave the bucket as it was after the first one.

- ID: `on_existing`
- Datatype: `string`
- Default Value: `replace`

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
