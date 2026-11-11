---
title: "Hetzner Cloud: List Server Types"
description: "List all available Hetzner Cloud server (VM) types, one entity per server type and location, including specs and per-location pricing."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Hetzner Cloud: List Server Types

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow operator lists the available server (virtual machine) types of the
Hetzner Cloud, using the [Hetzner Cloud API](https://docs.hetzner.cloud/).

It produces one entity per **(server type x location)** offering. Each entity
carries the server type specification (cores, memory, disk, CPU type,
architecture, …), the per-location availability, and the per-location price.

Booleans are written in their XSD form (`true` / `false`), and a property a
server type does not carry is left out of the entity rather than written as an
empty value.

## Authentication

You need a Hetzner Cloud API token of a project (Console → Security → API
Tokens). A read-only token is sufficient.

## Filters

All filters are optional. Leave them empty (or `false`) to list everything. A
filter that matches nothing yields an empty result, which the execution report
states.


## Parameter

### API Token

A Hetzner Cloud project API token (read-only is sufficient).

- ID: `api_token`
- Datatype: `password`
- Default Value: `None`

## Advanced Parameter

### Architecture

Restrict to a CPU architecture. Empty lists any architecture.

- ID: `architecture`
- Datatype: `string`
- Default Value: `None`



### CPU Type

Restrict to a CPU type. Empty lists any CPU type.

- ID: `cpu_type`
- Datatype: `string`
- Default Value: `None`



### Location

Restrict to a single location name (e.g. fsn1). Empty lists all.

- ID: `location`
- Datatype: `string`
- Default Value: `None`



### Only available

If enabled, list only offerings currently available in their location.

- ID: `only_available`
- Datatype: `boolean`
- Default Value: `false`



### Exclude deprecated

If enabled, drop offerings that are deprecated in their location.

- ID: `exclude_deprecated`
- Datatype: `boolean`
- Default Value: `false`
