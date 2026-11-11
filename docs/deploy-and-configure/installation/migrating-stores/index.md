---
title: "Migrating to another store"
icon: material/database
tags:
    - Configuration
    - cmemc
---
# Migrate to another store

## Introduction

This page describes how to move an eccenca Corporate Memory deployment from one knowledge graph store to another, for example from OpenLink Virtuoso to Ontotext GraphDB.
The result is a deployment on the new store with the same knowledge graphs and Build (DataIntegration) projects as before.

The migration runs between two deployments: the existing one (source) and a new one on the target store (target).
The content moves with [cmemc](../../../automate/cmemc-command-line-interface/index.md).
Queries that use store-specific SPARQL extensions are adapted afterwards.

The following parts of a deployment are affected:

| Part | Where it is kept | Migration |
| --- | --- | --- |
| Knowledge graphs, including the query catalog, shapes and the workspace configuration | the store | export and import with cmemc |
| Build projects | graphs in the store, plus resource files held by Build | export and import with cmemc |
| Connection to the store | the configuration of Explore backend (DataPlatform) | configure for the target store |
| Connection of Build to the store | none, Build accesses the store through Explore backend | no change |

## Prerequisites

- Both deployments run the same Corporate Memory version.
- A cmemc connection to each deployment, with an account that may read and write all graphs and projects.
  In the examples on this page, the connections are named `source` and `target`.
- Disk space on the machine running cmemc for an export of all graphs and the workspace.

## 1. Deploy the target store

1. Size the target store for the data volume of the source deployment, see [Triple Store Sizing](../../requirements/triple-store-hardware-sizing.md).
2. Install and configure the store.
   Store settings that affect Corporate Memory are listed in [Quad Store Configuration](../../configuration/quad-store-configuration/index.md).

## 2. Connect Corporate Memory to the target store

1. Set up a Corporate Memory deployment as described in the [installation scenarios](../index.md).
2. Configure Explore backend for the target store.
   The `store` section of the configuration selects the store with `store.type` and holds the store-specific settings.
   See the store-specific configuration pages under [Explore backend (DataPlatform)](../../configuration/explore/dataplatform/index.md).
3. Leave the Build configuration as it is.
   With the default `backend` workspace provider, Build keeps its workspace in the store through Explore backend, see [Workspace Providers](../../configuration/dataintegration/index.md#workspace-providers).

## 3. Transfer the content

1. Export all knowledge graphs and the workspace from the source deployment:

    ```bash
    cmemc -c source admin store export
    cmemc -c source admin workspace export
    ```

    Both archives are needed.
    Build projects are stored as graphs, but only the workspace archive contains the resource files of the datasets.

2. Import both archives into the target deployment, the store archive first:

    ```bash
    cmemc -c target admin store import <date>-source.store.zip
    cmemc -c target admin workspace import <date>-source.workspace.zip
    ```

    !!! warning

        `admin store import` replaces all graphs of the target deployment and deletes every graph that is not part of the archive.

The export and import commands, their options and the parts of a deployment they do not cover are described in [Backup and Restore](../../../automate/cmemc-command-line-interface/backup-and-restore/index.md).
User accounts, installed Python packages and the deployment configuration are transferred separately.

## 4. Validate the migration

1. Compare the triple count of every graph on both deployments:

    ```bash
    cmemc -c source graph count --all > source-counts.txt
    cmemc -c target graph count --all > target-counts.txt
    diff source-counts.txt target-counts.txt
    ```

2. Check that all Build projects load without errors:

    ```bash
    cmemc -c target project status --all --exit-1
    ```

3. Compare the results of the `SELECT` queries in the query catalog.
   List them with `cmemc query list --filter type SELECT`, run each one on both deployments, and compare the output:

    ```bash
    cmemc -c source query execute <query-iri> --accept text/csv > source-result.csv
    cmemc -c target query execute <query-iri> --accept text/csv > target-result.csv
    diff source-result.csv target-result.csv
    ```

    Fill the placeholders of a parameterized query with `--parameter <key> <value>`.
    A query that fails on the target deployment or returns different results is adapted in the next step.

## 5. Adapt store-specific queries

Queries that use SPARQL extensions of the source store do not run on the target store, or return different results.
The most common case is full-text search, for example `bif:contains` in Virtuoso or the Lucene connector in GraphDB.
Such queries occur in the query catalog, in SHACL shapes, in the workspace configuration and in SPARQL tasks of Build projects.

1. Find catalog queries that use an extension with the `regex` filter, which matches the query text:

    ```bash
    cmemc -c target query list --filter regex 'bif:contains'
    ```

2. Rewrite each query for the target store.
3. Compare the execution times on both deployments with `cmemc query replay`, to find queries that run noticeably slower on the target store.
   A replay file lists the queries to run, see [query replay](../../../automate/cmemc-command-line-interface/command-reference/query/index.md#query-replay).
   Queries with placeholders fail in a replay, because `query replay` ignores placeholders.

    !!! warning

        `query replay` also runs update queries.
        Put only `SELECT` queries into a replay file used for a comparison.

!!! tip

    Replace a filter on a fixed list of values, such as `FILTER (?x IN (...))`, with a `VALUES` block.
    Many stores evaluate a `VALUES` block more efficiently.
