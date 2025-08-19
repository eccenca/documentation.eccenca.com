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


This plugin creates vector embeddings from text data using OpenAI's embeddings API.
It processes input entities containing text data and generates high-dimensional vector
representations that capture semantic meaning.

## Features

- Supports OpenAI embeddings models (e.g., text-embedding-3-small)
- Batch processing for efficient API usage
- Configurable input/output paths
- Automatic schema generation based on configuration
- Built-in error handling and workflow cancellation support

## Configuration

- **URL**: OpenAI API endpoint (default: https://api.openai.com/v1)
- **API Key**: Your OpenAI API key for authentication
- **Model**: The embedding model to use (e.g., text-embedding-3-small)
- **Timeout**: Request timeout in milliseconds (default: 10000)
- **Buffer Size**: Number of texts to process per batch (default: 100)
- **Input Paths**: Comma-separated list of entity paths to embed (default: "text")
- **Output Paths**: Configurable paths for embedding vectors and source text

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

URL of the OpenAI API (without endpoint path and without trailing slash)

- ID: `base_url`
- Datatype: `string`
- Default Value: `https://api.openai.com/v1`



### The OpenAI API key

Fill the OpenAI API key if needed (or give a dummy value in case you access an unsecured endpoint).

- ID: `api_key`
- Datatype: `password`
- Default Value: `None`



### The embeddings model, e.g. text-embedding-3-small



- ID: `model`
- Datatype: `string`
- Default Value: `text-embedding-3-small`





## Advanced Parameter

### Timeout (Single Request, in Milliseconds)



- ID: `timout_single_request`
- Datatype: `Long`
- Default Value: `10000`



### Entries Processing Buffer

How many input values do you want to send per request?

- ID: `entries_processing_buffer`
- Datatype: `Long`
- Default Value: `100`



### Used entity paths (comma-separated list)

Changing this value will change, which input paths are used by the workflow task. A blank value means, all paths are used.

- ID: `embedding_paths`
- Datatype: `string`
- Default Value: `text`



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



