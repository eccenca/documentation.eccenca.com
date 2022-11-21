---
icon: material/database
---
# Migrating Stores

## Sizing and Deployment

- size and deploy of the new store (refer to the capacity planning / sizing considerations, refer to the docker container / orchestration)
- store specific config (e.g. search-all-graphs in SD)

## Transferring Data and Configuration

- backing-up / exporting and restore / import of graphs, DI-projects, configuration (if any)
    - graphs
        - blacklisting the DI projects graphs
    - config
        - DM
            - stardog text match support (this is a DM parameter!)
            - search queries
            - navigation
    - DP
        - configure the resp. store
    - DI
        - nothing to do ... just duplicate / copy the configuration as-is
        - `cmemc admin workspace export / import`

## Test and Validation

- best practice:
    - run all (SELECT) queries in the query catalog and compare results (e.g. with `cmemc`)
        -  theoretically this could also be applied to INSERT queries (by re-writing into SELECTS in case you want / need to omit altering your graphs)
    - count all triples in all graphs on both instances before/after export/import (`cmemc graph count --all`)

## Optimizing Your Setup

- optimizing customization (e.g. queries in SHAPES; DI; DM-config)
    - "textmatch" / "lucene" queries need to be migrated (a query can be helpful to find these queries...)
    - performance comparisons could be automated via `cmemc query replay`
        - identify query that won't run or run slow
- general query best practices
    - → query optimization guide
        - use `VALUE` instead of `FILTER (?x IN (...))` (esp. on GDB)
