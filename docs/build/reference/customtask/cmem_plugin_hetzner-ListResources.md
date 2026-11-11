---
title: "Hetzner Cloud: List Resources"
description: "Inventory all existing resources of a Hetzner Cloud project (servers, volumes, networks, load balancers, IPs, firewalls, SSH keys, snapshots, …), one entity per resource in a single union schema."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Hetzner Cloud: List Resources

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow operator inventories the resources actually provisioned in a
Hetzner Cloud project, using the [Hetzner Cloud API](https://docs.hetzner.cloud/).
It complements **Hetzner Cloud: List Server Types** (the catalog of what you
*could* create) by listing what you *have*.

It produces one entity per resource across 11 resource types: `server`,
`volume`, `network`, `load_balancer`, `floating_ip`, `primary_ip`, `firewall`,
`ssh_key`, `image`, `certificate` and `placement_group`. All entities share a
single union schema; the `resourceType` column discriminates each row's type,
and each row fills its shared columns plus its own type's columns. A column
that does not apply to a row carries no value at all, rather than an empty one.

Images are restricted to project-owned snapshots and backups; the shared
system / app OS catalog is excluded. Since the Hetzner API names only system
images, the `name` of a snapshot or backup falls back to its description.

Note that `ipv6` holds the routed IPv6 network in CIDR notation for a server,
and a single address for the IP resources.

## Authentication

You need a Hetzner Cloud API token of a project (Console → Security → API
Tokens). A read-only token is sufficient.

## Filters

All filters are optional. Leave them empty to inventory everything. A filter
that matches nothing yields an empty result, which the execution report states.

Located resources are the server, volume, primary IP, load balancer and
floating IP (by its home location). The network, firewall, SSH key, image,
certificate and placement group are global in the Hetzner API and always pass
the location filter.


## Parameter

### API Token

A Hetzner Cloud project API token (read-only is sufficient).

- ID: `api_token`
- Datatype: `password`
- Default Value: `None`

## Advanced Parameter

### Resource type

Restrict to a single resource type. Empty lists all types.

- ID: `resource_type`
- Datatype: `string`
- Default Value: `None`



### Label selector

A Hetzner label selector (e.g. env=prod), applied server-side.

- ID: `label_selector`
- Datatype: `string`
- Default Value: `None`



### Location

Restrict located resources to a single location name (e.g. fsn1). Empty lists all. Global resources always pass through.

- ID: `location`
- Datatype: `string`
- Default Value: `None`
