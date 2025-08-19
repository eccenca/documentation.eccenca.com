---
title: "Evaluate template"
description: "Evaluates a template on a sequence of entities. Can be used after a transformation or directly after datasets that output a single table, such as CSV or Excel."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Evaluate template
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->




The template operator supports the Jinja templating language. Documentation about Jinja can be found in the official [Template Designer Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/).

Note that support for RDF properties is limited, because Jinja does not support some special characters (in particula colons) in variable names. This makes it impractical to access RDF properties. For this reason, the transformation that precedes the template operator needs to make sure that it generates attributes that are valid Jinja variable names.

## Default evaluation

By default, the template is evaluated separately for each entity.
For each input entity, a output entity is generated that provides a single output attribute, which contains the evaluated template.

*Limitation*: For the default evaluation, accessing nested paths is not supported. If the preceding transformation contains hierarchical mappings, only the attributes from the root mapping can be accessed.

## Full evaluation

If 'full evaluation' is enabled, the entire input set will be evaluated at once.

The entities variable will contain all input entities and can be iterated over: 

    {% for entity in entities %}
    {{entity.property}}
    {% endfor %}

A single output entity will be generated that contains the evaluated template.

If the input entities are hierarchical (typically the case if the input transformation is hierarchical), each entity will be hierarchical as well.

Example iterating over an sequence of books that each contains a list of chapters:

    {% for book in entities %}
    Book {{book.title}}
    {% for chapter in book.chapter %}
    Chapter {{chapter.chapterNumber}}
    {% endfor %}
    {% endfor %}

In this example, the child mapping defines a `chapter` target property from which it is accessible from the root entities. If the child mapping allows multiple entities, the value of the property will be a list of entities.


## Parameter

### Template

The template

- ID: `template`
- Datatype: `template`
- Default Value: `None`



### Language

The template language. Currently, Jinja is supported.

- ID: `language`
- Datatype: `string`
- Default Value: `jinja`



### Output attribute

The attribute in the output that will hold the evaluated template.

- ID: `outputAttribute`
- Datatype: `string`
- Default Value: `output`



### Full evaluation

If enabled, the entire input set will be evaluated at once. The template will receive a hierarchical 'entities' variable that can be iterated over. A single output entity will be generated that contains the evaluated template.

- ID: `fullEvaluation`
- Datatype: `boolean`
- Default Value: `false`



### Forward input attributes

If true, the input attributes will be forwarded to the output.

- ID: `forwardInputAttributes`
- Datatype: `boolean`
- Default Value: `false`





## Advanced Parameter

`None`