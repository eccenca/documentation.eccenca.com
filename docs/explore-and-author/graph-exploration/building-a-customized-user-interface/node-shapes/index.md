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


### Tab Name (deprecated)


Name of the tab (deprecated, only interpreted until 20.06)

Used Path: `shui:tabName`


### Navigation list query


This property links the node shape to a SPARQL 1.1 Query in order to provide a sophisticated user navigation list query e.g. to add specific additional columns. The query should use {{FROM}} as a placeholder for the FROM section. Additionally, {{GRAPH}} can be used to access the graph in the FROM section.

Used Path: `shui:navigationListQuery`


### Depiction Image


This property links a node shape to an image in order to use this image when showing resources based on this node shape somewhere.

Used Path: `http://xmlns.com/foaf/0.1/depiction`

## Vocabulary

!!! info
    In this group, the affected vocabulary classes as well as the used property shapes are managed.

### Property Shapes


The used property shapes on this node. Please note that this is NOT a link to a datatype or object property but to a SHACL property shape.

Used Path: `shacl:property`


### Target class


Class this NodeShape applies to. This is a direct link to a class resource from a vocabulary.

Used Path: `shacl:targetClass`

## Processing

!!! info
    In this group, all shape properties are managed, have an effect on how new or existing resources are processed or created.

### URI template


A compact sequence of characters for describing a range of URIs through variable expansion.

Used Path: `shui:uriTemplate`


### On update update



A query which is executed when this nodeshape is submitted.
The query should be saved in the same graph as the shape (or imported).

The query can use these placeholders:

- `{{shuiResource}}` - the resource currently shown with the node shape of this property shape,
- `{{shuiGraph}}` - the currently used graph. 


Used Path: `shui:onUpdateUpdate`


### Target Graph Template


Graph templates can be used to enforce writing statement in specific graphs rather than into the selected graph. Graph templates can be added to node and property shapes. A template on a property shape is used only for overwriting a template on a node shape (without a node shape graph template, they do not have an effect).

Used Path: `shui:targetGraphTemplate`

## Statement Annotation

!!! info
    Statement Annotations provide a way to express knowledge about statements. This group is dedicated to properties which configure the Statement Annotation feature.

### Enable


A value of true enables visualisation and management capabilities of statement annotations (reification) for all statements which are shown via this shape.

Used Path: `shui:enableStatementLevelMetadata`


### Provide as Shape


A value of true enables this node shape to be applied as statement annotation (reification).

Used Path: `shui:isApplicableAsStatementLevelMetadata`
