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

This workflow task generates SHACL (Shapes Constraint Language)
node and property shapes by analyzing instance data from a knowledge graph. The generated
shapes describe the structure and properties of the classes used in the data graph.

## Usage

The plugin analyzes an input data graph and creates:

- **Node shapes**: One for each class (`rdf:type`) used in the data graph
- **Property shapes**: For all properties associated with each class, including:
    - Regular object properties (subject → object relationships)
    - Inverse object properties (object ← subject relationships, marked with ← prefix)
    - Datatype properties (literal values)

## Output

The generated shapes are written to a shape catalog graph with:

- Unique URIs based on UUIDs (UUID5 derived from class/property IRIs)
- Human-readable labels and names (using namespace prefixes when available)
- Metadata including source data graph reference and timestamps
- Optional plugin provenance information (see advanced options)

## Example

Given a data graph with:

``` turtle
ex:Person123 a ex:Person ;
    ex:name "John" ;
    ex:knows ex:Person456 .
```

The plugin generates:

- A node shape for `ex:Person` with `sh:targetClass ex:Person`

``` turtle
graph:90ee6e27-59b1-5ac8-9d7a-116c60c6791a a sh:NodeShape ;
  rdfs:label "Person (ex:)"@en ;
  sh:name "Person (ex:)"@en ;
  sh:property
    graph:0fcf371d-f99a-5eeb-ab50-6e6b5fbb0e06 ,
    graph:dd5c6728-75a2-5215-8a5d-f9cd4077aaea ;
  sh:targetClass ex:Person .
```

- Property shapes for `ex:name` (datatype property) and `ex:knows` (object property)

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

The knowledge graph containing the instance data to be analyzed for the SHACL shapes generation.

- ID: `data_graph_iri`
- Datatype: `string`
- Default Value: `None`

### Output shape catalog

The knowledge graph the generated shapes will be added to.

- ID: `shapes_graph_iri`
- Datatype: `string`
- Default Value: `None`

### Output shape catalog label

The label for the shape catalog graph. If no label is specified for a new shapes graph, a label will be generated. If no label is specified when adding to a shapes graph, the original label will be kept, or, if the existing graph does not have a label, a label will be generated. Only labels with language tag "en" or without language tag are considered.

- ID: `label`
- Datatype: `string`
- Default Value: `None`

### Handle existing output graph

Add result to the existing graph (add result to graph), overwrite the existing graph with the result (replace existing graph with result), or stop the workflow if the output graph already exists (stop workflow if output graph exists).

- ID: `existing_graph`
- Datatype: `string`
- Default Value: `stop`

### Import the output graph into the central shapes catalog

Import the SHACL shapes graph in the CMEM shapes catalog by adding an `owl:imports` statement to the central CMEM shapes catalog. If the graph is not imported, the new shapes are not activated and used.

- ID: `import_shapes`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### Fetch namespace prefixes from prefix.cc

Fetch the list of namespace prefixes from <https://prefix.cc> instead of using the local prefix database. If unavailable, fall back to the local database. Prefixes defined in the Corporate Memory project override database prefixes. Enabling this option exposes your IP address to prefix.cc but no other data is shared. If unsure, keep this option disabled. See <https://prefix.cc/about>.

- ID: `prefix_cc`
- Datatype: `boolean`
- Default Value: `false`

### Properties to ignore

Provide the list of properties (as IRIs) to ignore.

- ID: `ignore_properties`
- Datatype: `multiline string`
- Default Value: `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`

### Types to ignore

Provide the list of types (as IRIs) to ignore.

- ID: `ignore_types`
- Datatype: `multiline string`
- Default Value: `None`

### Include plugin provenance

Add information about the plugin and plugin settings to the shapes graph.

- ID: `plugin_provenance`
- Datatype: `boolean`
- Default Value: `false`

