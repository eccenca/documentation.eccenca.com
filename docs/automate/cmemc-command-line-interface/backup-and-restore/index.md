---
title: "cmemc: Backup and Restore"
icon: material/backup-restore
tags:
  - Automate
  - cmemc
---
# Backup and Restore

## Introduction

cmemc can export and re-import all data which eccenca Corporate Memory manages: the knowledge graphs in the store, the projects in the workspace, and any subset of them.
This page describes which artifacts you can create, how to restore each of them, and - just as important - which parts of a deployment cmemc does **not** cover.

!!! warning "A cmemc export is not a complete instance backup"

    The commands on this page back up the *content* of Corporate Memory.
    They do not back up your user accounts, your installed python packages or your deployment configuration.
    Refer to [What cmemc does not back up](#what-cmemc-does-not-back-up) below before you rely on these artifacts for disaster recovery.

## Backup artifacts at a glance

| Scope | Export command | Restore command |
| ----- | -------------- | --------------- |
| All knowledge graphs | `admin store export` | `admin store import` |
| All projects (workspace) | `admin workspace export` | `admin workspace import` |
| A single project | `project export` | `project import` |
| Selected graphs | `graph export` | `graph import` |

The store archive and the workspace archive overlap only partly: projects are represented as graphs in the store as well, but the workspace archive additionally contains the resource files of your datasets.
A complete content backup therefore consists of **both** archives.

## Backing up the content of an instance

Both export commands generate a file name if you do not provide one:

``` shell-session title="a complete content backup"
$ cmemc -c my-cmem admin store export
Exporting graphs backup to 2026-08-21-my-cmem.store.zip ... done
$ cmemc -c my-cmem admin workspace export
Export workspace to 2026-08-21-my-cmem.workspace.zip ... done
```

The generated name is built from the `--filename-template` option, which defaults to a template using the `{{date}}` and `{{connection}}` placeholders.
Without a `--connection` option, the connection part of the name becomes `unnamed`, so using `-c` is recommended when you archive backups of several instances side by side.

Use `--replace` to overwrite an existing file with the same name, for example when a scheduled job runs more than once a day.

!!! info

    `admin store export` reads every graph of your instance and creates significant load on the server.
    On a large instance it can take a long time to complete, so schedule it accordingly.

## Restoring the content of an instance

!!! danger "`admin store import` replaces the whole store"

    This command does not merge.
    It replaces all graphs with the content of the archive **and deletes all graphs which are not part of the archive**.
    Make sure the archive is the one you intend to restore before running it.

``` shell title="restore all graphs and the workspace"
cmemc -c my-cmem admin store import 2026-08-21-my-cmem.store.zip
cmemc -c my-cmem admin workspace import 2026-08-21-my-cmem.workspace.zip
```

!!! info "A quiet connection does not mean a failed import"

    `admin store import` transfers the archive to the server first, and the server then unzips and imports it graph by graph.
    After the initial transfer, the network connection is no longer used and may be closed by a reverse proxy or load balancer.
    This does not mean the import failed - the server continues to work on it.

## Backing up single projects

For moving work between instances, or for keeping a project in a git repository, exporting a single project is usually the better tool:

``` shell-session title="export one project"
$ cmemc project export my-project
Export project 1/1: my-project to 2026-08-21-my-cmem-my-project.project.zip ... done
```

Restoring works into any project identifier, so you can import a project archive next to the original one - which is a good way to test that an archive is intact:

``` shell-session title="restore a project under a different identifier"
$ cmemc project import 2026-08-21-my-cmem-my-project.project.zip restore-check
Import file 2026-08-21-my-cmem-my-project.project.zip to project restore-check ... done
```

Use the `--replace` option of `project import` to overwrite an existing project instead.

## Backing up single graphs

`graph export` writes selected graphs to a directory, creating a `.ttl` file with the triples and a `.ttl.graph` file holding the graph IRI for each of them:

``` shell-session title="export a graph to a directory"
$ cmemc graph export --output-dir graphs -t "{{date}}-{{iriname}}" https://ns.eccenca.com/data/config/
Export graph 1/1: https://ns.eccenca.com/data/config/ to graphs/2026-08-21-https__ns_eccenca_com_data_config.ttl ... done
```

This file pair is what makes a directory restorable: `graph import` scans a directory for such pairs and writes each file back into the graph named in its companion file.

``` shell title="restore all graphs of a directory"
cmemc graph import --replace graphs
```

!!! warning

    Without `--replace`, `graph import` **adds** the triples to the existing graph instead of overwriting it.
    For a restore, this is almost never what you want, since it merges the backup into whatever is currently in the graph.

Add `--include-imports` to `graph export` if the selected graphs use `owl:imports` and you need the complete import closure in your backup.
The [Command Reference](../command-reference/index.md) describes the remaining options, such as `--create-catalog` and `--compress`.

## What cmemc does not back up

The following parts of a deployment are outside of the Corporate Memory APIs and therefore outside of what cmemc can export:

- **User accounts, groups and clients.** These live in Keycloak and are backed up together with the Keycloak database.
- **Python packages installed in the workspace.** cmemc can install and uninstall them, but it cannot export the package files.
- **Deployment configuration.** The `application.yaml` files, reverse proxy configuration and container orchestration are part of your deployment, not of Corporate Memory's content.

For a full-instance procedure which covers these parts as well, refer to the backup section of the [local installation scenario](../../../deploy-and-configure/installation/scenario-local-installation/index.md).

### Reconstructing installed python packages

While the package files can not be archived, the *list* of installed packages can, which is usually enough to reproduce the environment:

``` shell title="record the installed packages"
cmemc -c my-cmem admin workspace python list --id-only > python-packages.txt
```

Note that this list contains the complete python environment of the workspace, including the packages which come with the Corporate Memory image.
Do not simply reinstall all of them after a restore.
Use the recorded list to identify the packages **you** added, and install those again:

``` shell title="reinstall a plugin package"
cmemc -c my-cmem admin workspace python install cmem-plugin-example==1.0.0
```

The `admin workspace python list-plugins` command helps here, since plugin discovery is restricted to packages with a `cmem-` prefix and therefore shows a much shorter list than `list`.

## Exports without user-identifying data

Since v26.2, `project export` and `admin workspace export` support the `--without-userdata` option.
It removes creation and modification timestamps as well as account names from the exported archive.

``` shell-session title="export a project without user-identifying metadata"
$ cmemc project export --without-userdata my-project
```

Use this whenever an export leaves your organisation, for example when a project archive is attached to a support ticket or published in a repository.

## Verifying a restore

After restoring, a short check confirms that the instance came up with the expected content:

``` shell title="check components, projects and graph sizes"
cmemc admin status
cmemc project status --all --exit-1
cmemc graph list --id-only | xargs cmemc graph count
```

`project status --all --exit-1` is particularly useful in a restore pipeline, since it exits with code 1 if any project has task loading errors.
Refer to [Scripting with cmemc](../scripting-with-cmemc/index.md#exit-codes) for the exit code conventions.

## Where to go from here

- [Scripting with cmemc](../scripting-with-cmemc/index.md) - exit codes and machine-readable output for backup jobs.
- [Using the Docker Image](../invocation/docker-image/index.md) - running backup jobs in a container with mounted volumes.
- [Continuous Integration and Delivery](../../continuous-integration/index.md) - automating activities on your instances.
