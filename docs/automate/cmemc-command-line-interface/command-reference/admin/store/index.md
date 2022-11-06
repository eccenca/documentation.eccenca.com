---
title: "cmemc: Command Group - admin store"
description: "Import, export and bootstrap the knowledge graph store."
icon: material/database-outline
tags:
  - SPARQL
  - cmemc
---
# admin store Command Group

Import, export and bootstrap the knowledge graph store.

This command group consist of commands to administrate the
knowledge graph store as a whole.

## admin store showcase

Create showcase data.

This command creates a showcase scenario of multiple graphs including
integration graphs, shapes, statement annotations etc.

Note: There is currently no deletion mechanism for the showcase data, so
you need to remove the showcase graphs manually (or just remove all
graphs).

```shell-session
$ cmemc admin store showcase [OPTIONS]
```

```text
Usage: cmemc admin store showcase [OPTIONS]

  Create showcase data.

  This command creates a showcase scenario of multiple graphs including
  integration graphs, shapes, statement annotations etc.

  Note: There is currently no deletion mechanism for the showcase data, so
  you need to remove the showcase graphs manually (or just remove all
  graphs).

Options:
  --scale INTEGER  The scale factor provides a way to set the target size of
                   the scenario. A value of 10 results in around 40k triples,
                   a value of 50 in around 350k triples.  [default: 10]

  --create         Delete old showcase data if present and create new showcase
                   databased on the given scale factor.

  --delete         Delete existing showcase data if present.
```
## admin store bootstrap

Update/Import bootstrap data.

This command imports the bootstrap data needed for managing shapes,
access conditions, the query catalog and the vocabulary catalog.

Note: There is currently no deletion mechanism for the bootstrap data,
so you need to remove the graphs manually (or just remove all graphs).

```shell-session
$ cmemc admin store bootstrap [OPTIONS]
```

```text
Usage: cmemc admin store bootstrap [OPTIONS]

  Update/Import bootstrap data.

  This command imports the bootstrap data needed for managing shapes, access
  conditions, the query catalog and the vocabulary catalog.

  Note: There is currently no deletion mechanism for the bootstrap data, so
  you need to remove the graphs manually (or just remove all graphs).

Options:
  --import    Delete existing bootstrap data if present and import bootstrap
              data which was delivered
```
## admin store export

Backup all knowledge graphs to a ZIP archive.

The backup file is a ZIP archive containing all knowledge graphs as
Turtle files + configuration file for each graph.

This command will create lots of load on the server.
It can take a long time to complete.

```shell-session
$ cmemc admin store export [OPTIONS] BACKUP_FILE
```

```text
Usage: cmemc admin store export [OPTIONS] BACKUP_FILE

  Backup all knowledge graphs to a ZIP archive.

  The backup file is a ZIP archive containing all knowledge graphs as Turtle
  files + configuration file for each graph.

  This command will create lots of load on the server. It can take a long
  time to complete.

Options:
  --overwrite  Overwrite existing files. This is a dangerous option, so use it
               with care.
```
## admin store import

Restore graphs from a ZIP archive.

The backup file is a ZIP archive containing all knowledge graphs as
Turtle files + configuration file for each graph.

The command will load a single backup ZIP archive into the triple store,
by replacing all graphs with the content of the Turtle files in the
archive and deleting all graphs which are not in the archive.

This command will create lots of load on the server.
It can take a long time to complete.
The backup file will be transferred to the server, then unzipped and
imported graph by graph. After the initial transfer, the network
connection is not used anymore, so it will be closed by proxies sometimes.
This does not mean that the import failed.

```shell-session
$ cmemc admin store import [OPTIONS] BACKUP_FILE
```

```text
Usage: cmemc admin store import [OPTIONS] BACKUP_FILE

  Restore graphs from a ZIP archive.

  The backup file is a ZIP archive containing all knowledge graphs as Turtle
  files + configuration file for each graph.

  The command will load a single backup ZIP archive into the triple store,
  by replacing all graphs with the content of the Turtle files in the
  archive and deleting all graphs which are not in the archive.

  This command will create lots of load on the server. It can take a long
  time to complete. The backup file will be transferred to the server, then
  unzipped and imported graph by graph. After the initial transfer, the
  network connection is not used anymore, so it will be closed by proxies
  sometimes. This does not mean that the import failed.
```
