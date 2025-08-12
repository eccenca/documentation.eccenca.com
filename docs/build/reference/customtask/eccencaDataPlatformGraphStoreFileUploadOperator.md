---
title: "Upload File to Knowledge Graph"
description: "Uploads an N-Triples or Turtle (limited support) file from the file repository to a 'Knowledge Graph' dataset. The output of this operatorcan be the input of datasets that support graph store file upload, e.g. 'Knowledge Graph'. The file will be uploaded to the graph specified in that dataset."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Upload File to Knowledge Graph
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Uploads an N-Triples or Turtle (limited support) file from the file repository to a 'Knowledge Graph' dataset. The output of this operatorcan be the input of datasets that support graph store file upload, e.g. 'Knowledge Graph'. The file will be uploaded to the graph specified in that dataset.

## Parameter

### RDF resource

RDF file (N-Triples or Turtle) from the resource repository that should be uploaded to the Knowledge Graph.

- Datatype: `resource`
- Default Value: `None`



### Max chunk size (MB)

The N-Triples file will be split into multiple chunks if the file size exceeds the max chunk size. For Turtle files this parameter is ignored since no chunking is supported.

- Datatype: `option[int]`
- Default Value: `None`



### Content type

The MIME type of the serialization format of the RDF file.

- Datatype: `enumeration`
- Default Value: `application/n-triples`



