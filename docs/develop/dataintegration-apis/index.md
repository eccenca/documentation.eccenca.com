---
icon: material/api
tags:
    - API
hide:
    - toc
---
# DataIntegration APIs

The latest OpenAPI specification is available at [https://releases.eccenca.com/OpenAPI/](https://releases.eccenca.com/OpenAPI/).

You can (re)view it with the [redoc web UI](https://redocly.github.io/redoc/?url=https://releases.eccenca.com/OpenAPI/eccenca-DataIntegration-OpenAPI-Reference-latest.json) or the [petstore web UI](https://petstore.swagger.io/?url=https://releases.eccenca.com/OpenAPI/eccenca-DataIntegration-OpenAPI-Reference-latest.json).

## Introduction

eccenca DataIntegration APIs can be used to control, initiate and setup all task and activities related to the [★ Build](../../build/index.md) step (such as datasets, transformations, linking tasks etc.).

### Media Types

The default [media type](https://en.wikipedia.org/wiki/Media_type) of most responses is application/json. Other possible response media types can be reached by changing the Accept header of the request.

Possible values of this HTTP header field are API dependent and listed as part of the specific HTTP method.

Dependent on the specific API, eccenca DataIntegration works with the following application media types which correspond to the following specification documents:

| Media Type                        | Specification Document                                                                               |
| --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| application/x-www-form-urlencoded | [HTML 4.01 Specification, Forms](https://www.w3.org/TR/html401/interact/forms.html)                  |
| application/json                  | [The JavaScript Object Notation (JSON) Data Interchange Format](https://tools.ietf.org/html/rfc8259) |
| application/xml                   | [XML Media Types](https://tools.ietf.org/html/rfc7303)                                               |
| application/n-triples             | [RDF 1.1 N-Triples - A line-based syntax for an RDF graph](https://www.w3.org/TR/n-triples/)         |
| application/problem+json          | [Problem Details for HTTP APIs](https://tools.ietf.org/html/rfc7807)                                 |

