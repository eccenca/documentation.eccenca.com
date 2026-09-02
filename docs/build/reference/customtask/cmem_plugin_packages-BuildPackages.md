---
title: "Build Packages"
description: "Build package archives from a CPA manifest, using graphs, projects and files from this instance."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Build Packages

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Builds package archives from a CPA manifest.

The manifest lists what belongs in the package. Graphs are exported from the store,
projects from the workspace, and text and image files from the file resources of the
project this task runs in. All of it is collected into a single archive, named after
the package ID and version taken from the manifest.

Manifests arrive on the input port, which is replaced by a parameter when the manifest
is configured on the task itself. Each manifest produces one archive.

The archives leave on the output port as `*.cpa` files, ready for the **Publish
Packages** task to upload them to a marketplace service, or for the **Install
Packages** task to install them on this instance. A release workflow typically chains
**Bump Version in Package Manifest**, this task, and then **Publish Packages**.

The manifest is trusted to describe content which is really there. A graph, project or
file it lists but which is missing from this instance makes the task fail while that
content is being exported. Text and image files are read from the project the task
runs in, so a manifest cannot pull auxiliary files out of a different project.


## Parameter

### Manifest JSON

The CPA manifest as JSON. If provided, the input port is removed and the package is built from this manifest. If left empty, the manifests are taken from the input port.

- ID: `manifest_file`
- Datatype: `multiline string`
- Default Value: `None`

## Advanced Parameter

`None`
