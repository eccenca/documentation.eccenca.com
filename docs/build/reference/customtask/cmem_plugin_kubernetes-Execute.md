---
title: "Execute a command in a kubernetes pod"
description: "Connect to a cluster, execute a command and gather the output."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Execute a command in a kubernetes pod

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This plugin enables execution of commands inside Kubernetes pods and captures their output.

## Features

- Supports multiple connection types:
    - **In-cluster**: Uses the service account kubernetes gives to pods
    (for plugins running inside k8s)

    - **Explicit config**: Uses a YAML kubeconfig file for external connections
- Executes shell commands in specified pods within namespaces
- Captures both stdout and stderr output
- Returns command output as a file entity for further processing
- Includes namespace listing functionality to verify cluster access and connectivity

## Output

Command output is captured and returned as a text file entity that can be consumed by
downstream workflow tasks.

## Use Cases

- Running external pipelines
- Running diagnostic commands in production pods
- Executing maintenance scripts from within or outside the cluster
- Gathering system information and logs
- Performing health checks and troubleshooting

## Parameter

### Config Type

The type of configuration you wish to use.

- ID: `config_type`
- Datatype: `string`
- Default Value: `explicit`

### Namespace

Namespaces provide a mechanism for isolating groups of resources.

- ID: `namespace`
- Datatype: `string`
- Default Value: `None`

### Pod

Pods are an abstraction that represent groups of one or more application containers (such as Docker), and some shared resources for those containers.

- ID: `pod`
- Datatype: `string`
- Default Value: `None`

### Container

In case there is more than one container in the pod OR the default container selection does not work, you need to specify the container ID in addition to the pod ID.

- ID: `container`
- Datatype: `string`
- Default Value: `None`

### Command

The command to execute.

- ID: `command`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### Kube Config

YAML source code of the kube config.

- ID: `kube_config`
- Datatype: `code-yaml`
- Default Value: `None`
