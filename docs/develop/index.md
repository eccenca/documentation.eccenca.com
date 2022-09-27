# ★ Develop

API documentation and programming recipes.

## Base URL

All relative API URLs are prefixed by a base URL of the form `https://{domain}:{port}/{context}` with the following parameters:

- `domain`: The hostname or domain, where DataPlatform is installed. (required: true, type: string)
- `port`: The port on which the application server is available. (required: false, type: integer)
- `context`: The application context where DataPlatform is available (can be empty). (required: false, type: string)
  
## HTTP error responses

The default format for HTTP error responses is compliant with [RFC 7807 Problem Details for HTTP APIs](https://tools.ietf.org/html/rfc7807).
An HTTP error response contains a JSON object that provides at least two fields:

- `title`: A short, human-readable summary of the problem type.
- `detail`: A human-readable explanation specific to this occurrence of the problem.

The following optional non-standard fields may also be set:

- `status`: The HTTP status code for this occurrence of the problem.
- `cause`: The cause for this occurrence of the problem. It contains at least the same elements as specified previously, such as `title` and `detail`.
  
The following example shows an HTTP response containing JSON problem details using the `application/problem+json` media type:

```json
HTTP/1.1 500
Content-Type: application/problem+json

{
"title": "Internal Server Error",
"status": 500,
"detail": "Database server 'Stardog' unavailable",
"cause": {
"title": "Internal Server Error",
"status": 500,
"detail": "Connection refused (Connection refused)"
}
}
```

## Available APIs and Recipes

- :material-file-document: [cmempy - Python API](./cmempy-python-api/index.md) — cmempy is a Python API wrapper around the eccenca Corporate Memory HTTP APIs which can be used to rapidly script processes which interact with Corporate Memory.
- :material-file-document: [DataIntegration APIs](./dataintegration-apis/index.md) — eccenca DataIntegration APIs can be used to control, initiate and setup all task and activities related to the [★ Build](../build/index.md) step (such as datasets, transformations, linking tasks etc.). ([DataIntegration OpenAPI Reference](https://markdown-sandbox.eccenca.com/develop/dataintegration-apis/#open-api-reference))
- :material-file-document: [DataPlatform APIs](../develop/dataintegration-apis/index.md) — eccenca DataPlatform APIs can be used to import, export, query and extract information from graphs as well as to check access conditions. [DataPlatform OpenAPI Reference](https://markdown-sandbox.eccenca.com/develop/dataplatform-apis/#open-api-reference))
