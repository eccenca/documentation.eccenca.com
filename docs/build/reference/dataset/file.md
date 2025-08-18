---
title: "RDF file"
description: "Dataset which retrieves and writes all entities from/to an RDF file. For reading, the dataset is loaded in-memory and thus the size is restricted by the available memory. Large datasets should be loaded into an external RDF store and retrieved using the SPARQL dataset instead."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# RDF file
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Dataset which retrieves and writes all entities from/to an RDF file. For reading, the dataset is loaded in-memory and thus the size is restricted by the available memory. Large datasets should be loaded into an external RDF store and retrieved using the SPARQL dataset instead.


## Parameter

### File

The RDF file. This may also be a zip archive of multiple RDF files.

- Datatype: `resource`
- Default Value: `None`



### Format

Optional RDF format. If left empty, it will be auto-detected based on the file extension. N-Triples is the only format that can be written, while other formats can only be read.

- Datatype: `string`
- Default Value: `None`



### Graph

The graph name to be read. If not provided, the default graph will be used. Must be provided if the format is N-Quads.

- Datatype: `string`
- Default Value: `None`



### Entity list

A list of entities to be retrieved. If not given, all entities will be retrieved. Multiple entities are separated by whitespace.

- Datatype: `multiline string`
- Default Value: `None`



### ZIP file regex

If the input resource is a ZIP file, files inside the file are filtered via this regex.

- Datatype: `string`
- Default Value: `.*`



