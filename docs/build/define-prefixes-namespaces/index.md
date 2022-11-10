---
tags:
    - KnowledgeGraph
    - BestPractice
---
# Define Prefixes / Namespaces

## Introduction

A namespace declaration consists of a **prefix name** and a **namespace IRI**.
Namespace declarations allow for abbreviation of IRIs by using a prefixed resource name instead of a full IRI. 
my chage -- Phani

For example, after defining a namespace with the values

- **prefix name** = `cohw`, and the
- **namespace IRI** = `https://data.company.org/hardware/`

you can use the term `cohw:test` as an abbreviation for the full IRI `https://data.company.org/hardware/test`.

This is in particular useful when you have to write source code in Turtle and SPARQL.

## Managing Namespace Declarations


### Using the Vocabulary Catalog

After installing a vocabulary from the [Vocabulary Catalog](/explore-and-author/vocabulary-catalog), the vocabulary namespace declaration is automatically added to all integration projects.

In order to get the **prefix name** and the **namespace IRI** from the vocabulary graph, the following terms from the [VANN vocabulary](https://vocab.org/vann/) need to be used on the Ontology resource.

- [vann:preferredNamespacePrefix](https://vocab.org/vann/#preferredNamespacePrefix) - to specify the **prefix name**
- [vann:preferredNamespaceUri](https://vocab.org/vann/#preferredNamespaceUri) - to specify the **namespace IRI**

In the Explore area, an Ontology with a correct namespace declaration looks like this.

![An ontology (graph) resource in the EXPLORE > Knowledge Graphs view](ontology-graph-resource.png)

### Using cmemc

The `vocabulary` command group of [cmemc](../../automate/cmemc-command-line-interface/index.md) has an `import` command, which you can use to install arbitrary vocabulary documents and register them as a vocabulary in Corporate Memory.

Beginning with v22.2, this command has an additional option `--namespace` which you can use to set a vocabulary namespace even if the vocabulary does not include the needed data for autodiscovery:

```shell-session
$ cmemc vocabulary import my-ont.ttl --namespace myo https//example.org/my/`
```

### Using the Project Configuration

In addition to the used vocabulary namespace declarations, you may want to add well-known namespaces for organizing to Knowledge Graphs.

Such organization use cases include:

- Namespaces per class / resource type:
    - **prefix name** = `persons`, **namespace IRI** = `https://example.org/data/persons/`
- Namespaces per data owner or origin:
    - **prefix name** = `sales`, **namespace IRI** = `https://example.org/data/sales/`

Prefixes in Data Integration are defined on a project base. When creating a new project, a list of well-know prefixes is already declared.

After selecting a project from the search results the prefix management is available in the project configuration in the lower right area:

![DataIntegration workspace](DI-workspace.png)

By using the **Edit Prefix Settings** button in this Configuration are, you will see the **Manage Prefixes** dialog:

![DataIntegration workspace prefix setup dialog](DI-workspace-prefix-dialog.png)

In this dialog, you are able to

- Delete a namespace declaration → **Delete Prefix**
- Add a new namespace declaration → **Add**

## Validating Namespace Declarations

After adding namespace declarations to a project, you are able to the abbreviated IRIs in user interface, such as the mapping editor, the Turtle editor or the Query editor:

![Prefixes displayed in the mapping dialogs, e.g. property selection.](prefix-displayed-in-mapping.png)

![Query Editor](DM-query-editor.png)

![Turtle Editor](DM-turtle-editor.png)
