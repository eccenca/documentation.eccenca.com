---
title: "Execute REST requests"
description: "REST operator that fetches and optionally merges data from a REST endpoint. It supports executing multiple requests either via input entities that each overwrite config parameters or via paging. If you only need to download a single file, the 'Download file' operator might be the better option. Most features are currently only supported for JSON REST APIs. By default the output of this operator is one entity per response with a single property 'result' that holds the response body. Responses of multiple requests are merged into a single JSON array if the 'Parse JSON' operator is connected or the Accept header starts with 'application/json'. Alternatively the response/s can be written to the file of a connected file-based dataset, either as a merged JSON file (JSON dataset) or, if the dataset file ends in '.zip', one file per response inside a ZIP file."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Execute REST requests

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Core parameter overview

- <a id="parameter_doc_url">`URL`</a>: The URL the request will be executed against. This value can be overwritten at execution time when the 'Read parameters from input' option
         is enabled. This value will also be adapted when a paging approach is configured, see the paging section for more details.
- `Method`: One of the following HTTP methods: GET, POST, PUT, PATCH or DELETE.
- `Accept`: The ACCEPT header value for content negotiation, e.g. 'application/json'.
- <a id="parameter_doc_contentType">`Content type`</a>: The CONTENT-TYPE header value. This is usually used for POST, PUT or PATCH requests when the API endpoint
                  supports multiple different MIME types and/or requires a content MIME type to be set. E.g. 'application/json'
- <a id="parameter_doc_content"></a>`Content`: The text content of a POST, PUT or PATCH request. This value can be overwritten at execution time when the
             'Read parameters from input' option is enabled.

## Authorization

If the request needs authorization following parameters should be set, else there is no authorization header sent.

- `Authorization header`: The header that is used for authorization, usually either 'Authorization' or 'Proxy-Authorization'.
- `Authorization header value`: The secret value for the authorization, i.e. password or token. This value will be encrypted
                                and cannot be accessed in the user interface anymore after saving it.
                                E.g. for OAuth the value would have the following form: `bearer <TOKEN_VALUE>`.

## Secrets in the request content and headers

Templates of the `Content` and `HTTP headers` parameters may reference sensitive variables, e.g. `secret={{global.apiSecret}}`
as content or `X-Api-Key: {{global.apiKey}}` as a header line. The evaluated value is sent with the request but not displayed:
the template preview, the task properties and the search show the placeholder `••••••` instead.
As with password parameters, anyone who can edit the task can send the value to any host.

## Sending multiple requests

In the default configuration a single requests is sent. If multiple requests should be sent with different URLs and/or content,
the configurations for these requests must be defined via the input port of the REST operator.

- <a id="parameter_doc_readParametersFromInput">Read parameters from input</a>:
    The 'URL' and 'Content' parameter values are read from entities that are input via the input
    port of the operator. The property names are 'url' and 'content' and only overwrite the
    original parameter value if defined.

    For each input entity a separate request will be sent.
- <a id="parameter_doc_limit">Limit</a>: If set to a positive number, then only that number of input entities will be processed as requests.
- <a id="parameter_doc_offset">Offset</a>: If set to a positive number, then that many input entities will be ignored before processing them as requests.

If the option 'Read parameters from input' is enabled or a paging method is configured, it is always assumed that multiple
requests will be sent. See section 'Output options' for how the responses of multiple requests are output.

## Paging

If the REST endpoint does not return all results in a single response, multiple requests (one per page) must usually be sent in order
to fetch all results. This is currently only supported for JSON requests.

- <a id="parameter_doc_pagingMethod">`Paging method`</a>:
   There are two paging methods currently supported:

     1. `Next page full URL`: The JSON response contains the full URL of the next page. This URL will be used for the subsequent request URL.
     2. `Next page identifier`: The JSON response contains the ID of the next page. This ID will be used as query parameter value for the subsequent request.

   In both cases the path to the next page value in the response JSON must be defined via the 'Next page JSON path' parameter.
   In case of the 'Next page identifier' paging method, also the parameter 'Next page ID query parameter' must be set.

- <a id="parameter_doc_nextPageJsonPath">`Next page JSON path`</a>: The property path in the result JSON where the 'next page' URL/value is provided.
   E.g. for following response structure, the value for this parameter would be `paging/next`:

   ```text
     {
       ...,
       "paging": {
         "next": "Next ID"
       }
     }
   ```

- <a id="parameter_doc_nextPageIdQueryParameter">`Next page ID query parameter`</a>: If the paging method is 'Next page identifier', this defines the query parameter name that should
  be attached to the original request URL in combination with the 'next page' value of the current response in order
  to request the next page.

## <a id="parameter_doc_httpHeaders">Setting HTTP headers</a>

- `HTTP headers`: This parameter allows to set HTTP headers of the request being made. Each line of the multi-line value should contain a single header, e.g.

  ```text
  Accept-Language: en-US,en;q=0.5
  Cache-Control: max-age=0
  ```

## Sending a multipart HTTP file request

If the content of a POST request should be sent as file content of a multipart HTTP request, instead of the request body,
following parameter must be configured:

- <a id="parameter_doc_multipartFileParameter">`Multi-part file parameter`</a>: If set to a non-empty value then, instead of a normal POST request, a multipart/form-data
                               file upload request will be executed.
                               The value of this parameter is used as the form parameter name.

## Output options

By default, the response body of a request is output as value of the 'result' property of an output entity.
If the response body needs to be processed this can e.g. be achieved with the 'Parse JSON' operator.
If multiple requests are sent, see sections 'Sending multiple requests' and 'Paging', one entity per response is output.
Only if the 'Parse JSON' operator is connected to the output or the 'Accept' parameter starts with 'application/json',
the responses are merged into a single JSON array that is output as a single entity. In that case each response of a
GET request must be valid JSON, otherwise the request is considered failed. Responses to other HTTP methods that are not
valid JSON are skipped.

Alternatively, the response/s can be written to the file of a file-based dataset:

- <a id="parameter_doc_outputResultAsFile">`Output result as file`</a>: If enabled, instead of outputting entities, the result/s will be written directly
                           to the file of the file-based dataset that is connected to the output of this operator.

With this option enabled, the operator outputs a file instead of entities. The task connected to the output must be a
file-based dataset, e.g. JSON, XML, CSV, Text or RDF file. The file of that dataset is replaced by the written file,
so its previous content is lost. Afterwards the responses can be processed like any other file of the dataset, e.g. by
a transformation that reads the dataset. Currently only text based responses are supported. Responses with HTTP status
204 (No Content) are not written.

### Single request

If a single request is sent, the response body is written to the dataset file as is. If the dataset file is a ZIP archive,
i.e. its name ends in '.zip', the response is written as the only entry of the archive, named as described under
'Multiple requests'. If the dataset is a JSON dataset with a file that does not end in '.zip', the response of a GET request
must be valid JSON, otherwise the request is considered failed, and the 'URL property' option, see section 'Propagating
the request URL', is applied to the valid response before it is written.

### Multiple requests

If multiple requests are sent, all responses are written to a single file in one of the following ways:

- ZIP archive: If the file of the connected dataset ends in '.zip', one entry per response is added to the archive.
  This applies to all file-based datasets, including a JSON dataset, for which no merged JSON array is written in that case.
  The entries are named 'responseBody' followed by a ten-digit counter, e.g. `responseBody0000000001.json`. The suffix
  is '.json', '.csv' or '.xml' for the JSON, CSV, Multi CSV ZIP and XML datasets and omitted for other datasets.
  The following datasets can read ZIP archives: JSON, XML, CSV, Multi CSV ZIP, Text, Binary file and RDF file. An RDF file dataset
  needs its 'format' parameter set, since the format is guessed from the dataset file name, which ends in '.zip'.
- Merged JSON file: If a JSON dataset with a file that does not end in '.zip' is connected, the responses are merged into
  a JSON array, i.e. `[<response 1>,<response 2>,...]`. Each response of a GET request must be valid JSON, otherwise the
  request is considered failed. For other HTTP methods, responses that are not valid JSON are skipped. The 'URL property'
  option is applied to each response before it is written.

Writing multiple responses to a dataset that is neither a JSON dataset nor based on a ZIP file fails with a validation error.

## Fine-tuning timeouts

If requests can take a much longer time than what can usually be expected, it is possible to increase the timeouts to
control when a request should eventually fail.

- `Request timeout`: The maximum overall time in milliseconds the request is allowed to take. Default: `10000`.
- `Connection timeout`: The maximum time in milliseconds the request is allowed to establish a connection to the server. Default: `5000`.
- `Read timeout`: The maximum time a request is allowed to stay idle, i.e. the time while it receives no data. Usually this
   should be greater than the time span between the request being sent and the first data being received. Default: `10000`

## Throttling requests

If a lot of requests are sent via the 'Read parameters from input' option, it can make sense to throttle the number
of requests sent in a specific time span.

- `Delay between requests`: The delay between subsequent requests in milliseconds. Default: `0`.

## Error handling

Following parameters can be tuned in order to decide when an execution should be considered as failed.

- `Retries per request`: How often a single request configuration (URL, content) should be retried before considering this
                         request configuration as failed. Default: `3`
- `Abort when request fails`: When enabled, if a single request configuration eventually fails, i.e. it reaches its max. retry count,
                              the overall execution of the REST operator will fail.
- `Max failed requests`: If set to a value greater 0, the execution will abort if more than the given number of request configurations
                         have failed (reached max. retries). This can be used if a number of failed requests can be tolerated.
                         When 'Abort when request fails' is enabled, this option is ignored.

## Propagating the request URL

If having the request URL in the response data is needed, following parameter needs to be configured:

- <a id="parameter_doc_urlProperty">`URL property`</a>: If this parameter is non-empty the request URL will be added to the response JSON object. It will be added as value to
                  a property with the specified name in the root level of the response JSON object.
                  This is mostly relevant if the request URL cannot be re-constructed from the response data. Only supported for JSON responses.


## Parameter

### URL

The URL to execute this request against. This can be overwritten at execution time via input.

- ID: `url`
- Datatype: `string`
- Default Value: `None`



### Method

One of the following HTTP methods: GET, POST, PUT, PATCH or DELETE.

- ID: `method`
- Datatype: `enumeration`
- Default Value: `GET`



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



### Content type

The content-type header String. This can be set in case of PUT or POST. If another content type comes back, the task will fail.

- ID: `contentType`
- Datatype: `string`
- Default Value: `None`



### Content

The content that is send with a POST, PUT or PATCH request. For handling this payload dynamically this parameter must be overwritten via the task input. A template of this parameter may use sensitive variables; their values are sent with the request but not displayed.

- ID: `content`
- Datatype: `string`
- Default Value: `None`



### HTTP headers

Configure additional HTTP headers. One header per line. Each header entry follows the curl syntax. A template of this parameter may use sensitive variables; their values are sent with the request but not displayed.

- ID: `httpHeaders`
- Datatype: `multiline string`
- Default Value: `None`



### Read parameters from input

If this is set to true, specific parameters can be overwritten at execution time and one request per overwrite config will be executed. Else inputs are ignored and exactly one request will be executed. Parameters that can currently be overwritten: url, content

- ID: `readParametersFromInput`
- Datatype: `boolean`
- Default Value: `false`



### Multi-part file parameter

If set to a non-empty String then instead of a normal POST a multipart/form-data file upload request is executed. This value is used as the form parameter name.

- ID: `multipartFileParameter`
- Datatype: `string`
- Default Value: `None`



### Authorization header

The authorization header. This is usually either 'Authorization' or 'Proxy-Authorization'. If left empty, no authorization header is sent.

- ID: `authorizationHeader`
- Datatype: `string`
- Default Value: `None`



### Authorization header value

The authorization header value. Usually this has the form 'type secret', e.g. for OAuth `bearer <insert secret access token>`. This config parameter will be encrypted in the backend.

- ID: `authorizationHeaderValue`
- Datatype: `password`
- Default Value: `None`



### Delay between requests

The delay between requests in milliseconds.

- ID: `delayBetweenRequests`
- Datatype: `int`
- Default Value: `0`



### Retries per request

How often should a single request be retried if it fails.

- ID: `retriesPerRequest`
- Datatype: `int`
- Default Value: `3`



### Abort when request fails

If a single request fails, i.e. it reaches its max. retry count, should the execution then be aborted or the next requests be executed.

- ID: `abortOnRequestFail`
- Datatype: `boolean`
- Default Value: `true`



### Limit

If this is set to a number greater 0, then only this number of input REST configurations will be executed. Mainly used for debugging and executing a subset.

- ID: `limit`
- Datatype: `int`
- Default Value: `0`



### Offset

How many input entries to skip.

- ID: `offset`
- Datatype: `int`
- Default Value: `0`



### Max failed requests

If set to greater 0, then the execution will abort if more than the given number of requests have failed. This should be used to fail early. If 'abort on request fail' is set to true, then this option has no effect.

- ID: `maxFailedRequests`
- Datatype: `int`
- Default Value: `0`



### Paging method

There are two paging methods currently supported: 1. Next page full URL: The JSON response contains the full URL of the next page. This URL will be used for the subsequent request. 2. Next page identifier: The JSON response contains the ID of the next page. This ID will be used as query parameter for the subsequent request. In both cases the path to the next page value in the response JSON must be defined via the 'Next page JSON path' parameter. In case of the 'Identifier next page parameter' paging method, also the parameter 'Next page ID query parameter' must be set.

- ID: `pagingMethod`
- Datatype: `enumeration`
- Default Value: `none`



### Next page JSON path

The path to the JSON value containing the next page value of the JSON response, e.g. paging/next. The path syntax follows the Silk path syntax, but only allows forward paths.

- ID: `nextPageJsonPath`
- Datatype: `string`
- Default Value: `None`



### Next page ID query parameter

The query parameter name for the next page ID that should be attached to the next page URI request. This is necessary for the 'Next page identifier' paging method.

- ID: `nextPageIdQueryParameter`
- Datatype: `string`
- Default Value: `None`



### Output result as file

If enabled, the response/s are written to the file of the file-based dataset connected to the output, replacing its previous content. A single response is written as is, or as the only entry of a ZIP file. Multiple responses are written as one entry per response into a ZIP file if the dataset file ends in '.zip', or merged into a JSON array if a JSON dataset is connected. The task connected to the output must be a file-based dataset. If disabled, the response/s are output as entities with a single property 'result'.

- ID: `outputResultAsFile`
- Datatype: `boolean`
- Default Value: `false`



### URL property

If this is non-empty, a property is created in the root JSON object (if it exists) with the same name that has the request URL as value. This is mostly relevant if the request URL cannot be re-constructed from the response data. Only supported for JSON response data.

- ID: `urlProperty`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
