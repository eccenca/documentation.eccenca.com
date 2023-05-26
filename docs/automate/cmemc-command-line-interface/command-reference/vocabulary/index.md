---
title: "cmemc: Command Group - vocabulary"
description: "List, (un-)install, import or open vocabs / manage cache."
icon: eccenca/application-vocabularies
tags:
  - Vocabulary
  - cmemc
---
# vocabulary Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, (un-)install, import or open vocabs / manage cache.


## vocabulary open

Open / explore a vocabulary graph in the browser.

```shell-session title="Usage"
$ cmemc vocabulary open IRI
```




Vocabularies are identified by their graph IRI. Installed vocabularies can be listed with the `vocabulary list` command.



## vocabulary list

Output a list of vocabularies.

```shell-session title="Usage"
$ cmemc vocabulary list [OPTIONS]
```




Vocabularies are graphs (see `graph` command group) which consists of class and property descriptions.



??? info "Options"
    ```text

    --id-only                       Lists only vocabulary identifier (IRIs) and
                                    no labels or other metadata. This is useful
                                    for piping the ids into other cmemc
                                    commands.
  
    --filter [all|installed|installable]
                                    Filter list based on status.  [default:
                                    installed]
  
    --raw                           Outputs raw JSON.
    ```

## vocabulary install

Install one or more vocabularies from the catalog.

```shell-session title="Usage"
$ cmemc vocabulary install [OPTIONS] [IRIS]...
```




Vocabularies are identified by their graph IRI. Installable vocabularies can be listed with the vocabulary list command.



??? info "Options"
    ```text

    -a, --all   Install all vocabularies from the catalog.
    ```

## vocabulary uninstall

Uninstall one or more vocabularies.

```shell-session title="Usage"
$ cmemc vocabulary uninstall [OPTIONS] [IRIS]...
```




Vocabularies are identified by their graph IRI. Already installed vocabularies can be listed with the vocabulary list command.



??? info "Options"
    ```text

    -a, --all   Uninstall all installed vocabularies.
    ```

## vocabulary import

Import a turtle file as a vocabulary.

```shell-session title="Usage"
$ cmemc vocabulary import [OPTIONS] FILE
```




With this command, you can import a local ontology file as a named graph and create a corresponding vocabulary catalog entry.

The uploaded ontology file is analysed locally in order to discover the named graph and the prefix declaration. This requires an OWL ontology description which correctly uses the `vann:preferredNamespacePrefix` and `vann:preferredNamespaceUri` properties.



??? info "Options"
    ```text

    --namespace <TEXT TEXT>...  In case the imported vocabulary file does not
                                include a preferred namespace prefix, you can
                                manually add a namespace prefix with this
                                option. Example: --namespace ex
                                https://example.org/
  
    --replace                   Replace (overwrite) existing vocabulary, if
                                present.
    ```

