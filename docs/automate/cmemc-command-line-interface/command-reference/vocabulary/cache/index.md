---
title: "cmemc: Command Group - vocabulary cache"
description: "List und update the vocabulary cache."
icon: eccenca/application-vocabularies
tags:
  - Vocabulary
  - cmemc
---
# vocabulary cache Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List und update the vocabulary cache.

## vocabulary cache update

Reload / updates the data integration cache for a vocabulary.

```shell-session title="Usage"
cmemc vocabulary cache update [OPTIONS] [IRIS]...
```

??? info "Options"
    ```text

    -a, --all   Update cache for all installed vocabularies.
    ```

## vocabulary cache list

Output the content of the global vocabulary cache.

```shell-session title="Usage"
cmemc vocabulary cache list [OPTIONS]
```

??? info "Options"
    ```text

    --id-only   Lists only vocabulary term identifier (IRIs) and no labels or
                other metadata. This is useful for piping the ids into other
                cmemc commands.
    --raw       Outputs raw JSON.
    ```
