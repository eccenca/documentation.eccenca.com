---
title: "cmemc: Command Group - admin store"
description: "Import, export and bootstrap the knowledge graph store."
icon: material/database-outline
tags:
  - SPARQL
  - cmemc
---
# admin store Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Import, export and bootstrap the knowledge graph store.

This command group consist of commands to administrate the knowledge graph store as a whole.


## admin store showcase

Create showcase data.

```shell-session title="Usage"
$ cmemc admin store showcase [OPTIONS]
```




This command creates a showcase scenario of multiple graphs including integration graphs, shapes, statement annotations, etc.

!!! note
    There is currently no deletion mechanism for the showcase data, and you need to remove the showcase graphs manually (or just remove all graphs).




??? info "Options"
    ```text

    --scale INTEGER  The scale factor provides a way to set the target size of
                     the scenario. A value of 10 results in around 40k triples,
                     a value of 50 in around 350k triples.  [default: 10]
    --create         Delete old showcase data if present and create new showcase
                     databased on the given scale factor.
    --delete         Delete existing showcase data if present.
    ```

## admin store bootstrap

Update/Import or remove bootstrap data.

```shell-session title="Usage"
$ cmemc admin store bootstrap [OPTIONS]
```




Use ``--import`` to import the bootstrap data needed for managing shapes and configuration objects. This will remove the old data first.

Use ``--remove`` to delete bootstrap data.

!!! note
    The removal of existing bootstrap data will search for resources which are flagged with the isSystemResource property.




??? info "Options"
    ```text

    --import    Delete existing bootstrap data if present and import bootstrap
                data which was delivered with Corporate Memory.
    --remove    Delete existing bootstrap data if present.
    ```

## admin store export

Backup all knowledge graphs to a ZIP archive.

```shell-session title="Usage"
$ cmemc admin store export [OPTIONS] BACKUP_FILE
```




The backup file is a ZIP archive containing all knowledge graphs (one Turtle file + configuration file per graph).

This command will create lots of load on the server. It can take a long time to complete.



??? info "Options"
    ```text

    --overwrite  Overwrite existing files. This is a dangerous option, so use it
                 with care.
    ```

## admin store import

Restore graphs from a ZIP archive.

```shell-session title="Usage"
$ cmemc admin store import BACKUP_FILE
```




The backup file is a ZIP archive containing all knowledge graphs  (one Turtle file + configuration file per graph).

The command will load a single backup ZIP archive into the triple store by replacing all graphs with the content of the Turtle files in the archive and deleting all graphs which are not in the archive.

This command will create lots of load on the server. It can take a long time to complete. The backup file will be transferred to the server, then unzipped and imported graph by graph. After the initial transfer the network connection is not used anymore and may be closed by proxies. This does not mean that the import failed.



## admin store migrate

Migrate configuration resources to the current version.

```shell-session title="Usage"
$ cmemc admin store migrate [OPTIONS]
```




This command serves two purposes: (1) When invoked without an option, it lists all migrateable configuration resources. (2) When invoked with the ``--workspaces`` option, it migrates the workspace configurations to the current version.



??? info "Options"
    ```text

    --workspaces  Migrate workspace configurations to the current version.
    ```

