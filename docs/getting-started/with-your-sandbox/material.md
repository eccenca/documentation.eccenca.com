---
comments: false
hide:
  - toc
  - navigation
---

# Masterclass - Material and Namespace Suggestions

A list of materials and resources to reproduce and follow the masterclass (MC).

!!! info "About Session"

    This masterclass provides the foundation of KG solutions based on the eccenca Corporate Memory platform. The platform covers the full lifecycle of KG applications. Our partners and experts love it for its productivity, ease of use and level of automation in KG creation and evolution. It boosts your abilities to capture, access and re-use knowledge from your organization in a whole new way. Join our tutors to learn about the platform and what it can do in your KG projects.

<div class="grid cards" markdown>

- ## File resources

    ---

    | Type           | Name                       | Resource                                                           |
    | -------------- | -------------------------- | ------------------------------------------------------------------ |
    | Dataset (XLSX) | Hardware Products          | [hardware.xlsx](./material/resources/hardware.xlsx){target=_blank} |
    | Dataset (CSV)  | Service Products           | [services.csv](./material/resources/services.csv){target=_blank}   |
    | Dataset (JSON) | Supplier                   | [supplier.json](./material/resources/supplier.json){target=_blank} |
    | Dataset (XML)  | Organizational Information | [orgmap.xml](./material/resources/orgmap.xml){target=_blank}       |
    | Vocabulary*    | Products Vocabulary        | [pv.ttl](./material/vocabs/pv.ttl){target=_blank}                  |

    *) vocabulary already installed, attached for information purposes only.

- ## Name(space) suggestions

    ---

    | Type          | Name                   | IRI                                 |
    | ------------- | ---------------------- | ----------------------------------- |
    | Dataset (KG)  | MC Prod - Integration  | `http://mc.eccenca.com/prod-int/`   |
    | Dataset (KG)  | MC Prod - Hardware     | `http://mc.eccenca.com/prod-hw/`    |
    | Dataset (KG)  | MC Prod - Services     | `http://mc.eccenca.com/prod-srv/`   |
    | Dataset (KG)  | MC Prod - Supplier     | `http://mc.eccenca.com/prod-suppl/` |
    | Dataset (KG)  | MC Prod - Organization | `http://mc.eccenca.com/prod-org/`   |
    | Dataset (KG)  | MC Prod - Links        | `http://mc.eccenca.com/prod-links/` |
    | Build Project | MC Product Build Demo  |                                     |

- ## Resource IRI suggestions

    ---

    | Type             | IRI                                                            |
    | ---------------- | -------------------------------------------------------------- |
    | Department       | `http://mc.eccenca.com/prod-data/dept-{id}`                    |
    | Employee         | `http://mc.eccenca.com/prod-data/empl-{email}`                 |
    | Hardware         | `http://mc.eccenca.com/prod-data/hw-{id}`                      |
    | Price            | `http://mc.eccenca.com/prod-data/price-{parent-id}-{currency}` |
    | Product Category | `http://mc.eccenca.com/prod-data/prod-cat-{uuid(name)}`        |
    | Service          | `http://mc.eccenca.com/prod-data/srv-{id}`                     |
    | Supplier         | `http://mc.eccenca.com/prod-data/suppl-{id}`                   |

</div>
