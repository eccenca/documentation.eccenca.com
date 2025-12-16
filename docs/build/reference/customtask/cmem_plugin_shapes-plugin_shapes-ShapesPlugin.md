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

A task to generate SHACL node and property shapes from an instance data knowledge graph.

## Parameters

**<a id="parameter_doc_data_graph_iri">Input data graph</a>**

The knowledge graph containing the instance data to be analyzed for the SHACL shapes generation.

**<a id="parameter_doc_shapes_graph_iri">Output Shape Catalog</a>**

The knowledge graph, the generated shapes will be added to.

**<a id="parameter_doc_label">Output shape catalog label</a>**

The label for the shape catalog graph. If no label is specified for a new shapes graph, a label will be generated. If
no label is specified when adding to a shapes graph, the original label will be kept, or, if the existing graph does not have
a label, a label will be generated. Only labels with language tag "en" or without language tag are considered.

**<a id="parameter_doc_existing_graph">Handle existing output graph</a>**

Add result to the existing graph (add result to graph), overwrite the existing graph with the result (replace existing
graph with result), or stop the workflow if the output graph already exists (stop workflow if output graph exists).

**<a id="parameter_doc_import_shapes">Import the output graph into the central shapes catalog</a>**

Import the SHACL shapes graph in the CMEM shapes catalog by adding an `owl:imports` statement to the central CMEM shapes catalog.
If the graph is not imported, the new shapes are not activated and used.

**<a id="parameter_doc_prefix_cc">Fetch namespace prefixes from prefix.cc</a>**

Fetch the list of namespace prefixes from <https://prefix.cc> instead of using the local prefix database. If unavailable,
fall back to the local database. Prefixes defined in the Corporate Memory project override database prefixes. Enabling this
option exposes your IP address to prefix.cc but no other data is shared. If unsure, keep this option disabled. See
<https://prefix.cc/about>.

**<a id="parameter_doc_ignore_properties">Properties to ignore</a>**

Provide the list of properties (as IRIs) for which you do not want to create property shapes.
Example:

```
http://www.w3.org/1999/02/22-rdf-syntax-ns#type
http://xmlns.com/foaf/0.1/familyName
```

**<a id="parameter_doc_plugin_provenance">Include plugin provenance</a>**

Add information about the plugin and plugin settings to the shapes graph.

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

### Include plugin provenance

Add information about the plugin and plugin settings to the shapes graph.

- ID: `plugin_provenance`
- Datatype: `boolean`
- Default Value: `false`
