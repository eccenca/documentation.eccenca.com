---
title: "XML"
description: "Read from or write to an XML file."
icon: octicons/cross-reference-24
tags:
    - Dataset
---

# XML

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Typically, this dataset is used to transform an XML file to another format, e.g., to RDF. It can also be used to generate XML files.

## Reading

When this dataset is used as an input for another task (e.g., a transformation task), the input type of the consuming task selects the path where the entities to be read are located.

Example:

    <Persons>
      <Person>
        <Name>John Doe</Name>
        <Year>1970</Year>
      </Person>
      <Person>
        <Name>Max Power</Name>
        <Year>1980</Year>
      </Person>
    </Persons>

A transformation for reading all persons of the above XML would set the input type to `/Person`.
The transformation iterates all entities matching the given input path.
In the above example the first entity to be read is:

    <Person>
      <Name>John Doe</Name>
      <Year>1970</Year>
    </Person>

All paths used in the consuming task are relative to this, e.g., the person name can be addressed with the path `/Name`.

Path examples:

- The empty path selects the root element.
- `/Person` selects all persons.
- `/Person[Year = "1970"]` selects all persons which are born in 1970.
- `/#id` Is a special syntax for generating an id for a selected element. It can be used in URI patterns for entities which do not provide an identifier. Examples: `http://example.org/{#id}` or `http://example.org/{/pathToEntity/#id}`.
- The wildcard * enumerates all direct children, e.g., `/Persons/*/Name`.
- The wildcard ** enumerates all direct and indirect children.
- The backslash can be used to navigate to the parent XML node, e.g., `\Persons/SomeHeader`.
- `#text` retrieves the text of the selected node.

## Writing

When writing XML, all entities need to possess a unique URI. Writing multiple root entities with the same URI will result in multiple entries in the generated XML. If multiple nested entities with the same URI are written, only the last entity with a given URI will be written.

## Parameter

### File

The XML file. This may also be a zip archive of multiple XML files that share the same schema.

- ID: `file`
- Datatype: `resource`
- Default Value: `None`

## Advanced Parameter

### Base path

The base path when writing XML. For instance: /RootElement/Entity. Should no longer be used for reading XML! Instead, set the base path by specifying it as input type on the subsequent transformation or linking tasks.

- ID: `basePath`
- Datatype: `string`
- Default Value: `None`

### URI pattern

A URI pattern, e.g., <http://namespace.org/{ID}>, where {path} may contain relative paths to elements

- ID: `uriPattern`
- Datatype: `string`
- Default Value: `None`

### Output template

The output template used for writing XML. Must be valid XML. The generated entity is identified through a processing instruction of the form <?MyEntity?>.

- ID: `outputTemplate`
- Datatype: `code-xml`
- Default Value: `<Root><?Entity?></Root>`

### Streaming

Streaming allows for reading large XML files.

- ID: `streaming`
- Datatype: `boolean`
- Default Value: `true`

### Max depth

Maximum depth of written XML. This acts as a safe guard if a recursive structure is written.

- ID: `maxDepth`
- Datatype: `int`
- Default Value: `15`

### ZIP file regex

If the input resource is a ZIP file, files inside the file are filtered via this regex.

- ID: `zipFileRegex`
- Datatype: `string`
- Default Value: `^(?!.*[\/\\]\..*$|^\..*$).*\.xml$`
