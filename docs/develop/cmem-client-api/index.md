---
status: new
title: "cmem-client: Python API"
icon: material/language-python
tags:
    - API
    - Python
    - cmem-client
hide:
    - toc
---

# cmem-client: Python API

## Introduction

`cmem-client` is the official Python client for eccenca Corporate Memory. It gives
Python developers a typed, object-oriented API for accessing and manipulating a
Corporate Memory deployment - projects, graphs, datasets, workflows, queries, and more -
without having to talk to the REST API directly.

Corporate Memory provides its functionality through several services: Build
(DataIntegration), the Explore backend (DataPlatform), Keycloak and the Marketplace.
`cmem-client` hides that split behind a single object. You create one client, configure it
once - from environment variables, from settings you hold yourself, from a Python plugin
context or from an existing cmempy setup - and reach every part of the deployment through
its properties.

On top of plain HTTP calls, the library validates every response into a Pydantic model, so
an unexpected server field surfaces as an error instead of a missing dictionary key three
frames later. The whole package is type annotated and checked with mypy, so your editor can
complete and check your code. Collections such as the graphs, projects or workflows of a
deployment behave like read-only dictionaries: they support `len()`, membership tests, item
access and iteration, and fetch their data lazily on first use. Logging goes through the
Python standard library and is configured with a single call on the client, including a
`TRACE` level below `DEBUG` which records the arguments and the results of the methods that
carry it.

The package is published under the Apache 2 license at
[pypi.org](https://pypi.org/project/cmem-client), so a plain `pip install cmem-client`
installs it. It requires Python 3.13 or newer. It is also the foundation of
[cmemc](../../automate/cmemc-command-line-interface/index.md), the Corporate Memory command
line interface, which is based solely on `cmem-client` since v26.2.

`cmem-client` succeeds the deprecated [cmempy Python API](../cmempy-python-api/index.md),
but it is not a drop-in replacement. Where cmempy offers module level functions returning
parsed JSON, `cmem-client` gives you a client object whose responses are validated models.
An already configured cmempy environment can be reused directly, which makes a gradual
migration possible.

Browse the full [API Reference](api-reference/index.md) for every module, class and
function the package provides.
