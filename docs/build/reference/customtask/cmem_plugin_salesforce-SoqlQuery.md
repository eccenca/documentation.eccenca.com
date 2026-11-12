---
title: "SOQL query (Salesforce)"
description: "Executes a custom Salesforce Object Query (SOQL) to return sets of data your organization's Salesforce account."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# SOQL query (Salesforce)

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This task executes a custom Salesforce Object Query (SOQL)
and returns sets of tabular data from your organization's Salesforce account.

> Use the Salesforce Object Query Language (SOQL) to search your organization's
> Salesforce data for specific information. SOQL is similar to the SELECT statement in
> the widely used Structured Query Language (SQL) but is designed specifically for
> Salesforce data.
-- <cite>[developer.salesforce.com](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)</cite>

SOQL uses the SELECT statement combined with filtering statements to return sets of
data, which can optionally be ordered. For a complete description of the syntax, see
[Salesforce SOQL SELECT Syntax](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select.htm).

This task ignores any entities it receives; the query comes only from the SOQL Query
parameter. A query that matches no records fails with an error rather than returning
an empty result.

Examples:

Retrieve all standard fields from all Lead resources.

```text
SELECT FIELDS(STANDARD) FROM Lead
```

Retrieve first name and last name of all Contact resources.

```text
SELECT Contact.Firstname, Contact.Lastname FROM Contact
```

Please refer to the [Salesforce Standard Objects list](https://developer.salesforce.com/docs/atlas.en-us.238.0.object_reference.meta/object_reference/sforce_api_objects_list.htm) of the Salesforce Platform data
model in order to get an overview of the available objects and fields.


## Parameter

### Username

Username of the Salesforce Account. This is typically your email address.

- ID: `username`
- Datatype: `string`
- Default Value: `None`



### Password



- ID: `password`
- Datatype: `string`
- Default Value: `None`



### Security Token

In addition to your standard account credentials, you need to provide a security token to access your data. Refer to the [Salesforce Reset Token Documentation](https://help.salesforce.com/s/articleView?id=sf.user_security_token.htm&type=5) to learn how to retrieve or reset your token.

- ID: `security_token`
- Datatype: `string`
- Default Value: `None`



### SOQL Query

The query text of your SOQL query. SOQL uses the SELECT statement combined with filtering statements to return sets of data, which can optionally be ordered. For a complete description of the syntax, see [Salesforce SOQL SELECT Syntax](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select.htm).

- ID: `soql_query`
- Datatype: `multiline string`
- Default Value: `None`

## Advanced Parameter

### Dataset

Besides the direct output of the fetched entities, write the complete raw query response - including Salesforce's internal metadata for each record - to a JSON dataset (mostly for debugging purposes).

- ID: `dataset`
- Datatype: `string`
- Default Value: `None`
