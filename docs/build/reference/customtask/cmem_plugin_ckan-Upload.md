---
title: "Upload files to CKAN"
description: "Publish files as the files of a dataset on a CKAN service."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Upload files to CKAN

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow task attaches the files that arrive on its input port to a
dataset of a [CKAN](https://ckan.org) service, such as the
[PMD Dataportal](https://dataportal.material-digital.de). What CKAN calls a
resource of a package is a file attached to a dataset, and that is what this
task writes.

Files arrive as file entities, so anything that produces them can feed this
task - the **Download CKAN files** task of this package when files are moved
between two services, or **Download Nextcloud files** of
`cmem-plugin-nextcloud`. For every file it published, the task hands on the
dataset, the file and the address the file now has, which is how a following
task can record in a graph where something was published.

A file is recognised as being already there by its name. CKAN does allow a
dataset to hold several files of one name, and replacing then updates the last
of them and leaves the others alone.

The dataset has to exist on the service already. The task never creates one, so
the title, the description and the licence stay with whoever curates the
service, and a first publication starts by creating the dataset there.

Publishing needs an API token, and it needs one whose user may write to that
dataset. What the service accepts is up to the service: an instance running the
`scheming` extension validates every file against a schema of its own, and
rejects what does not fit.


## Parameter

### CKAN URL

The base URL of the CKAN service, e.g. `https://dataportal.material-digital.de`.

- ID: `url`
- Datatype: `string`
- Default Value: `None`



### API token

An API token of the CKAN service, belonging to a user who may write to the dataset below.

- ID: `token`
- Datatype: `password`
- Default Value: `None`



### Dataset

The dataset the files are attached to. It has to exist already.

- ID: `dataset`
- Datatype: `string`
- Default Value: `None`



### When the file is already there

What happens to a file the dataset already holds under the same name. Replacing updates that file instead of adding a second one, which is what makes a repeated run leave the dataset as it was after the first one.

- ID: `on_existing`
- Datatype: `string`
- Default Value: `replace`

## Advanced Parameter

### On error

What happens when a single file cannot be transferred. Either way the workflow ends in an error.

- ID: `on_error`
- Datatype: `string`
- Default Value: `stop`
