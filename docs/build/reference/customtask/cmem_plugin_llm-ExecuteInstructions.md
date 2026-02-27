---
title: "Execute Instructions"
description: "Send instructions (prompt) to an LLM and process the result."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Execute Instructions

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

## Overview

This plugin executes Large Language Model (LLM) instructions over entity collections, enabling
AI-powered text generation, analysis, and transformation tasks within Corporate Memory workflows.

## Core Functionality

- **LLM Integration**: Supports OpenAI API, Azure OpenAI, and OpenAI-compatible endpoints
  (Anthropic Claude, OpenRouter, etc.)
- **Entity Processing**: Processes entities individually or in batches with configurable
  concurrency
- **Template System**: Uses Jinja2 templates for dynamic prompt generation from entity data
- **Output Formats**: Supports text, JSON mode, and structured outputs with Pydantic schemas
- **Performance Optimization**: Includes batching, rate limiting, and async processing for
  high-throughput scenarios

## Input/Output Behavior

After processing, each entity receives an additional path (default: `_instruction_output`)
containing the LLM response. For TEXT and JSON_MODE output formats, the response is stored
in this path. For STRUCTURED_OUTPUT, the Pydantic model fields are directly added to the
entity (the `_instruction_output` path is not used).

Input/output ports are automatically configured based on template variables:

- **No placeholders**: No input ports required
- **With placeholders**: Single input port created for entity data
- **Schema handling**: Fixed schemas when using specific entity paths, flexible schemas otherwise

## Template System

Uses Jinja2 templating for dynamic prompts:

```jinja2
{{ entity }}           # Entire entity as JSON
{{ entity.name }}      # Specific entity property
```

The following template processing rules are implemented:

1. **Variable Extraction**: Automatically detects template variables to configure input ports
2. **Entity Iteration**: Processes entities from the single input port individually
3. **Single Entity Context**: Each entity is processed independently with its own template context

## Output Formats

1. **Text Output (Default)** - Standard LLM text responses for general-purpose tasks.
2. **JSON Mode** - Ensures valid JSON output format. Add JSON structure requirements
   to your prompt template.
3. **Structured Output** - Uses Pydantic schemas for type-safe, validated responses:

```python
from pydantic import BaseModel

class StructuredOutput(BaseModel):
    title: str
    summary: str
    keywords: list[str]
    confidence_score: float
```

## Performance Features

Parallel Processing:

- **Concurrent Requests**: Configurable semaphore-controlled API calls
- **Batch Processing**: Entities processed in configurable batch sizes
- **Rate Limiting**: Optional delays between requests
- **Memory Optimization**: Streaming processing with generator patterns

Error Handling:

- **Graceful Degradation**: Continue processing on API errors (configurable)
- **Detailed Logging**: Comprehensive error reporting and debugging information
- **Workflow Integration**: Proper cancellation support and progress reporting

## API Compatibility

Supported Providers:

- **OpenAI**: Direct API access with full feature support
- **Azure OpenAI**: Enterprise Azure-hosted services with API versioning
- **OpenAI-Compatible**: Anthropic Claude, OpenRouter, local models, and other compatible endpoints

Authentication:

- **API Keys**: Secure password-type parameters for API authentication
- **Azure Integration**: Supports Azure OpenAI API versioning and endpoint configuration
- **Flexible Endpoints**: Custom base URLs for various providers

## Advanced Configuration

### Message Templates

Customize the conversation structure beyond simple prompts:

```json
[
    {"role": "system", "content": "You are a data analyst."},
    {"role": "user", "content": "{{ instruction_prompt }}"}
]
```

### Performance Tuning

- **Temperature Control**: Adjust creativity vs. determinism (0.0-2.0)
- **Timeout Management**: Request-level timeout configuration
- **Concurrency Limits**: Prevent rate limiting with request throttling
- **Batch Optimization**: Balance memory usage vs. throughput

## Best Practices

1. **Schema Design**: Use specific entity paths in templates for fixed schemas
2. **Error Strategy**: Enable error continuation for large datasets
3. **Performance**: Adjust concurrency and batch size based on API limits
4. **Templates**: Design prompts with clear instructions and expected outputs
5. **Testing**: Start with small entity sets to validate templates and outputs

For detailed prompting guidance, see [OpenAI's Text Generation Guide](https://platform.openai.com/docs/guides/text?api-mode=chat).

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

### Instruct Model

The identifier of the instruct model to use. Note that some provider do not support a model list endpoint. Just create a custom entry then. Available model IDs for some public providers can be found here: [OpenAI](https://platform.openai.com/docs/models), [Claude](https://docs.claude.com/en/docs/about-claude/models/overview), [OpenRouter](https://openrouter.ai/models), [Azure](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure). **Note:** For STRUCTURED_OUTPUT format, only certain models support structured outputs. See [OpenAI Structured Outputs Guide](https://platform.openai.com/docs/guides/structured-outputs) for supported models.

- ID: `model`
- Datatype: `string`
- Default Value: `gpt-4o-mini`

### Instruction Prompt Template

The instruction prompt template. Please have a look at the task documentation for detailed instructions.

- ID: `instruct_prompt_template`
- Datatype: `code-jinja2`
- Default Value: `Write a paragraph about this entity: {{ entity }}`

## Advanced Parameter

### API Version

Azure OpenAI API version (only used when API Type is `AZURE_OPENAI`). For more information about OpenAI API version at Azure, please see [the documentation](https://learn.microsoft.com/en-gb/azure/ai-foundry/openai/api-version-lifecycle).

- ID: `api_version`
- Datatype: `string`
- Default Value: `None`

### Temperature (between 0 and 2)

A parameter that controls the randomness and creativity of the model. A high temperature value (`0.8` - `1.0`) increases randomness and creativity. This is useful for open-ended tasks like storytelling or brainstorming. A low temperature value (`0.0` - `0.4`) produces more deterministic and focused outputs. This is suitable for factual or technical tasks.

- ID: `temperature`
- Datatype: `double`
- Default Value: `1.0`

### Timeout (seconds)

The timeout for a single API request in seconds.

- ID: `timeout`
- Datatype: `double`
- Default Value: `300`

### Instruction Output Path

The entity path where the instruction result will be provided. Note: This parameter is not used when Output Format is set to STRUCTURED_OUTPUT. For structured outputs, only the Pydantic model fields are included in the output schema.

- ID: `instruction_output_path`
- Datatype: `string`
- Default Value: `_instruction_output`

### Messages Template

A list of messages comprising the conversation compatible with OpenAI chat completion API message object. Have look at [Message roles and instruction following](https://platform.openai.com/docs/guides/text#message-roles-and-instruction-following) to learn about different levels of priority to messages with different roles.

- ID: `messages_template`
- Datatype: `code-json`
- Default Value:

``` json
[
    {
        "role": "developer",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "{{ instruction_prompt }}"
    }
]
```

### Output Format

Specifying the format that the model must output. Possible values are `TEXT` - Standard text output, `STRUCTURED_OUTPUT` - output follows a given schema. Add your schema as Pydantic model in the parameter below, `JSON_MODE` - a more basic version of the structured outputs feature where you have to add your structure to the prompt template.

- ID: `output_format`
- Datatype: `enumeration`
- Default Value: `TEXT`

### Pydantic Schema

The Pydantic schema definition with a mandatory class named `StructuredOutput(BaseModel)`. This is only used in combination with the Structured Output format. A schema may have up to 100 object properties total, with up to 5 levels of nesting. The total string length of all property names, definition names, enum values, and const values cannot exceed 15,000 characters.

- ID: `pydantic_schema`
- Datatype: `code-python`
- Default Value:

``` python
from pydantic import BaseModel

class StructuredOutput(BaseModel):
    title: str
    abstract: str
    keywords: list[str]

```

### Raise on API errors

How to react on API errors. When enable, any API errors will cause the workflow to stop with an exception. When disabled, API errors are logged and the error message is written to the entity output, allowing the workflow to continue processing other entities.

- ID: `raise_on_error`
- Datatype: `boolean`
- Default Value: `true`

### Maximum Concurrent Requests

Maximum number of concurrent API requests to prevent rate limiting and resource exhaustion.

- ID: `max_concurrent_requests`
- Datatype: `Long`
- Default Value: `10`

### Batch Size

Number of entities to process in each batch for memory optimization.

- ID: `batch_size`
- Datatype: `Long`
- Default Value: `100`

### Request Delay (seconds)

Delay between API requests in seconds to respect rate limits.

- ID: `request_delay`
- Datatype: `double`
- Default Value: `0.0`
