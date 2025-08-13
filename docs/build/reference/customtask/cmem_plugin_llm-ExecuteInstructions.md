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


## Introduction

This plugin allows to execute an LLM instruction over a given list of entities.

After being processed, each entity receives one additional path (`_instruction_output`).
This path contains the output of the executed instruction over the entity.

## Parameters

### <a id="parameter_doc_base_url">Base URL </a>

- The base URL of the OpenAI compatible API (without endpoint path).
- Default: `https://api.openai.com/v1`

### <a id="parameter_doc_api_key">API key </a>

- An optional OpenAI API key.
- Default: blank

### <a id="parameter_doc_model">Instruct Model </a>

- The instruct model.
- Example: `gpt-4o-mini`

### <a id="parameter_doc_instruct_prompt_template">Instruction Prompt Template </a>

- The instruction prompt template. Please have look at
  [Text generation and prompting](https://platform.openai.com/docs/guides/text?api-mode=chat)
  to learn how to prompt a model to generate text.
- You can add Jinja placeholder to the template text, which will be replaced with data from
  incoming entities:
    - A placeholder such as `{{ variable }}` will be replaced with the whole incoming entity
      as a JSON string.
    - A placeholder which includes a path (`{{ variable.name }}`) will be replaced with the
      `name` property of an incoming entity.
- If you use Jinja placeholders in the template text, input and output ports of this task are
  configured as follows:
    - For each different placeholder object, an additional input port is added to the task.
    - If you do not insert any placeholders, there will be no input ports.
    - Variables are sorted alphabetically, so `{{ variable_a }}` will be replaced with entity
      data from the first input port, while `{{ variable_b }}` will be replaced with entity
      data from the second input port.
    - During execution, the task iterates over the entities from the first input port.
    - Entities from all other input ports will be consumed when the execution starts. Then, in
      each iteration, their data will inserted to the prompt `{{ variable }}` accordingly.
    - You can configure how those additional input ports will be consumed with the parameter
      <a id="parameter_doc_consume_all_entities">consume_all_entities</a>.
    - It is recommended to only use known entity paths from the connected input tasks, such as
      `{{ variable.path }}`, so the ports can be configured with a FixedSchema.
      This avoids the need for additional transformation tasks on the output port.
- Your instruct prompt template is inserted as a user message in
  the <a id="parameter_doc_messages_template">messages_template</a>.
- Default template:
``` jinja2
Write a paragraph about this entity: {{ entity }}
```

<details>
<summary>Advanced Parameter</summary>

### <a id="parameter_doc_temperature">Temperature (between 0 and 2)  - Advanced Parameter</a>

- Higher values like 0.8 will make the output more random,while lower values like 0.2 will make it more focused and deterministic.
- Default: `1.0`

### <a id="parameter_doc_timeout">Timeout for a single API call  - Advanced Parameter</a>

- The timeout of a single request in seconds.
- Default: `300`

### <a id="parameter_doc_instruction_output_path">Instruction Output Path  - Advanced Parameter</a>

- The entity path where the instruction result will be provided.
- Default: `_instruction_output`

### <a id="parameter_doc_messages_template">Messages Template  - Advanced Parameter</a>

- A list of messages comprising the conversation compatible with OpenAI
        chat completion API message object.
- Have look at [Message roles and instruction following](https://platform.openai.com/docs/guides/text#message-roles-and-instruction-following)
  to learn about different levels of priority to messages with different roles.
- Default messages template:
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

### <a id="parameter_doc_consume_all_entities">Consume all entities from additional input ports  - Advanced Parameter</a>

- If true, all entities from additional input ports will be consumed.
        Otherwise, only the first entity of the additional ports will be used.
- Be aware that all entities are loaded in memory.
- Default: `False`

### <a id="parameter_doc_output_format">Output Format  - Advanced Parameter</a>

- Specifying the format that the model must output.
- Possible values:
    - TEXT: Standard text output.
    - STRUCTURED_OUTPUT: Structured output following a given schema. Add your schema as Pydantic
      model here: <a id="parameter_doc_pydantic_schema">pydantic_schema</a>
    - JSON_MODE: JSON mode is a more basic version of the Structured Outputs feature.
      While JSON mode ensures that model output is valid JSON, Structured Outputs
      reliably matches the model's output to the schema you specify. If you want to request
      a specified structure, you can add it to
      <a id="parameter_doc_instruct_prompt_template">instruct_prompt_template</a>
- Default: `OutputFormat.TEXT`

### <a id="parameter_doc_pydantic_schema">Pydantic Schema definition the model is using in the response.  - Advanced Parameter</a>

- The Pydantic schema definition with a mandatory class named
        `StructuredOutput(BaseModel)`.
- This field is only used when <a id="parameter_doc_output_format">output_format</a>
  is set to `STRUCTURED_OUTPUT`.
- A schema may have up to 100 object properties total, with up to 5 levels of nesting.
- The total string length of all property names, definition names, enum values,
  and const values cannot exceed 15,000 characters.
- Default:
``` python
from pydantic import BaseModel

class StructuredOutput(BaseModel):
    title: str
    abstract: str
    keywords: list[str]

```
</details>


## Parameter

### Base URL

The base URL of the OpenAI compatible API (without endpoint path).

- Datatype: `string`
- Default Value: `https://api.openai.com/v1`



### API key

An optional OpenAI API key.

- Datatype: `password`
- Default Value: `None`



### Instruct Model

The instruct model.

- Datatype: `string`
- Default Value: `gpt-4o-mini`



### Temperature (between 0 and 2)

Higher values like 0.8 will make the output more random,while lower values like 0.2 will make it more focused and deterministic.

- Datatype: `double`
- Default Value: `1.0`



### Timeout for a single API call

The timeout of a single request in seconds.

- Datatype: `double`
- Default Value: `300`



### Instruction Output Path

The entity path where the instruction result will be provided.

- Datatype: `string`
- Default Value: `_instruction_output`



### Messages Template

A list of messages comprising the conversation compatible with OpenAI chat completion API message object.

- Datatype: `code-json`
- Default Value: `[
    {
        "role": "developer",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "{{ instruction_prompt }}"
    }
]`



### Instruction Prompt Template

The instruction prompt template.

- Datatype: `code-jinja2`
- Default Value: `Write a paragraph about this entity: {{ entity }}`



### Consume all entities from additional input ports

If true, all entities from additional input ports will be consumed. Otherwise, only the first entity of the additional ports will be used.

- Datatype: `boolean`
- Default Value: `false`



### Output Format

Specifying the format that the model must output.

- Datatype: `enumeration`
- Default Value: `TEXT`



### Pydantic Schema definition the model is using in the response.

The Pydantic schema definition with a mandatory class named `StructuredOutput(BaseModel)`.

- Datatype: `code-python`
- Default Value: `from pydantic import BaseModel

class StructuredOutput(BaseModel):
    title: str
    abstract: str
    keywords: list[str]
`



