---
title: "JQL query"
description: "Search and retrieve JIRA issues."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# JQL query

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task sends a [JQL query](https://www.atlassian.com/software/jira/guides/jql/overview)
to the [REST API (v2)](https://developer.atlassian.com/cloud/jira/platform/rest/v2/) of a given
Jira service. It is tested both with on-premise Jira deployments as well as with instances on
`atlassian.net`.

The result of the JQL query is a list of JIRA issue descriptions (entities).
This list is forwarded as a JSON document to the output port,
where you should connect a JSON Dataset.

Note that you need to create an [API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)
for your Atlassian account, to access the API of your atlassian.net hosted Jira instance.

## Parameter

### Jira Server

Base URL of the jira service, e.g. '<https://jira.example.org>'

- ID: `base_url`
- Datatype: `string`
- Default Value: `None`

### Account

- ID: `username`
- Datatype: `string`
- Default Value: `None`

### Password or Token

- ID: `password`
- Datatype: `password`
- Default Value: `None`

### JQL Query

Warning: An empty query string retrieves all issues.

- ID: `jql_query`
- Datatype: `string`
- Default Value: `None`

### Limit

Maximum number of issues to retrieve (0 = retrieve all issues).

- ID: `limit`
- Datatype: `Long`
- Default Value: `0`

## Advanced Parameter

### Verify SSL Connection

- ID: `ssl_verify`
- Datatype: `boolean`
- Default Value: `true`

### Connection Timeout

Number of seconds, the plugin will wait to establish a connection to the Jira Service.

- ID: `timeout`
- Datatype: `Long`
- Default Value: `300`

### Results per Page

Number of items to return per request.

- ID: `results_per_page`
- Datatype: `Long`
- Default Value: `100`
