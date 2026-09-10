---
title: "Uninstall Packages"
description: "Uninstall packages and their unused dependencies from this instance."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Uninstall Packages

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Uninstalls packages and their dependencies from Corporate Memory.

The task uninstalls a single package chosen on the task, a list of package IDs which
arrives on the input port, or every package installed on this instance. The three modes
exclude each other, and the input port exists only for the list mode. Configuring two of
them at once makes the task fail before it runs.

There is no output port. Uninstalling is a terminal step, and it is not reversible: a
package can only be brought back with the **Install Packages** task.

Dependencies of a package are removed with it, but only when nothing else needs them. A
dependency which another installed package also uses stays, and so does one which was
already installed before the package pulled it in.

The **Preview dependencies** action lists what would be removed alongside the package.
It applies to a package chosen on the task, not to the other two modes.


## Parameter

### Package ID

The identifier of a package installed on this instance.

- ID: `package_id`
- Datatype: `string`
- Default Value: `None`



### Ignore not installed packages

If enabled, the task reports a warning instead of raising an error for packages which are not installed.

- ID: `ignore_not_installed_packages`
- Datatype: `boolean`
- Default Value: `false`



### Uninstall listed packages from input port

If enabled, the task provides an input port for a package list delivered by a previous task, and the package ID has to be left empty. The requested input schema path is `package_id` (mandatory).

- ID: `uninstall_list_of_packages`
- Datatype: `boolean`
- Default Value: `false`



### Uninstall all packages

If enabled, every package installed on this instance is uninstalled, and the package ID has to be left empty. With nothing installed the task fails, unless not installed packages are ignored.

- ID: `uninstall_all_packages`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

`None`
