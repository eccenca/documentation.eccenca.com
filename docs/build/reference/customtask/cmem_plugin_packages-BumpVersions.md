---
title: "Bump Version in Package Manifest"
description: "Raise the version of a CPA manifest, by semantic level or to the current date."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Bump Version in Package Manifest

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Raises the `package_version` of a CPA manifest without touching anything else in it.

The version is either bumped by one semantic level, or replaced by the current date, so
that 20 August 2026 becomes `2026.8.20`. The date is read as UTC from the clock of this
instance. Leading zeros are not valid in a semantic version, which is why the date is
written as `2026.8.20` and not as `2026.08.20`.

A bump never lowers a version. In the date mode the new version can fail to be higher
than the current one, when the manifest was already bumped on the same day or carries a
version ahead of today's date; the task then fails by default.

Manifests arrive on the input port, which is replaced by a parameter when the manifest
is configured on the task itself.

The bumped manifests leave on the output port. That port can feed several consumers at
once, so a release workflow typically wires it both to a file dataset, which stores the
raised manifest back into the project, and to the **Build Packages** task, which builds
the archive from it and hands that to **Publish Packages**.

The emitted manifest is a canonical serialization of the manifest model, not the
original file with a single line changed. It is reformatted, and fields left out of the
original are filled in with their defaults. Storing it back over a hand-formatted
manifest therefore produces a larger diff than the version line alone.


## Parameter

### Manifest JSON

The CPA manifest as JSON. If provided, the input port is removed and the version is raised in this manifest. If left empty, the manifests are taken from the input port.

- ID: `manifest_file`
- Datatype: `multiline string`
- Default Value: `None`



### Bump mode

How the new version is derived from the current one.

- ID: `bump_mode`
- Datatype: `string`
- Default Value: `patch`

## Advanced Parameter

### When the version would not be raised

What to do when the new version is not higher than the current one. This can only happen in the current date mode: the manifest was already bumped on the same day, or it carries a version ahead of today's date.

- ID: `on_version_not_raised`
- Datatype: `string`
- Default Value: `error`
