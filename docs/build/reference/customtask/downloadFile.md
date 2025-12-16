---
title: "Download file"
description: "Downloads a file from a given URL."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Download file
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Downloads a file from a given URL.

## Parameter

### URL

The URL of the file to be downloaded.

- ID: `url`
- Datatype: `string`
- Default Value: `None`

### Accept

The accept header String.

- ID: `accept`
- Datatype: `string`
- Default Value: `None`

### Request timeout

Request timeout in ms. The overall maximum time the request should take.

- ID: `requestTimeout`
- Datatype: `int`
- Default Value: `10000`

### Connection timeout

Connection timeout in ms. The time until which a connection with the remote end must be established.

- ID: `connectionTimeout`
- Datatype: `int`
- Default Value: `5000`

### Read timeout

Read timeout in ms. The max. time a request stays idle, i.e. no data is send or received.

- ID: `readTimeout`
- Datatype: `int`
- Default Value: `10000`

### HTTP headers

Configure additional HTTP headers. One header per line. Each header entry follows the curl syntax.

- ID: `httpHeaders`
- Datatype: `multiline string`
- Default Value: `None`

### Authorization header

The authorization header. This is usually either 'Authorization' or 'Proxy-Authorization'If left empty, no authorization header is sent.

- ID: `authorizationHeader`
- Datatype: `string`
- Default Value: `None`

### Authorization header value

The authorization header value. Usually this has the form 'type secret', e.g. for OAuth 'bearer <insert secret access token>.'This config parameter will be encrypted in the backend.

- ID: `authorizationHeaderValue`
- Datatype: `password`
- Default Value: `None`

## Advanced Parameter

`None`
