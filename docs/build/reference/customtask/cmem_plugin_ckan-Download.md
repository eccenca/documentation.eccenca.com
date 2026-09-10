---
title: "Download CKAN files"
description: "Download the files of a dataset from a CKAN service."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Download CKAN files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow task downloads the files of a dataset from a
[CKAN](https://ckan.org) service, such as the
[PMD Dataportal](https://dataportal.material-digital.de). What CKAN calls the
resources of a package are files attached to a dataset, and this task fetches
their content.

Files leave the task as file entities, written into a temporary directory of
the DataIntegration node. They exist for the length of the workflow run and are
not added to the project, so anything that is meant to survive the run has to be
written somewhere by a following task - **Extract from PDF files** of
`cmem-plugin-pdf-extract`, **Upload files to Nextcloud** of
`cmem-plugin-nextcloud` and the **Upload files to CKAN** task of this package
all take file entities.

Datasets and files arrive on the input port, which is what a task in front of
this one is for: it can walk a list of datasets that a SPARQL query or another
task produced. Without such an input, the task fetches the dataset configured
on it.

Each file is fetched from the address CKAN records for it, which is not
necessarily on the same service: a harvested dataset points at the service it
was harvested from, and a file behind a login there fails even though the
dataset itself was readable.


## Parameter

### CKAN URL

The base URL of the CKAN service, e.g. `https://dataportal.material-digital.de`.

- ID: `url`
- Datatype: `string`
- Default Value: `None`



### API token

An API token of the CKAN service. Can stay empty for a service that publishes its datasets without a login.

- ID: `token`
- Datatype: `password`
- Default Value: `None`



### Dataset

The dataset whose files are downloaded. Ignored for the datasets that arrive on the input port.

- ID: `dataset`
- Datatype: `string`
- Default Value: `None`



### File matching regex

Downloads only the files whose name matches this regular expression, e.g. `\.csv$`. Empty means every file of the dataset.

- ID: `name_regex`
- Datatype: `string`
- Default Value: `None`



### File format

Downloads only the files CKAN records under this format, e.g. `CSV`. Empty means every format. CKAN takes the format as free text, so it is often missing or spelled differently than expected.

- ID: `file_format`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### On error

What happens when a single file cannot be transferred. Either way the workflow ends in an error.

- ID: `on_error`
- Datatype: `string`
- Default Value: `stop`
