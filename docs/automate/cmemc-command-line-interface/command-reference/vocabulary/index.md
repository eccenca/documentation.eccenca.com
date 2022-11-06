---
title: "cmemc: Command Group - vocabulary"
description: "List, (un-)install, import or open vocabs / manage cache."
icon: material/graph-outline
tags:
  - Vocabulary
  - cmemc
---
# vocabulary Command Group

List, (un-)install, import or open vocabs / manage cache.

## vocabulary open

Open / explore a vocabulary graph in the browser.

Vocabularies are identified by their graph IRI.
Installed vocabularies can be listed with the `vocabulary list` command.

```shell-session
$ cmemc vocabulary open [OPTIONS] IRI
```

```text
Usage: cmemc vocabulary open [OPTIONS] IRI

  Open / explore a vocabulary graph in the browser.

  Vocabularies are identified by their graph IRI. Installed vocabularies can
  be listed with the `vocabulary list` command.
```
## vocabulary list

Output a list of vocabularies.

Vocabularies are graphs (see `graph` command group) which consists
of class and property descriptions.

```shell-session
$ cmemc vocabulary list [OPTIONS]
```

```text
Usage: cmemc vocabulary list [OPTIONS]

  Output a list of vocabularies.

  Vocabularies are graphs (see `graph` command group) which consists of
  class and property descriptions.

Options:
  --id-only                       Lists only vocabulary identifier (IRIs) and
                                  no labels or other meta data. This is useful
                                  for piping the ids into other cmemc
                                  commands.

  --filter [all|installed|installable]
                                  Filter list based on status.  [default:
                                  installed]

  --raw                           Outputs raw JSON.
```
## vocabulary install

Install one or more vocabularies from the catalog.

Vocabularies are identified by their graph IRI.
Installable vocabularies can be listed with the
`vocabulary list --filter installable` command.

```shell-session
$ cmemc vocabulary install [OPTIONS] [IRIS]...
```

```text
Usage: cmemc vocabulary install [OPTIONS] [IRIS]...

  Install one or more vocabularies from the catalog.

  Vocabularies are identified by their graph IRI. Installable vocabularies
  can be listed with the `vocabulary list --filter installable` command.

Options:
  -a, --all   Install all vocabularies from the catalog.
```
## vocabulary uninstall

Uninstall one or more vocabularies.

Vocabularies are identified by their graph IRI.
Already installed vocabularies can be listed with the
`vocabulary list --filter installed´ command.

```shell-session
$ cmemc vocabulary uninstall [OPTIONS] [IRIS]...
```

```text
Usage: cmemc vocabulary uninstall [OPTIONS] [IRIS]...

  Uninstall one or more vocabularies.

  Vocabularies are identified by their graph IRI. Already installed
  vocabularies can be listed with the `vocabulary list --filter installed´
  command.

Options:
  -a, --all   Uninstall all installed vocabularies.
```
## vocabulary import

Import a turtle file as a vocabulary.

With this command, you can import a local ontology file as a named graph
and create a corresponding vocabulary catalog entry.

The uploaded ontology file is analysed locally in order to discover the
named graph and the prefix declaration. This requires an OWL ontology
description which correctly uses the `vann:preferredNamespacePrefix` and
`vann:preferredNamespaceUri` properties.

```shell-session
$ cmemc vocabulary import [OPTIONS] FILE
```

```text
Usage: cmemc vocabulary import [OPTIONS] FILE

  Import a turtle file as a vocabulary.

  With this command, you can import a local ontology file as a named graph
  and create a corresponding vocabulary catalog entry.

  The uploaded ontology file is analysed locally in order to discover the
  named graph and the prefix declaration. This requires an OWL ontology
  description which correctly uses the `vann:preferredNamespacePrefix` and
  `vann:preferredNamespaceUri` properties.

Options:
  --namespace <TEXT TEXT>...  In case the imported vocabulary file does not
                              include a preferred namespace prefix, you can
                              manually add a namespace prefix with this
                              option. Example: --namespace ex
                              https://example.org/

  --replace                   Replace (overwrite) existing vocabulary, if
                              present.
```
