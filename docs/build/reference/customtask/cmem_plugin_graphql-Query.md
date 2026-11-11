---
title: "GraphQL query"
description: "Sends a GraphQL query or mutation to an endpoint and returns the result as entities."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# GraphQL query

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This task sends a GraphQL query or mutation to an endpoint and
captures the response.

## How often the endpoint is called

Jinja syntax in the query or in the variables turns the task into a loop: both are
rendered once per arriving entity and the endpoint is called once per entity, with a
failing entity logged, counted in the report and skipped rather than taking the whole
task down. Text without Jinja syntax is sent exactly once, and anything connected as
input is then ignored.

## What leaves the task

The responses leave on the output port in one of two shapes:

- **entities**: one per call. Their paths are the fields the query asks for, under the
  alias where a field has one, so the next task is offered the schema while the workflow
  is drawn rather than only after a first run. A field that selects sub fields becomes a
  relation, and the entities behind it follow the shape of the response.
- **file**: all responses of the run written to a single JSON file. What leaves the port
  is that one file rather than the data in it.

How many values a field carries is not part of a query - that lives in the endpoint's own
schema - so every path is offered as possibly multi valued and the entities are built to
match. A field the endpoint answers with a single object therefore arrives as a list
holding one entity, and a JSON dataset connected to the output port holds an array in
that place.

## Where this task fits

The task usually opens a chain: a GraphQL API at one end, and at the other a transform
that maps the response into a graph, or a dataset that keeps it for later steps. The file
shape suits the second kind of chain, and a task that uploads or stores what it is handed,
since a file travels through those without being taken apart on the way.

## Caveats

- **Three kinds of query describe nothing in advance**, and the entities then leave with a
  schema that stays unknown until the task has run, which the next task has to accept as
  it comes: one that does not parse as GraphQL on its own, which is the usual case for a
  Jinja template because the placeholders sit where GraphQL expects values; one holding
  more than one operation; and one whose top level is a fragment rather than plain fields.
  A run that hands on a file is not affected, since a file is described the same way
  whatever the query asks for.
- **Jinja text is never checked for GraphQL syntax errors until it is rendered**, so a
  mistake in it surfaces while the task runs, as a failed entity, rather than as a
  configuration error while the task is set up.


## Parameter

### Endpoint

The URL the query is sent to, for example `https://fruits-api.netlify.app/graphql`. A collective list of public GraphQL APIs is available [here](https://github.com/IvanGoncharov/graphql-apis).

- ID: `graphql_url`
- Datatype: `string`
- Default Value: `None`



### Access token

The token the endpoint is authenticated with. It is sent as the `Authorization: Bearer <token>` header. Leave it empty for an endpoint that needs no authentication. For GitLab, a personal, project or group access token works, with scope `read_api` for queries or `api` for mutations.

- ID: `access_token`
- Datatype: `password`
- Default Value: `None`



### Output mode

In which shape the responses leave this task.

- ID: `output_mode`
- Datatype: `string`
- Default Value: `entities`



### Query

The query or mutation to send, written in [GraphQL](https://graphql.org/). May contain Jinja syntax, for example `{{ id }}`, which is rendered against each arriving entity before the query is sent. `query allFruits { fruits { id scientific_name fruit_name family climatic_zone } }`

- ID: `graphql_query`
- Datatype: `multiline string`
- Default Value: `None`



### Query variables

The values for the variables the query declares, as a JSON object - `{"id": 1}` for a query taking `$id`. An empty object is sent for a query that declares none. May contain Jinja syntax, for example `{"id": {{ id }}}`, which is rendered against each arriving entity before the query is sent.

- ID: `graphql_variable_values`
- Datatype: `multiline string`
- Default Value: `{}`

## Advanced Parameter

`None`
