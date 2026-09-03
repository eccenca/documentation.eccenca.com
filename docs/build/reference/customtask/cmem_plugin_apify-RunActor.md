---
title: "Run Apify actor"
description: "Run an Apify actor and deliver its dataset as a file."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Run Apify actor

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This task drives [Apify](https://apify.com) from a workflow. It starts an actor
run, waits for it, and hands the dataset the run produced on as a file.

The actor input is a JSON document written as a Jinja template. Whatever the
template refers to becomes the input port of this task, so the values come from
the entities of the preceding operator - the knowledge graph decides what is
scraped. A template that refers to nothing has no input port and is sent as it
stands. Substituted values need the `tojson` filter, as in
`"query": {{ companyName | tojson }}`, which quotes and escapes them correctly
and renders a list where a list is supplied.

The result leaves through the file port as one file per actor run, in the chosen
format. It is deliberately not turned into entities here: a dataset can be very
large, and reading structure out of a file is what the JSON, CSV and XML
datasets of Corporate Memory already do.

The task covers three cases, which change its shape. Reading an existing Apify
dataset starts no run and needs no input. Running an actor without reading it
delivers a record of the run instead of a file. Running and reading does both in
one step.

Caveats worth knowing:

- Editing the actor input changes the input port, which can invalidate the
  mapping of a workflow that was already saved.
- Values are read from the input entities by path name, so a path has to be a
  name Jinja accepts. Rename it in a preceding operator if it is a URI.
- With one run per entity, a path holding several values contributes only its
  first; the report says how often that happened.
- A build tag such as `latest` satisfies the Build parameter but pins nothing -
  it follows whatever the actor's author publishes next. A version number pins.
- Downloaded files stay in the temporary directory of the worker.


## Parameter

### API token

The Apify API token used for every request this task makes.

- ID: `api_token`
- Datatype: `password`
- Default Value: `None`



### Mode

What this task does when it runs.

- ID: `mode`
- Datatype: `string`
- Default Value: `run_and_read`



### Actor

The Apify actor to run. Required unless the mode is Read.

- ID: `actor`
- Datatype: `string`
- Default Value: `None`



### Build

The version or build tag of the actor to run. Required unless the mode is Read.

- ID: `build`
- Datatype: `string`
- Default Value: `None`



### Actor input

The JSON document sent to the actor, as a Jinja template. The names it refers to become the input port of this task.

- ID: `actor_input`
- Datatype: `code-jinja2`
- Default Value:

``` text
{
  "startUrls": [{ "url": "https://example.org" }]
}
```



### Input strategy

How several input entities are mapped onto actor runs.

- ID: `strategy`
- Datatype: `string`
- Default Value: `collect`



### Apify dataset

The existing Apify dataset to deliver. Required when the mode is Read.

- ID: `apify_dataset`
- Datatype: `string`
- Default Value: `None`



### Output format

The format the Apify dataset is downloaded in.

- ID: `output_format`
- Datatype: `string`
- Default Value: `json`



### Error handling

What happens when an actor run does not succeed.

- ID: `run_error_handling`
- Datatype: `string`
- Default Value: `warning`

## Advanced Parameter

### Maximum number of runs

The upper bound on actor runs started with one run per entity. More input entities than this aborts the task before anything is started.

- ID: `max_runs`
- Datatype: `Long`
- Default Value: `10`



### Maximum duration (minutes)

How long the task waits for its runs before it aborts them and fails. Apify enforces the same limit, so a run stops even if this task does not.

- ID: `max_duration`
- Datatype: `Long`
- Default Value: `60`
