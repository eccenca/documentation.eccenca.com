---
tags:
    - Configuration
---

## Configuration for connecting to internal memory backend

You can configure a in-memory SPARQL backend. Based on Jena Models, in-memory backends do not provide persistent storage.
Hence, shutting down a DataPlatform configured with an in-memory backend deletes your data and therefore you should use it only for testing purposes.

Configuration example:

This example configures an in-memory store which initializes with the triples contained in the given file.

```yaml
store:
  type: memory
  authorization: REWRITE_FROM
  memory:
    files:
      - "/data/data.trig"
```


***Property: store.type***

The type of the store must be set to "memory"

| Category | Value |
|--- | ---: |
| Default | memory |
| Required | true |
| Valid values | MEMORY |
| Environment | STORE_TYPE |

***Property: store.authorization***


| Category | Value |
|--- | ---: |
| Default | REWRITE_FROM |
| Required | false |
| Valid values | string |
| Environment | STORE_AUTHORIZATION |

Specific settings for in-memory backend

***Property: store.memory.files***

list of files in file URI scheme

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | A list of files |
| Environment | STORE_MEMORY_FILES |

