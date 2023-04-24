---
title: "cmemc: Command Reference"
description: "This page lists all commands with its short descriptions."
icon: octicons/cross-reference-24
tags:
  - Reference
  - cmemc
---
# Command Reference
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! info

    cmemc is organized as a tree of command groups, each with a set of
    commands. You can access the command groups in the table as well as in the
    navigation on the left. You can access the commands directly from the table
    or by visiting a command group page first.

| Command Group | Command | Description |
| ------------: | :------ | :---------- |
| [admin](admin/index.md) | [status](admin/index.md#admin-status) | Output health and version information. |
| [admin](admin/index.md) | [token](admin/index.md#admin-token) | Fetch and output an access token. |
| [admin metrics](admin/metrics/index.md) | [get](admin/metrics/index.md#admin-metrics-get) | Get sample data of a metric. |
| [admin metrics](admin/metrics/index.md) | [inspect](admin/metrics/index.md#admin-metrics-inspect) | Inspect a metric. |
| [admin metrics](admin/metrics/index.md) | [list](admin/metrics/index.md#admin-metrics-list) | List metrics for a specific job. |
| [admin store](admin/store/index.md) | [showcase](admin/store/index.md#admin-store-showcase) | Create showcase data. |
| [admin store](admin/store/index.md) | [bootstrap](admin/store/index.md#admin-store-bootstrap) | Update/Import bootstrap data. |
| [admin store](admin/store/index.md) | [export](admin/store/index.md#admin-store-export) | Backup all knowledge graphs to a ZIP archive. |
| [admin store](admin/store/index.md) | [import](admin/store/index.md#admin-store-import) | Restore graphs from a ZIP archive. |
| [admin user](admin/user/index.md) | [list](admin/user/index.md#admin-user-list) | List user accounts. |
| [admin user](admin/user/index.md) | [create](admin/user/index.md#admin-user-create) | Create a user account. |
| [admin user](admin/user/index.md) | [update](admin/user/index.md#admin-user-update) | Update a user account. |
| [admin user](admin/user/index.md) | [delete](admin/user/index.md#admin-user-delete) | Delete a user account. |
| [admin user](admin/user/index.md) | [password](admin/user/index.md#admin-user-password) | Change the password of a user account. |
| [admin user](admin/user/index.md) | [open](admin/user/index.md#admin-user-open) | Open user in the browser. |
| [admin workspace](admin/workspace/index.md) | [export](admin/workspace/index.md#admin-workspace-export) | Export the complete workspace (all projects) to a ZIP file. |
| [admin workspace](admin/workspace/index.md) | [import](admin/workspace/index.md#admin-workspace-import) | Import the workspace from a file. |
| [admin workspace](admin/workspace/index.md) | [reload](admin/workspace/index.md#admin-workspace-reload) | Reload the workspace from the backend. |
| [admin workspace python](admin/workspace/python/index.md) | [install](admin/workspace/python/index.md#admin-workspace-python-install) | Install a python package to the workspace. |
| [admin workspace python](admin/workspace/python/index.md) | [uninstall](admin/workspace/python/index.md#admin-workspace-python-uninstall) | Uninstall a python package from the workspace. |
| [admin workspace python](admin/workspace/python/index.md) | [list](admin/workspace/python/index.md#admin-workspace-python-list) | List installed python packages. |
| [admin workspace python](admin/workspace/python/index.md) | [list-plugins](admin/workspace/python/index.md#admin-workspace-python-list-plugins) | List installed workspace plugins. |
| [config](config/index.md) | [list](config/index.md#config-list) | List configured connections. |
| [config](config/index.md) | [edit](config/index.md#config-edit) | Edit the user-scope configuration file. |
| [config](config/index.md) | [get](config/index.md#config-get) | Get the value of a known cmemc configuration key. |
| [config](config/index.md) | [eval](config/index.md#config-eval) | Export all configuration values of a configuration for evaluation. |
| [dataset](dataset/index.md) | [list](dataset/index.md#dataset-list) | List available datasets. |
| [dataset](dataset/index.md) | [delete](dataset/index.md#dataset-delete) | Delete datasets. |
| [dataset](dataset/index.md) | [download](dataset/index.md#dataset-download) | Download the resource file of a dataset. |
| [dataset](dataset/index.md) | [upload](dataset/index.md#dataset-upload) | Upload a resource file to a dataset. |
| [dataset](dataset/index.md) | [inspect](dataset/index.md#dataset-inspect) | Display metadata of a dataset. |
| [dataset](dataset/index.md) | [create](dataset/index.md#dataset-create) | Create a dataset. |
| [dataset](dataset/index.md) | [open](dataset/index.md#dataset-open) | Open datasets in the browser. |
| [dataset resource](dataset/resource/index.md) | [list](dataset/resource/index.md#dataset-resource-list) | List available file resources. |
| [dataset resource](dataset/resource/index.md) | [delete](dataset/resource/index.md#dataset-resource-delete) | Delete file resources. |
| [dataset resource](dataset/resource/index.md) | [inspect](dataset/resource/index.md#dataset-resource-inspect) | Display all metadata of a file resource. |
| [dataset resource](dataset/resource/index.md) | [usage](dataset/resource/index.md#dataset-resource-usage) | Display all usage data of a file resource. |
| [graph](graph/index.md) | [count](graph/index.md#graph-count) | Count triples in graph(s). |
| [graph](graph/index.md) | [tree](graph/index.md#graph-tree) | Show graph tree(s) of the owl:imports hierarchy. |
| [graph](graph/index.md) | [list](graph/index.md#graph-list) | List accessible graphs. |
| [graph](graph/index.md) | [export](graph/index.md#graph-export) | Export graph(s) as NTriples to stdout (-), file or directory. |
| [graph](graph/index.md) | [delete](graph/index.md#graph-delete) | Delete graph(s) from the store. |
| [graph](graph/index.md) | [import](graph/index.md#graph-import) | Import graph(s) to the store. |
| [graph](graph/index.md) | [open](graph/index.md#graph-open) | Open / explore a graph in the browser. |
| [project](project/index.md) | [open](project/index.md#project-open) | Open projects in the browser. |
| [project](project/index.md) | [list](project/index.md#project-list) | List available projects. |
| [project](project/index.md) | [export](project/index.md#project-export) | Export projects to files. |
| [project](project/index.md) | [import](project/index.md#project-import) | Import a project from a file or directory. |
| [project](project/index.md) | [delete](project/index.md#project-delete) | Delete projects. |
| [project](project/index.md) | [create](project/index.md#project-create) | Create projects. |
| [project](project/index.md) | [reload](project/index.md#project-reload) | Reload projects from the workspace provider. |
| [query](query/index.md) | [execute](query/index.md#query-execute) | Execute queries which are loaded from files or the query catalog. |
| [query](query/index.md) | [list](query/index.md#query-list) | List available queries from the catalog. |
| [query](query/index.md) | [open](query/index.md#query-open) | Open queries in the editor of the query catalog in your browser. |
| [query](query/index.md) | [status](query/index.md#query-status) | Get status information of executed and running queries. |
| [query](query/index.md) | [replay](query/index.md#query-replay) | Re-execute queries from a replay file. |
| [query](query/index.md) | [cancel](query/index.md#query-cancel) | Cancel a running query. |
| [vocabulary](vocabulary/index.md) | [open](vocabulary/index.md#vocabulary-open) | Open / explore a vocabulary graph in the browser. |
| [vocabulary](vocabulary/index.md) | [list](vocabulary/index.md#vocabulary-list) | Output a list of vocabularies. |
| [vocabulary](vocabulary/index.md) | [install](vocabulary/index.md#vocabulary-install) | Install one or more vocabularies from the catalog. |
| [vocabulary](vocabulary/index.md) | [uninstall](vocabulary/index.md#vocabulary-uninstall) | Uninstall one or more vocabularies. |
| [vocabulary](vocabulary/index.md) | [import](vocabulary/index.md#vocabulary-import) | Import a turtle file as a vocabulary. |
| [vocabulary cache](vocabulary/cache/index.md) | [update](vocabulary/cache/index.md#vocabulary-cache-update) | Reload / updates the data integration cache for a vocabulary. |
| [vocabulary cache](vocabulary/cache/index.md) | [list](vocabulary/cache/index.md#vocabulary-cache-list) | Output the content of the global vocabulary cache. |
| [workflow](workflow/index.md) | [execute](workflow/index.md#workflow-execute) | Execute workflow(s). |
| [workflow](workflow/index.md) | [io](workflow/index.md#workflow-io) | Execute a workflow with file input/output. |
| [workflow](workflow/index.md) | [list](workflow/index.md#workflow-list) | List available workflow. |
| [workflow](workflow/index.md) | [status](workflow/index.md#workflow-status) | Get status information of workflow(s). |
| [workflow](workflow/index.md) | [open](workflow/index.md#workflow-open) | Open a workflow in your browser. |
| [workflow scheduler](workflow/scheduler/index.md) | [open](workflow/scheduler/index.md#workflow-scheduler-open) | Open scheduler(s) in the browser. |
| [workflow scheduler](workflow/scheduler/index.md) | [list](workflow/scheduler/index.md#workflow-scheduler-list) | List available scheduler. |
| [workflow scheduler](workflow/scheduler/index.md) | [inspect](workflow/scheduler/index.md#workflow-scheduler-inspect) | Display all metadata of a scheduler. |
| [workflow scheduler](workflow/scheduler/index.md) | [disable](workflow/scheduler/index.md#workflow-scheduler-disable) | Disable scheduler(s). |
| [workflow scheduler](workflow/scheduler/index.md) | [enable](workflow/scheduler/index.md#workflow-scheduler-enable) | Enable scheduler(s). |

