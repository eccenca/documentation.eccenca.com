---
title: "Publish Packages"
description: "Publish package archives to a marketplace service."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Publish Packages

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Publishes package archives to a marketplace service.

The input port expects package archives (`*.cpa`), for example as produced by the
**Build Packages** task. Every archive on the port is uploaded, one after the other.

There is no output port. Publishing is the last step of a release workflow, which
typically chains **Bump Version in Package Manifest**, **Build Packages**, and then this
task. Once an archive is published, the **Install Packages** task can install it from
the same marketplace service.

Uploading needs an account on the target marketplace service, and the task authenticates
with the configured Keycloak credentials.

An upload which fails does not stop the task. The remaining archives are still uploaded,
and the failure is reported when the task finishes. When more than one upload fails,
only the last failure is reported.


## Parameter

### Marketplace URL

The URL of the marketplace service to publish packages to.

- ID: `marketplace_url`
- Datatype: `string`
- Default Value: `https://eccenca.market`



### Keycloak username

The username to authenticate with the Keycloak server of the marketplace service.

- ID: `username`
- Datatype: `string`
- Default Value: `None`



### Keycloak password

The password to authenticate with the Keycloak server of the marketplace service.

- ID: `password`
- Datatype: `password`
- Default Value: `None`

## Advanced Parameter

`None`
