---
title: "Execute Instructions"
description: "Prompt a large language model once per entity and add the answer to the entity."
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


Sends a prompt to a large language model once for every entity it receives, and adds the
model's answer to that entity. The prompt is a Jinja template rendered against the entity, so
every entity gets a prompt of its own. Requests go over the OpenAI chat completions protocol,
which covers OpenAI itself, Azure OpenAI and any service speaking the same protocol -
Anthropic, OpenRouter, or a model hosted locally. With no endpoint configured, the task uses
the built-in model proxy of the eccenca Corporate Memory deployment it runs in.

## Ports

Entities arrive on one input port and leave, enriched, on one output port. The shape of both
follows from the instruction prompt alone; variables written into the developer prompt or into
the messages template are not looked at.

- **A prompt without variables** is the same for every entity, so there is nothing to read.
  The task then has no input port at all and emits a single entity.
- **`{{ entity }}`** renders the whole entity, whose paths cannot be known beforehand. Both
  ports are flexible, and everything that arrives is passed through to the output.
- **`{{ entity.title }}`** names one path. The input port then asks for exactly the paths the
  prompt names, and the output port carries them through beside the answer.

`entity` is the only variable name a prompt may introduce. Any other one is rejected while the
task is being configured rather than at run time.

The answer is added on a path of its own. Under structured output it is the fields of the
schema you supply that become paths instead, and a model nested inside that schema becomes a
sub-entity rather than a path. Switching the task to file input replaces the input side
entirely: the port then takes file entities, one file is sent per request, and there are no
entity paths left for a prompt to read.

## Where it fits

The task sits between whatever produces entities - a dataset, a knowledge graph, an earlier
transformation - and whatever consumes them, and leaves what it passes through untouched.
**Create Embeddings** is its counterpart: that task turns text into vectors for retrieval
rather than generating new text, and the two often appear in one workflow, one finding the
entities worth looking at and the other writing about them.

## Caveats

The model is asked once per entity, so a run costs one request per entity, and how long it
takes is governed by how many of those may be in flight at a time.

Cancelling a workflow takes effect between batches. Requests already sent are finished first.

Only failures reported by the API count as API errors. A prompt that cannot be rendered, a
messages template that is not valid JSON and a file that cannot be read stop the workflow
whatever the error setting says.

Where API errors are not raised, the error text is written to the answer path and the workflow
carries on, so a later task can consume a failure message as though it were an answer. Under
structured output that is worse than it sounds: the declared output schema has no answer path,
the error text is written to one regardless, and the values then no longer line up with the
fields the schema promises.

JSON mode guarantees only that the answer parses as JSON, never that it has the structure you
had in mind - that still has to be described in the prompt. Structured output does constrain
the shape, but only against providers and models that implement it.


## Parameter

### Instruct model

The identifier of the chat model to ask. Some providers do not offer a model listing, in which case type the identifier in directly rather than picking it from the list. Structured output additionally requires a model that implements it; the provider's own model overview says which ones do. Model identifiers for some public providers: [OpenAI](https://platform.openai.com/docs/models), [Claude](https://docs.claude.com/en/docs/about-claude/models/overview), [OpenRouter](https://openrouter.ai/models), [Azure](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure).

- ID: `model`
- Datatype: `string`
- Default Value: `None`



### Developer prompt template

The developer (system) prompt, which sets the model's role and behaviour. It is substituted into the messages template wherever `{{ developer_prompt }}` appears, but it is not itself rendered against the entity: Jinja variables written here stay in the prompt as literal text.

- ID: `developer_prompt_template`
- Datatype: `code-jinja2`
- Default Value: `You are a helpful assistant.`



### Instruction prompt template

The instruction (user) prompt, the actual request made of the model. It is rendered against each entity and the result is substituted into the messages template wherever `{{ instruction_prompt }}` appears. The variables it uses decide whether the task has an input port and what that port asks for, which the task documentation describes in full.

- ID: `instruct_prompt_template`
- Datatype: `code-jinja2`
- Default Value: `Write a paragraph about this entity: {{ entity }}`



### Enable file inputs

If enabled, the task sends files instead of entity data. The input port then accepts file entities, and each file is base64 encoded into its own request: images go as image content parts and everything else - PDFs, spreadsheets, presentations, text and code - as file content parts, with the filename preserved. A file carrying no MIME type is classified by its extension. The model has to be able to read the type you send it, and which types a provider accepts varies widely. Both prompts are sent alongside the file, but there is no entity left for them to read, so entity variables in the instruction prompt have nothing to render. The messages template is replaced by a built-in one. For text and JSON mode the output additionally carries `_filename` and `_mimetype`, so a later task can see what the model saw; structured output keeps its schema to the declared fields and adds neither.

- ID: `enable_file_inputs`
- Datatype: `boolean`
- Default Value: `false`

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



### Temperature

How random the model is allowed to be, between `0` and `2`. A high value (`0.8` - `1.0`) makes the output more varied and more creative, which suits open-ended writing. A low value (`0.0` - `0.4`) makes it more repeatable and more focused, which suits factual and technical work.

- ID: `temperature`
- Datatype: `double`
- Default Value: `1.0`



### Timeout (seconds)

How long a single API request may take before it is abandoned, in seconds.

- ID: `timeout`
- Datatype: `double`
- Default Value: `300`



### Instruction output path

The entity path the model's answer is written to. It may not be a path the prompt reads. Structured output does not use it, because the fields of the schema become the output paths instead.

- ID: `instruction_output_path`
- Datatype: `string`
- Default Value: `_instruction_output`



### Messages template

The list of messages sent to the chat completions API, as JSON. `{{ developer_prompt }}` and `{{ instruction_prompt }}` are replaced by the two prompts, and the template has to mention `instruction_prompt` somewhere. Use it to add further messages, to give an example exchange, or to assign the prompts to roles other than the default ones - [message roles and instruction following](https://platform.openai.com/docs/guides/text#message-roles-and-instruction-following) explains what the roles weigh. It is replaced by a built-in template when file inputs are enabled.

- ID: `messages_template`
- Datatype: `code-json`
- Default Value:

``` json
[
    {
        "role": "developer",
        "content": "{{ developer_prompt }}"
    },
    {
        "role": "user",
        "content": "{{ instruction_prompt }}"
    }
]
```



### Output format

What the model is asked to return. `TEXT` takes the answer as it comes. `JSON_MODE` makes the provider guarantee that the answer parses as JSON, while the structure it should have remains something to describe in the prompt. `STRUCTURED_OUTPUT` hands the provider a schema instead, so the answer comes back in the shape the Pydantic schema gives.

- ID: `output_format`
- Datatype: `enumeration`
- Default Value: `TEXT`



### Pydantic schema

The schema the answer has to follow, used by the structured output format. It is a Pydantic model, and the root class has to be named `StructuredOutput`. Only class definitions with typed fields are accepted here, next to imports from `pydantic`, `typing`, `typing_extensions`, `datetime` and `enum`. Methods, plain assignments and anything else executable are rejected. Nested models are allowed and become sub-entities on the output. Providers place their own limits on the schema, commonly at 100 properties, five levels of nesting, and 15,000 characters across all property, definition, enum and constant names.

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

If enabled, an error reported by the API stops the workflow. If disabled, the error is logged, its text is written to the output in place of an answer, and the remaining entities are still processed. Errors that are not the API's - an unrenderable prompt, an unreadable file - stop the workflow either way.

- ID: `raise_on_error`
- Datatype: `boolean`
- Default Value: `true`



### Maximum concurrent requests

How many API requests may be in flight at once. This is what governs how fast a run gets through its entities, and lowering it is the first answer to a provider that rate-limits.

- ID: `max_concurrent_requests`
- Datatype: `Long`
- Default Value: `10`



### Batch size

How many entities are prepared and processed together. Entities are read and handed on one batch at a time rather than all at once, so a smaller batch keeps less in memory and lets results reach the next task sooner.

- ID: `batch_size`
- Datatype: `Long`
- Default Value: `100`



### Request delay (seconds)

How long to wait before each API request, in seconds. Left at zero, requests are sent as fast as the concurrency limit allows. Raise it for a provider that rejects bursts even within its request limit.

- ID: `request_delay`
- Datatype: `double`
- Default Value: `0.0`
