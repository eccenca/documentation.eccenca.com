---
title: "Create Embeddings"
description: "Fetch and output LLM created embeddings from input entities."
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


This plugin creates vector embeddings from text data using an OpenAI compatible embeddings API.
It processes input entities containing text data and generates high-dimensional vector
representations that capture semantic meaning.

## Features

- Supports OpenAI embeddings models (e.g., `text-embedding-3-small`)
- Batch processing for efficient API usage
- Configurable input/output paths
- Built-in error handling and workflow cancellation support

## Input/Output

- **Input**: Entities with text data in specified paths
- **Output**: Original entities enhanced with embedding vectors and source text
- Embedding vectors are stored as string representations of float arrays
- Source text used for embedding is preserved for reference

## Use Cases

- Semantic search and similarity matching
- Text clustering and classification
- Recommendation systems
- Natural language processing pipelines

## Parameter

### Base URL

The base URL of the OpenAI compatible API (without endpoint path).

- ID: `base_url`
- Datatype: `string`
- Default Value: `https://api.openai.com/v1/`



### API Type

Select the API client type. This determines the authentication method and endpoint configuration used for API requests. Choose `OPENAI` for direct OpenAI API access or `AZURE_OPENAI` for Azure-hosted OpenAI services. Consider using the API version advanced parameter in case you access Azure-hosted OpenAI services.

- ID: `api_type`
- Datatype: `enumeration`
- Default Value: `OPENAI`



### API key

An optional API key for authentication.

- ID: `api_key`
- Datatype: `password`
- Default Value: `None`



### Embeddings model

The identifier of the embeddings model to use. Available model IDs for some public providers can be found here: [Claude](https://docs.claude.com/en/docs/build-with-claude/embeddings#available-models), [OpenAI](https://platform.openai.com/docs/guides/embeddings#embedding-models).

- ID: `model`
- Datatype: `string`
- Default Value: `text-embedding-3-small`



### Embedding entity paths (comma-separated list)

Changing this value will change, which input paths are used by the workflow task to calculate embeddings. A blank value means, all paths are used.

- ID: `embedding_paths`
- Datatype: `string`
- Default Value: `text`



### Forward entity paths (comma-separated list)

Paths from input entities to forward to output without modification. These paths will be passed through unchanged alongside embeddings.

- ID: `forward_paths`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

### API Version

Azure OpenAI API version (only used when API Type is `AZURE_OPENAI`). For more information about OpenAI API version at Azure, please see [the documentation](https://learn.microsoft.com/en-gb/azure/ai-foundry/openai/api-version-lifecycle).

- ID: `api_version`
- Datatype: `string`
- Default Value: `None`



### Timeout (milliseconds)

The timeout for a single API request in milliseconds.

- ID: `timout_single_request`
- Datatype: `Long`
- Default Value: `10000`



### Entries Processing Buffer

How many input values do you want to send per request?

- ID: `entries_processing_buffer`
- Datatype: `Long`
- Default Value: `100`



### Entity Embedding text (output)

Changing this value will change the output schema accordingly. Default: _embedding_source

- ID: `embedding_output_text`
- Datatype: `string`
- Default Value: `_embedding_source`



### Entity Embedding path (output)

Changing this value will change the output schema accordingly. Default: _embedding

- ID: `embedding_output_path`
- Datatype: `string`
- Default Value: `_embedding`



