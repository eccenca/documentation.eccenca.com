---
title: "Create Embeddings"
description: "Turn the text of each entity into a vector embedding and add it to the entity."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Create Embeddings

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Turns the text an entity carries into a vector embedding and adds it to that entity, using an
embeddings model reached over the OpenAI embeddings protocol. Embeddings are what makes
similarity search possible: two entities whose text means roughly the same thing get vectors
that sit close to one another, which is the basis for semantic search, clustering and
retrieval-augmented generation.

## Ports

Entities arrive on one input port and leave on one output port with two paths added - the
vector, and the text the vector was computed from. Keeping the source text means a later
reader can see exactly what was embedded rather than having to reconstruct it.

Naming the paths to embed fixes the shape of both ports: the input port asks for those paths
and for any paths you forward, and the output port carries all of them plus the two new ones.
Leaving the selection empty embeds everything an entity carries, which no schema can describe
in advance, so the input port becomes flexible and the output schema is settled only at run
time.

Both added values are text. The vector is the text form of a Python list of floats, such as
`[0.021, -0.118, ...]`, not a JSON array. The source text is the value itself when the entity
holds a single value, or when a single selected path holds a single value; otherwise it is the
text form of a Python dictionary from path to values - again not JSON, so single quotes rather
than double ones.

## Where it fits

Embeddings are of no use on their own: they are written on to a store that can search them,
and the usual chain is a dataset or a knowledge graph, then this task, then that store. Its
sibling **Execute Instructions** is the generating half of the same picture, so the two often
appear in one workflow - this task finding the entities worth looking at, and that one writing
about them.

## Caveats

Entities are sent in chunks and a whole chunk is embedded in one request. Nothing catches a
failure of that request, so a rate limit, a text longer than the model's context window, or an
entity the provider rejects stops the workflow and takes the rest of the chunk with it.
Cancelling likewise takes effect between chunks.

An output path may not be a path the incoming entities already carry. This is checked when the
task is configured and again against the schema that actually arrives, and is an error either
way.

Embeddings are comparable only when they come from the same model. Changing the model means
everything already stored has to be computed again.


## Parameter

### Embeddings model

The identifier of the embeddings model to use. Some providers do not offer a model listing, in which case type the identifier in directly rather than picking it from the list. Model identifiers for some public providers: [Claude](https://docs.claude.com/en/docs/build-with-claude/embeddings#available-models), [OpenAI](https://platform.openai.com/docs/guides/embeddings#embedding-models).

- ID: `model`
- Datatype: `string`
- Default Value: `None`



### Embedding entity paths (comma-separated list)

The entity paths whose values are embedded, separated by commas. Naming paths here fixes the schema of both ports. Leaving it empty embeds every path an entity carries and leaves both ports open instead.

- ID: `embedding_paths`
- Datatype: `string`
- Default Value: `text`



### Forward entity paths (comma-separated list)

Further entity paths carried to the output unchanged, comma-separated. A path named here that an incoming entity does not have arrives empty rather than missing, so the output schema holds whatever was promised.

- ID: `forward_paths`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### Base URL

The base URL of the OpenAI compatible API, without the endpoint path. Left empty, the task uses the built-in large language model proxy of the eccenca Corporate Memory deployment it runs in. That fallback does not apply to `AZURE_OPENAI`, which always needs a URL here.

- ID: `base_url`
- Datatype: `string`
- Default Value: `None`



### API type

Which client is used to reach the API. `OPENAI` speaks the plain OpenAI protocol and covers OpenAI itself as well as every compatible service. `AZURE_OPENAI` uses Azure's authentication and URL layout, and needs both a base URL and an API version.

- ID: `api_type`
- Datatype: `enumeration`
- Default Value: `OPENAI`



### API key

The key used to authenticate against the API. It is ignored when the built-in model proxy is used, which authenticates with the `EXPLORE_AI_APIKEY` entry of `environments/config.env` instead.

- ID: `api_key`
- Datatype: `password`
- Default Value: `None`



### API version

The Azure OpenAI API version, read only when the API type is `AZURE_OPENAI`. The versions currently offered are listed in [the Azure documentation](https://learn.microsoft.com/en-gb/azure/ai-foundry/openai/api-version-lifecycle).

- ID: `api_version`
- Datatype: `string`
- Default Value: `None`



### Timeout (seconds)

How long a single API request may take, in seconds. One request covers a whole chunk of entities, so this limits embedding the chunk rather than embedding one entity.

- ID: `timout_single_request`
- Datatype: `Long`
- Default Value: `10000`



### Entries processing buffer

How many entities are embedded per API request. Larger chunks mean fewer requests, but a chunk is also the unit that is lost when a request fails, and providers cap how much text one request may carry.

- ID: `entries_processing_buffer`
- Datatype: `Long`
- Default Value: `100`



### Entity embedding text (output)

The entity path the embedded source text is written to. It may not be a path the incoming entities already carry.

- ID: `embedding_output_text`
- Datatype: `string`
- Default Value: `_embedding_source`



### Entity embedding path (output)

The entity path the vector is written to. It may not be a path the incoming entities already carry.

- ID: `embedding_output_path`
- Datatype: `string`
- Default Value: `_embedding`
