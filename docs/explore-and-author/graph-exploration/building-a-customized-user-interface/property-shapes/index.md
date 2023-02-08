---
icon: octicons/cross-reference-24
tags:
    - Reference
    - Vocabulary
---
# Property Shapes
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Property Shapes are resources of type `shacl:PropertyShape`.
They are used to specify constraints and UI options that need to be met in the context of a Node Shape.

The following Property Shape properties are supported:


## Naming and Presentation

!!! info

    In this group, presentation and naming properties are collected. Most of the properties are straight forward to use, other properties provide more complex features, such as table reports.

### Provide Workflow Trigger


Integrates a workflow trigger button in order to execute workflows from or with this resource.

Used Path: `shui:provideWorkflowTrigger`


### Name


This name will be shown to the user.

Used Path: `shacl:name`


### Description


This text will be shown to the user in a tooltip. You can use new and blank lines for basic text structuring.

Used Path: `shacl:description`


### Query: Table Report


Use this property to provide a tabular read-only report of a custom SPARQL query at the place where this property shape is used in the user interface.

The following placeholder can be used in the query text of the SPARQL query:

- `{{shuiMainResource}}` - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage) ;
- `{{shuiResource}}` - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape) ;
- `{{shuiGraph}}` - the currently used graph.


Used Path: `shui:valueQuery`


### Query: Table Report (hide header)


If set to true, the report table will be rendered without header (in case you expect only a single value).

Used Path: `shui:valueQueryHideHeader`


### Query: Table Report (hide footer)


If set to true, the report table will be rendered without footer (in case you expect only a single value or row).

Used Path: `shui:valueQueryHideFooter`


### Order


Specifies the order of the property in the UI. Ordering is separate for each group.

Used Path: `shacl:order`


### Group


Group to which the property belongs to.

Used Path: `shacl:group`


### Show always


Default is false. A value of true let optional properties (min count = 0) show up by default.

Used Path: `shui:showAlways`


### Read only


Default is false. A value of true means the properties are not editable by the user. Useful for displaying system properties.

Used Path: `shui:readOnly`

## Vocabulary

!!! info

    In this group, property paths as well cardinality restrictions are managed.

### Property of


The node shape this property shape belongs to.

Used Path: `shacl:property`


### Path


The datatype or object property used in this shape.

Used Path: `shacl:path`


### Node kind


Type of the node.

Used Path: `shacl:nodeKind`


### Min count


Min cardinality, 0 will show this property under optionals unless 'Show always = true'

Used Path: `shacl:minCount`


### Max count


Max cardinality

Used Path: `shacl:maxCount`

## Datatype Property Specific

!!! info

    In this group, all shape properties are managed, which only have effects on datatype properties.

### Datatype


The datatype of the property.

Used Path: `shacl:datatype`


### Use textarea


Default is false. A value of true enables multiline editing capabilities for Literals via a `textarea` widget.

Used Path: `shui:textarea`


### Regex Pattern


A XPath regular expression (Perl like) that all literal strings need to match.

Used Path: `shacl:pattern`


### Regex Flags


An optional string of flags for the regular expression pattern (e.g. 'i' for case-insensitive mode)

Used Path: `shacl:flags`


### Languages allowed


This limits the given Literals to a list of languages. This property works only in combination with the datatype `rdf:langString`. Note that the expression for this property only allows for '2 Char ISO-639-1-Codes' only (no sub-tags).

Used Path: `shui:languageIn`


### Languages Unique


Default is false. A value of true enforces that no pair of Literals may use the same language tag.

Used Path: `shacl:uniqueLang`

## Object Property Specific

!!! info

    In this group, all shape properties are managed, which only have effects on object properties.

### Class


Class of the connected IRI if nodeKind == sh:IRI.

Used Path: `shacl:class`


### Query: Selectable Resources


This query allows for listing selectable resources in the dropdown list for this property shape.

Used Path: `shui:uiQuery`


### Inverse Path


Default is false. A value of true inverts the expected / created direction of a relation.

Used Path: `shui:inversePath`


### Deny new resources


A value of true disables the option to create new resources.

Used Path: `shui:denyNewResources`


### Node shape


The shape of the linked resource.

Used Path: `shacl:node`

## Processing

!!! info

    In this group, all shape properties are managed, have an effect on how new or existing resources are processed or created.

### URI template


A compact sequence of characters for describing a range of URIs through variable expansion.

Used Path: `shui:uriTemplate`


### Ignore on copy


Disables reusing the value(s) when creating a copy of the resource.

Used Path: `shui:ignoreOnCopy`


### Query: On insert update


This query is executed when a property value is added or changed.

The following placeholder can be used in the query text of the SPARQL query:

- `{{shuiMainResource}}` - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage) ;
- `{{shuiResource}}` - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape) ;
- `{{shuiGraph}}` - the currently used graph.
    

Used Path: `shui:onInsertUpdate`


### Query: On delete update


This query is executed when a value is changed or removed.

The following placeholder can be used in the query text of the SPARQL query:

- `{{shuiMainResource}}` - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage) ;
- `{{shuiResource}}` - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape) ;
- `{{shuiGraph}}` - the currently used graph.
    

Used Path: `shui:onDeleteUpdate`


### Target Graph Template


Graph templates can be used to enforce writing statement in specific graphs rather than into the selected graph. Graph templates can be added to node and property shapes. A template on a property shape is used only for overwriting a template on a node shape (without a node shape graph template, they do not have an effect).

Used Path: `shui:targetGraphTemplate`

## Statement Annotation

!!! info

    Statement Annotations provide a way to express knowledge about statements. This group is dedicated to properties which configure the Statement Annotation feature.

### Enable


A value of true enables visualisation and management capabilities of statement annotations (reification) for all statements which are shown via this shape.

Used Path: `shui:enableStatementLevelMetadata`


### Provided Shapes


Instead of providing all possible statement annotation node shapes for the creation of new statement annotations, this property will limit the list to the selected shapes only.

Used Path: `shui:provideStatementLevelMetadataShapes`
