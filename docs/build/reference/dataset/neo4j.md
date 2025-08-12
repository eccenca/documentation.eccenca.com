---
title: "Neo4j"
description: "Neo4j graph"
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Neo4j
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->




Supports reading and writing Neo4j graphs. The following sections outline how graphs are generated and read back.

For more information about Neo4j, please refer to the [Neo4j documentation](https://neo4j.com/docs/).

### Nodes

For each entity that is written to a Neo4j dataset, a _node_ will be created.
A property `uri` will be added to each generated node, which holds the URI of the original entity.
In applications, the URI property should be used instead of the node identifiers, which are auto-generated in Neo4j and do not represent stable URIs.

When reading nodes, the entity URIs will be generated based on that property.
At the moment, it's not supported to read nodes that do not provide a `uri` property.

### Labels

_Labels_ in Neo4j are used to group nodes into sets where all nodes that have a certain _label_ belongs to the same set.
Neo4j _labels_ are comparable with _classes_ in RDF (not to be confused with labels in RDF).

When writing entities to the Neo4j dataset, the following _labels_ will be added to each generated node:

- For each entity _type_ (such as the _type_ set in a mapping), a _label_ will be added to the node in Neo4j.
  Since _types_ in eccenca DataIntegration are usually URIs, they will be converted according to the rules further down.
- The _label_ as configured by the _label_ parameter on the Neo4j dataset itself.
  This is typically used to identify all entities that have been written by a certain Neo4j dataset specification in the project.
  For instance, if two Neo4j dataset specifications are added to a project - both writing to the same Neo4j database - different labels can be set to distinguish both sets of entities.
  In that respect it may be used to model a similar concept as _graphs_ in RDF.

### Relationships

A relationship connects two nodes in Neo4j.
Hierarchical mappings will generate relationships for all object mappings.

Relationships can be addressed with property paths in mappings.
At the moment, only paths of length 1 are supported, i.e., it's not possible to use non-property paths.

### Handling of URIs

In eccenca DataIntegration, URIs are typically used to uniquely identify classes and properties.
While URIs are central in RDF, Neo4j does allow arbitrary names and does not have any special support for URIs.

When generating Neo4j labels, properties and relationships, URIs will be shortened according to the following rules.
- If a registered project prefix matches a URI, a name `{prefixName}_{localPart}` will be generated. For instance, `http://xmlns.com/foaf/0.1/name` will become `foaf_name`.
  Note that underscores (`_`) are used instead of colons (`:`) to separate the namespace and the local name.
  The reason is that colons are reserved in the Cypher query language and some tools don't escape properly and fail on databases that use colons in names.
- If no project prefix matches a URI, the URI will be used verbatim. This will look ugly in Neo4j tools, so generally it's recommended to define prefixes for all used namespaces.

When reading generated entities, the URIs of the classes and properties will be reconstructed based on the prefix table of the project. If the prefixes change between writing and reading, different URIs will be generated.

### RDF vs. Neo4j terminology

Neo4j uses a different terminology than RDF or description logic.
For users familiar with RDF, the following table shows the correspondent terms for some central concepts.
This is meant to help understanding and does not aim to provide a precise mapping as there are semantic differences between Neo4j and RDF.

| RDF | Neo4j |
| --- |--- |
| resource     | node |
| class      | label      |
| datatype property      | property      |
| object property      | relationship |
| graph | Do not exist in Neo4j, but labels can be used to mimic graphs.    |


## Parameter

### URI

The URL to the Neo4j instance

- Datatype: `string`
- Default Value: `bolt://localhost:7687`



### User

The Neo4j username for basic authentication.

- Datatype: `string`
- Default Value: `neo4j`



### Password

The Neo4j password for basic authentication.

- Datatype: `password`
- Default Value: `PASSWORD_PARAMETER:7vIY2uNcIiwSSo+/MNozEg==`



### Database

Database (leave empty for default)

- Datatype: `string`
- Default Value: `None`



### Node label

Neo4j label for all entities to be covered by this dataset. When reading, all nodes with this label will be read. When writing, this label will be added to all generated nodes. If the dataset is cleared, only nodes with this label will be deleted.

- Datatype: `string`
- Default Value: `Any`



### Clear before execution

If set to true, all nodes with the specified label will be removed, before executing a workflow that writes to this graph.

- Datatype: `boolean`
- Default Value: `true`



