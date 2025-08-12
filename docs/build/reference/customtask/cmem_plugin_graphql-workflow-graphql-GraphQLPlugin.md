---
title: "GraphQL query"
description: "Executes a custom GraphQL query to a GraphQL endpoint and saves result to a JSON dataset."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# GraphQL query
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

This workflow task performs GraphQL operations by sending
     queries, mutations, and variables over operations. Allows for customization
     in the GraphQL query using, Jinja queries and Jinja variables, which can be
     obtained from entities. The result of the query is saved as a JSON document
     in a pre-created JSON dataset.
     

## Parameter

### Endpoint

The URL of the GraphQL endpoint you want to query. A collective list of public GraphQL APIs is available [here](https://github.com/IvanGoncharov/graphql-apis). Example Endpoint: `https://fruits-api.netlify.app/graphql`

- Datatype: `string`
- Default Value: `None`



### Query

The query text of the GraphQL Query you want to execute. GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. Learn more on GraphQL [here](https://graphql.org/). Example Query: query allFruits { fruits { id scientific_name tree_name fruit_name family origin description climatic_zone } }

- Datatype: `multiline string`
- Default Value: `None`



### Query variables

Pass dynamic variables when making a query or mutation. Example Variables: {"id" : 1}

- Datatype: `multiline string`
- Default Value: `{}`



### Target JSON Dataset

The Dataset where this task will save the JSON results.

- Datatype: `string`
- Default Value: `None`



### OAuth access token

Access token that connects to a GraphQL endpoint to authorize and secure user access to resources and data.

- Datatype: `string`
- Default Value: `None`



