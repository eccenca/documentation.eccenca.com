---
title: "Download file"
description: "Downloads a file from a given URL."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Download file
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## 1. Purpose
The **Download File** operator downloads a single file from a remote URL and exposes it as a file output that can be consumed by downstream operators.

Typical use cases:
- Importing external datasets into a workflow.
- Downloading configuration files or archives.
- Fetching files from internal HTTP endpoints.

## 2. Input and output

### Input
- **Inputs:** none  
  The operator does not consume any upstream entities.

### Output
- **Output:** one file
    - A single file is created from the HTTP response body.
    - The file is exposed as a file output that downstream operators can read.
    - The MIME type is taken from the HTTP response `Content-Type` if available.

## 3. Configuration notes
The detailed list of parameters is shown in the UI (auto-generated). This section explains how to think about the most important ones.

- **URL**
    - Remote endpoint from which the file is downloaded.
    - The operator is intended for `http://` and `https://` URLs.

- **Timeouts**
    - *Request timeout* (in milliseconds): upper bound for the whole request, including streaming the response.
    - *Connection timeout*: how long to wait for the TCP connection to be established.
    - *Read timeout*: maximum idle time during data transfer (no bytes sent or received).
    - For large files or slow servers, increase the request/read timeouts as needed.

- **HTTP headers**
    - One header per line, curl-style syntax: `Header-Name: Header-Value`.
    - Headers are sent as-is with the request.

- **Authorization header / value**
    - *Authorization header*: name of the header (e.g. `Authorization`, `Proxy-Authorization`).
    - *Authorization value*: header value (e.g. `Bearer <access-token>`).
    - The value is stored encrypted in the backend.

## 4. Behaviour
When executed, the operator:
1. Builds an HTTP request from the configured parameters.
2. Sends an HTTP **GET** request to the configured URL.
3. Streams the response body into a temporary file on disk.
4. Emits that file as the operator’s output.
5. Reports the execution via the standard task/execution reporting mechanisms.

File handling:
- The file is created with a temporary name.
- The file extension is determined as follows:
    - For ZIP-like content types (e.g. `application/zip`), the extension `.zip` is used.
    - Otherwise, the extension is derived from the URL path if possible.
    - If no extension can be determined, a generic fallback (for example `.tmp`) is used.

Only a single file is produced per execution. If the request fails, no file is emitted.

## 5. Supported URLs and protocols
The operator sends an HTTP request to the configured URL.

- **Intended behaviour**
    - Use `http://` and `https://` URLs.
    - These are the supported schemes for downloading files.

- **Other schemes (e.g. `ftp://`)**
    - Not supported.
    - Using non-HTTP(S) URLs may result in an error and should not be relied on.

If reliable FTP or other protocols are needed, they should be handled by a dedicated operator or external tooling.

## 6. Error handling and failure modes
Typical failure scenarios:
- **Invalid URL / DNS / connection issues**
    - The operator fails the execution; no file is produced.
- **Non-2xx HTTP status codes (e.g. 404, 500)**
    - The request fails and the file is not created.
- **Timeouts**
    - If connection or read timeouts are exceeded, the request is aborted.
- **Streaming / I/O errors**
    - If writing to the temporary file fails, the execution fails and the partially written file is not exposed.

Errors are reported via the standard task and execution reporting mechanisms.

## 7. Examples

### 7.1 Simple HTTP download
- **URL:** `https://example.com/data.csv`
- **Parameters:**
    - Accept header: `text/csv` (optional)
    - Timeouts: defaults or slightly increased for large files.

Result:
- One file containing the downloaded CSV data, which can be passed to downstream file-processing operators.

### 7.2 Authenticated download
- **URL:** `https://internal.example.com/report.json`
- **Parameters:**
    - Authorization header: `Authorization`
    - Authorization value: `Bearer <access-token>`

Result:
- One JSON file containing the report, assuming the token is valid and the server returns a successful response.


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

The authorization header value. Usually this has the form 'type secret', e.g. for OAuth `bearer <insert secret access token>`.This config parameter will be encrypted in the backend.

- ID: `authorizationHeaderValue`
- Datatype: `password`
- Default Value: `None`





## Advanced Parameter

`None`