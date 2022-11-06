---
title: "cmemc: Command Group - vocabulary cache"
description: "List und update the vocabulary cache."
icon: material/cached
tags:
  - Vocabulary
  - cmemc
---
# vocabulary cache Command Group

List und update the vocabulary cache.

## vocabulary cache update

Reload / updates the data integration cache for a vocabulary.

```shell-session
$ cmemc vocabulary cache update [OPTIONS] [IRIS]...
```

```text
Usage: cmemc vocabulary cache update [OPTIONS] [IRIS]...

  Reload / updates the data integration cache for a vocabulary.

Options:
  -a, --all   Update cache for all installed vocabularies.
```
## vocabulary cache list

Output the content of the global vocabulary cache.

```shell-session
$ cmemc vocabulary cache list [OPTIONS]
```

```text
Usage: cmemc vocabulary cache list [OPTIONS]

  Output the content of the global vocabulary cache.

Options:
  --id-only   Lists only vocabulary term identifier (IRIs) and no labels or
              other meta data. This is useful for piping the ids into other
              cmemc commands.

  --raw       Outputs raw JSON.
```
