---
title: "Create/Update Salesforce Objects"
description: "Manipulate data in your organization's Salesforce account."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Create/Update Salesforce Objects
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This task retrieves data from an incoming workflow task (such as a SPARQL query),
and sends bulk API requests to the Salesforce Object API, in order to
manipulate data in your organization's Salesforce account.

The working model is:

- Each entity from the input data is interpreted as a single Salesforce object of the
configured object type.
- Each path from the input entity is interpreted as a field from the Salesforce
data model (refer to  the [Salesforce Standard Objects list](https://developer.salesforce.com/docs/atlas.en-us.238.0.object_reference.meta/object_reference/sforce_api_objects_list.htm)).
- The special path `id` is used to identify an object in Salesforce and switch
between update/creation mode, means:
    - If there is NO id path available, a new object is created.
    - If there IS an id path available, an update is done if the object exists.

Example:

- You want to create new Lead objects based on data from a Knowledge Graph.
- The [Lead Object Reference](https://developer.salesforce.com/docs/atlas.en-us.238.0.object_reference.meta/object_reference/sforce_api_objects_lead.htm) lists the supported fields, e.g. `FirstName`,
`LastName` and `Email`.
- Your input SPARQL task looks like this. Note that the variables need
to match the field strings from the Salesforce data model:

```
SELECT DISTINCT FirstName, LastName, Email ...
```

- You select `Lead` as the Object API Name of this task and you connect both task in
the workflow in order get the result of the SPARQL task as in input for this task.
- For each SPARQL result, a new Lead is created.

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

### Object API Name

Salesforce Object API Name

- ID: `salesforce_object`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
