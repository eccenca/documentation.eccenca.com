---
title: "Install Packages"
description: "Install packages and their dependencies from a marketplace service or from package archives."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Install Packages

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Installs packages and their dependencies into Corporate Memory.

The task installs a single package chosen on the task, package archives which arrive on
the input port, or a list of package IDs which arrives on the input port. The three
modes exclude each other, and the input port exists only for the two which need it.
Configuring two of them at once makes the task fail before it runs.

There is no output port. Installing is a terminal step: the packages land on this
instance and nothing is handed on.

Package archives can come from the **Build Packages** task, or from any other task which
provides files. Dependencies are always fetched from a marketplace service, so even a
package installed from an archive needs one to be reachable.

The **Preview dependencies** action lists what an installation would pull in. It applies
to a package chosen on the task, not to the two input port modes.


## Parameter

### Package ID

The identifier of a package on the marketplace service.

- ID: `package_id`
- Datatype: `string`
- Default Value: `None`



### Import conflict policy

How to proceed when a package is already installed.

- ID: `import_conflict_policy`
- Datatype: `string`
- Default Value: `fail`



### Install package archives (*.cpa) from input port

If enabled, the task provides an input port for package archives delivered by a previous task, and the package ID has to be left empty. The sending task needs to deliver the archive with the FileEntitySchema, e.g. [Get project files](https://documentation.eccenca.com/latest/build/reference/customtask/getProjectFiles/) or [Download Nextcloud files](https://documentation.eccenca.com/latest/build/reference/customtask/cmem_plugin_nextcloud-Download/).

- ID: `install_from_input_files`
- Datatype: `boolean`
- Default Value: `false`



### Install listed packages from input port

If enabled, the task provides an input port for a package list delivered by a previous task, and the package ID has to be left empty. The requested input schema paths are `package_id` (mandatory) and `marketplace_url` (optional, defaults to `https://eccenca.market`).

- ID: `install_from_list`
- Datatype: `boolean`
- Default Value: `false`



### Marketplace URL

The URL of the marketplace service from which packages are installed.

- ID: `marketplace_url`
- Datatype: `string`
- Default Value: `https://eccenca.market`

## Advanced Parameter

### Ignore dependencies

If enabled, package dependencies are not installed.

- ID: `ignore_dependencies`
- Datatype: `boolean`
- Default Value: `false`



### Use cache

If enabled, uses the local marketplace package cache. Disabled by default, as write access to the file system may not be available.

- ID: `use_cache`
- Datatype: `boolean`
- Default Value: `false`
