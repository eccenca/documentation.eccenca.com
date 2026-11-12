---
title: "Generate SHACL shapes from data"
description: "Generate SHACL node and property shapes from a data graph"
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Generate SHACL shapes from data

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task generates SHACL (Shapes Constraint Language) node
and property shapes by analyzing the instance data of a knowledge graph. The generated
shapes describe the classes the data uses and the properties each class is used with.

The data graph and the shape catalog are both chosen by IRI parameter rather than by
workflow connection, so the task has neither an input nor an output port. It is a
terminal step: it reads and writes graphs directly and hands nothing on to a following
task.

## What is generated

- A **node shape** for every class that instances are typed with.
- A **property shape** for every property those instances use: object properties in the
  subject → object direction, object properties in the object ← subject direction, whose
  names carry a `←` prefix, and datatype properties, whose values are literals.

Every shape gets an IRI derived from a UUID5 of the class or property it describes, so
within one catalog the same class or property always maps to the same shape. Names and
labels come from the title eccenca Corporate Memory resolves for that class or property.
A description follows wherever one can be resolved - the `rdfs:comment`,
`dcterms:description` or `skos:definition` of the class or property, looked up wherever
it is defined, so a vocabulary graph counts as well as the data graph. A class or
property that nothing describes gets no `sh:description`, and neither does a shape for
the object ← subject direction: the description is written about the property, so on the
inverse path it would say the opposite of what the shape holds.

Every property shape carries `shui:showAlways`, and a shape for the object ← subject
direction carries `shui:inversePath` as well. A node shape carries the `foaf:depiction` of
its target class wherever the data graph or the class's own vocabulary offers one. The
catalog itself records the data graph it was generated from, when it was written, and the
classes it manages.

## Caveats

Names, labels and descriptions are requested in English. Where a vocabulary offers no
English text, Corporate Memory answers in whatever language it does have, and the
literal carries that language rather than claiming to be English. A class or property
the deployment knows nothing about falls back to a name built from its IRI, which has
no language at all and is written without a tag.

A property used by several classes gets one property shape, shared by every node shape
that uses it. Its `sh:nodeKind` is decided by whichever of those classes sorts first, so a
property carrying IRI values under one class and literal values under another is described
as only one of the two - the same one on every run over the same data.

A class or property that is a blank node is skipped. Instance data sharing a graph with an
ontology types things with anonymous class expressions, and a shape has nothing to target
in one.

`sh:datatype rdf:langString` is added as soon as any value of a property carries a
language tag, however few of them do. A property whose values mix tagged and untagged
literals therefore gets a shape that its own source data does not satisfy.

Adding to an existing catalog replaces the name, label and description of every shape the
run writes, and the classes the catalog declares, rather than leaving an earlier run's
beside them. Everything else in the catalog is left alone, including shapes this run did
not produce - that is what adding is for.

## Example

Given a data graph typing instances with a vocabulary the deployment knows:

``` turtle
ex:Person123 a ex:Person ;
    ex:name "John" ;
    ex:knows ex:Person456 .
```

the task generates a node shape for `ex:Person`

``` turtle
graph:90ee6e27-59b1-5ac8-9d7a-116c60c6791a a sh:NodeShape ;
  rdfs:label "Person (ex:)"@en ;
  sh:name "Person (ex:)"@en ;
  sh:description "A person."@en ;
  sh:property
    graph:0fcf371d-f99a-5eeb-ab50-6e6b5fbb0e06 ,
    graph:dd5c6728-75a2-5215-8a5d-f9cd4077aaea ;
  sh:targetClass ex:Person .
```

together with a property shape for each of `ex:knows` and `ex:name`, of which the first
reads

``` turtle
graph:0fcf371d-f99a-5eeb-ab50-6e6b5fbb0e06 a sh:PropertyShape ;
  rdfs:label "knows (ex:)"@en ;
  sh:name "knows (ex:)"@en ;
  sh:nodeKind sh:IRI ;
  sh:path ex:knows ;
  shui:showAlways true .
```



## Parameter

### Input data graph

The knowledge graph holding the instance data to analyze.

- ID: `data_graph_iri`
- Datatype: `scheme:string`
- Default Value: `None`



### Output shape catalog

The graph the generated shapes are written to.

- ID: `shapes_graph_iri`
- Datatype: `scheme:string`
- Default Value: `None`



### Handle an existing shape catalog

What to do when the output shape catalog already exists.

- ID: `existing_graph`
- Datatype: `string`
- Default Value: `stop`



### Import into the central shape catalog

If enabled, the generated catalog is imported into the central shape catalog by adding an `owl:imports` statement to it. Shapes in a catalog the central one does not import are not picked up.

- ID: `import_shapes`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### Output shape catalog label

The label of the shape catalog. Left empty, a new catalog gets a generated label, and a catalog being added to keeps the label it has - but a catalog being replaced is rewritten whole, generated label included. Only a label tagged "en" or carrying no language tag counts as an existing label, and only such a label is replaced.

- ID: `label`
- Datatype: `string`
- Default Value: `None`



### Fetch namespace prefixes from prefix.cc

If enabled, the namespace prefix list is fetched from <https://prefix.cc> instead of the local prefix database, falling back to the local database when the service cannot be reached. Prefixes defined in the project win over both. Enabling this exposes your IP address to prefix.cc; no other data is shared. If unsure, leave it disabled. See <https://prefix.cc/about>.

- ID: `prefix_cc`
- Datatype: `boolean`
- Default Value: `false`



### Properties to ignore

The properties to leave out of the generated shapes, as IRIs, one per line.

- ID: `ignore_properties`
- Datatype: `multiline string`
- Default Value: `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`



### Classes to ignore

The classes to leave out of the generated shapes, as IRIs, one per line.

- ID: `ignore_types`
- Datatype: `multiline string`
- Default Value: `None`



### Include task provenance

If enabled, the shape catalog also records the task that generated it and the parameter values it ran with. Where the type of the task cannot be determined, nothing is recorded and the run continues with a warning in the log.

- ID: `plugin_provenance`
- Datatype: `boolean`
- Default Value: `false`



### Omit the namespace prefix from property names

If enabled, property shape names and labels leave off the trailing namespace prefix, reading "label" rather than "label (rdfs:)". Node shape names always keep it.

- ID: `omit_namespace_addon`
- Datatype: `boolean`
- Default Value: `false`



### Declare the classes the catalog manages

If enabled, the shape catalog states with `shui:managedClasses` which classes it manages: node shapes, property shapes, property groups, SPARQL constraints, prefix declarations, chart visualizations, table reports, widget integrations and workflow triggers.

- ID: `managed_classes`
- Datatype: `boolean`
- Default Value: `true`



### Add depictions to node shapes

If enabled, a node shape is given the `foaf:depiction` of its target class, where one can be found. The class is looked up in the data graph and in the graph named by its own namespace, tried both with and without the trailing separator, because the graph a vocabulary was loaded into is not recorded anywhere. A class depicted more than once contributes one of its depictions, the same one on every run.

- ID: `depictions`
- Datatype: `boolean`
- Default Value: `true`
