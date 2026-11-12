---
title: "Parse YAML"
description: "Parses YAML documents from a code field, entities or files and converts them to JSON."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Parse YAML

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This task reads YAML documents, converts each of them to JSON, and hands the result on
either as entities or as files.

The YAML comes from one of three places: the code field of this task, entities carrying it
as text, or files arriving on an input port. Both port modes read every entity of every
port the task declares, so a batch of files becomes a batch of results, and the number of
those ports is configurable, for documents which come from several tasks at once.
Configured to read from its code field, it declares no input port and starts the workflow.
On the output side the task either hands on the structure of the documents as entities, or
one JSON file per document.

It usually sits between a task that produces files and one that consumes them: read a
directory of YAML, parse it here, and let a task that stores project resources keep the
JSON. Feeding the entities output into a transformation is the other common chain.

Worth knowing before configuring it:

- A document has to describe a mapping or a sequence. A file holding nothing but a string
  or a number is rejected, since neither becomes a JSON object.
- Exactly one document is read per file. A stream of several documents separated by `---`
  fails.
- Parsing is safe, so YAML tags that construct arbitrary Python objects are refused.
- Documents leaving as entities are combined into one stream whose paths are the union of
  all of them, and a value a document does not carry becomes empty. Where two documents
  disagree about a key - a string in one, a list in the next - the key is carried as text
  in both, since one schema cannot hold it both ways.
- A key which is not a string becomes one. Mind that `on`, `yes` and `no` are booleans in
  YAML, so `on:` reads back as `True` unless it is quoted in the source document.
- A returned file is named after the file it came from - after the entry, when that file
  is an entry in an archive - with a `.json` suffix, made unique when two of them would
  otherwise share a name. A document that did not come from a file - from the code field,
  or from an entity - has no name of its own and is written as `parsed-yaml.json` instead.


## Parameter

### Source / Input Mode

Where the YAML documents come from.

- ID: `source_mode`
- Datatype: `string`
- Default Value: `code`



### Target / Output Mode

In which shape the parsed documents leave this task.

- ID: `target_mode`
- Datatype: `string`
- Default Value: `entities`



### YAML Source Code (when using the *code* input)

The YAML document itself, used in the 'code' source mode.

- ID: `source_code`
- Datatype: `code-yaml`
- Default Value: `# Add your YAML code here (and select 'code' as input mode).`

## Advanced Parameter

### Number of Input Ports

How many input ports the task declares. Raise it to read from several tasks at once, in the order the ports are shown. It has no effect in the 'code' source mode, which declares no input port at all.

- ID: `number_of_inputs`
- Datatype: `Long`
- Default Value: `1`



### Tolerate Unusable Input

If enabled, a document that cannot be parsed is reported and skipped instead of stopping the task, and an input that delivers nothing at all produces an empty result. A batch in which every document fails remains an error, since something arrived and none of it could be used.

- ID: `tolerate_unusable_input`
- Datatype: `boolean`
- Default Value: `false`



### Input Schema Type / Class

The type the input ports ask for, used in the 'entities' source mode. Change it when the preceding task delivers entities of a different type.

- ID: `input_schema_type`
- Datatype: `string`
- Default Value: `urn:x-eccenca:yaml-document`



### Input Schema Path / Property

The path the YAML document is read from, used in the 'entities' source mode. Change it when the preceding task carries the document in a differently named path.

- ID: `input_schema_path`
- Datatype: `string`
- Default Value: `text`
