---
title: "Node Shape Reference"
description: "This page lists all supported properties to describe node shapes."
icon: octicons/cross-reference-24
tags:
    - Reference
    - Vocabulary
---

# Node Shapes

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Node Shapes are resources of type `shacl:NodeShape`.
They can be used to validate resources as well as to define custom forms for presenting and editing resources of a specific type.

This page lists all supported properties to describe node shapes.

## Naming and Presentation

!!! info
    In this group, presentation and naming properties are collected. Most of the properties are straight forward to use.

### Name

The name of the node is presented to the user only when he needs to distinguish between different shapes for the same resource.

Used Path: `shacl:name`

### Description

The node description should provide context information for the user when creating a new resource based on this node.

Used Path: `rdfs:comment`

### Navigation list query

This property links the node shape to a SPARQL 1.1 Query in order to provide a sophisticated user navigation list query e.g. to add specific additional columns. The query should use {{FROM}} as a placeholder for the FROM section.

Used Path: `shui:navigationListQuery`

### Depiction Image

This property links a node shape to an image in order to use this image when showing resources based on this node shape somewhere.

Used Path: `http://xmlns.com/foaf/0.1/depiction`

### Order

Specifies the order of this node shape.

This property is used for the drop-down list in the shaped resource view as well as for priorising depictions and update queries.
It is only relevant in case multiple node shapes are on the same level in the shape hierarchy (which is based on the rdfs:subClassOf relationship).

Used Path: `shacl:order`

### Widgets

Integrate non-validating visualization widget in the node shape area.

Used Path: `shui:WidgetIntegration_integrate`

### Chart Visualization

Integrates a chart visualization in the node shape area. This Property is deprecated - charts on node shape level are not supported anymore.

Used Path: `shui:provideChartVisualization`

## Vocabulary

!!! info
    In this group, the affected vocabulary classes as well as the used property shapes are managed.

### Property Shapes

The used property shapes on this node. Please note that this is NOT a link to a datatype or object property but to a SHACL property shape.

Used Path: `shacl:property`

### Target class

Class this NodeShape applies to. This is a direct link to a class resource from a vocabulary.

Used Path: `shacl:targetClass`

## Processing / User Interaction

!!! info
    In this group all shape properties are managed, which have an effect on how new or existing resources are processed or created.

### SPARQL Constraints

Add additional SPARQL based validation to your Node Shape.

Used Path: `shacl:sparql`

### URI template

The URI template which is used, when a user manually creates new resources with this Node Shape.

Used Path: `shui:uriTemplate`

### Severity

Categorize validation results (:Info, :Warning, :Violation). Defaults to :Violation.

Used Path: `shacl:severity`

### Closed Node

Enabling this will result in failing validation if the resource / node has properties which are NOT described with attached property shapes.

Used Path: `shacl:closed`

### Query: On delete update

A query which is executed when the resource the node shape applies to gets deleted.

The following placeholder can be used in the query text of the SPARQL query:

- `{{shuiGraph}}` - the currently used graph
- `{{shuiAccount}}` - the account IRI of the active user, this includes the username (use a SUBSTR() function if you need the name only)
- `{{shuiAccountName}}` - the user name/ID of the active user account
- `{{shuiMainResource}}` - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage)

Used Path: `shui:onDeleteUpdate`

### Query: On update update

A query which is executed when this node shape is submitted.
The query should be saved in the same graph as the shape (or imported).

The query can use these placeholders:

- `{{shuiGraph}}` - the currently used graph
- `{{shuiResource}}` - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape)
- `{{shuiAccount}}` - the account IRI of the active user, this includes the username (use a SUBSTR() function if you need the name only)
- `{{shuiAccountName}}` - the user name/ID of the active user account
- `{{shuiMainResource}}` - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage)

Used Path: `shui:onUpdateUpdate`

### Target Graph Template

Graph templates can be used to enforce writing statement in specific graphs rather than into the selected graph. Graph templates can be added to node and property shapes. A template on a property shape is used only for overwriting a template on a node shape (without a node shape graph template, they do not have an effect).

Used Path: `shui:targetGraphTemplate`

### Query: Is Creatable Resource

This query is executed to check if users get the controls to create resources (described with the node shape).

The query needs to be an ASK query and can include the following placeholders, which will be substituted before execution:

- `{{shuiGraph}}` - the IRI of the current working graph
- `{{shuiAccount}}` - the IRI of the active user account
- `{{shuiAccountName}}` - the user name/ID of the active user account

Used Path: `shui:askIfCreatableQuery`

### Query: Is Removable Resource

This query is executed to check if users get the controls to remove resources (described with the node shape).

The query needs to be an ASK query and can include the following placeholders, which will be substituted before execution:

- `{{shuiResource}}` - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape)
- `{{shuiGraph}}` - the IRI of the current working graph
- `{{shuiAccount}}` - the IRI of the active user account
- `{{shuiAccountName}}` - the user name/ID of the active user account
- `{{shuiMainResource}}` - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage)

Used Path: `shui:askIfRemovableQuery`

### Query: Is Editable Resource

This query is executed to check if users get the controls to edit resources (described with the node shape).

The query needs to be an ASK query and can include the following placeholders, which will be substituted before execution:

- `{{shuiResource}}` - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape)
- `{{shuiGraph}}` - the IRI of the current working graph
- `{{shuiAccount}}` - the IRI of the active user account
- `{{shuiAccountName}}` - the user name/ID of the active user account
- `{{shuiMainResource}}` - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage)

Used Path: `shui:askIfEditableQuery`

### Query: Is Cloneable Resource

This query is executed to check if users get the controls to remove resources (described with the node shape).

The query needs to be an ASK query and can include the following placeholders, which will be substituted before execution:

- `{{shuiResource}}` - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape)
- `{{shuiGraph}}` - the IRI of the current working graph
- `{{shuiAccount}}` - the IRI of the active user account
- `{{shuiAccountName}}` - the user name/ID of the active user account
- `{{shuiMainResource}}` - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage)

Used Path: `shui:askIfCloneableQuery`

### On update trigger workflow

A workflow trigger which is executed when this nodeshape is submitted. The workflow(s) run
instantaneously upon submitting the form.

Used Path: `shui:onUpdateTriggerWorkflow`

## Statement Annotation

!!! info
    Statement Annotations provide a way to express knowledge about statements. This group is dedicated to properties which configure the Statement Annotation feature.

### Enable

A value of true enables visualisation and management capabilities of statement annotations (reification) for all statements which are shown via this shape.

Used Path: `shui:enableStatementLevelMetadata`

### Provide as Shape

A value of true enables this node shape to be applied as statement annotation (reification).

Used Path: `shui:isApplicableAsStatementLevelMetadata`
