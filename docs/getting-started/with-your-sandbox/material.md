---
comments: false
hide:
  - toc
  - navigation
---

# Masterclass - Material and Namespace Suggestions

A list of materials and resources to reproduce and follow the masterclass.

!!! info "About Session"

    This masterclass provides the foundation of KG solutions based on the eccenca Corporate Memory platform. The platform covers the full lifecycle of KG applications. Our partners and experts love it for its productivity, ease of use and level of automation in KG creation and evolution. It boosts your abilities to capture, access and re-use knowledge from your organization in a whole new way. Join our tutors to learn about the platform and what it can do in your KG projects.

<div class="grid cards" markdown>

-   ## File resources

    ---

    | Type           | Name                       | Resource                                                           |
    | -------------- | -------------------------- | ------------------------------------------------------------------ |
    | Dataset (XLSX) | Hardware Products          | [hardware.xlsx](./material/resources/hardware.xlsx){target=_blank} |
    | Dataset (CSV)  | Service Products           | [services.csv](./material/resources/services.csv){target=_blank}   |
    | Dataset (JSON) | Supplier                   | [supplier.json](./material/resources/supplier.json){target=_blank} |
    | Dataset (XML)  | Organizational Information | [orgmap.xml](./material/resources/orgmap.xml){target=_blank}       |
    | Vocabulary     | Products Vocabulary*       | [pv.ttl](./material/vocabs/pv.ttl){target=_blank}                  |

    *) FYI, vocabulary already installed

-   ## Name(space) suggestions

    ---

    | Type          | Name                    | IRI                                  |
    | ------------- | ----------------------- | ------------------------------------ |
    | Dataset (KG)  | KGC Prod - Integration  | `http://kgc.eccenca.com/prod-int/`   |
    | Dataset (KG)  | KGC Prod - Hardware     | `http://kgc.eccenca.com/prod-hw/`    |
    | Dataset (KG)  | KGC Prod - Services     | `http://kgc.eccenca.com/prod-srv/`   |
    | Dataset (KG)  | KGC Prod - Supplier     | `http://kgc.eccenca.com/prod-suppl/` |
    | Dataset (KG)  | KGC Prod - Organization | `http://kgc.eccenca.com/prod-org/`   |
    | Dataset (KG)  | KGC Prod - Links        | `http://kgc.eccenca.com/prod-links/` |
    | Build Project | KGC Product Build Demo  |                                      |

-   ## Resource IRI suggestions

    ---

    | Type             | IRI                                                             |
    | ---------------- | --------------------------------------------------------------- |
    | Department       | `http://kgc.eccenca.com/prod-data/dept-{id}`                    |
    | Employee         | `http://kgc.eccenca.com/prod-data/empl-{email}`                 |
    | Hardware         | `http://kgc.eccenca.com/prod-data/hw-{id}`                      |
    | Price            | `http://kgc.eccenca.com/prod-data/price-{parent-id}-{currency}` |
    | Product Category | `http://kgc.eccenca.com/prod-data/prod-cat-{name|uuid}`         |
    | Service          | `http://kgc.eccenca.com/prod-data/srv-{id}`                     |
    | Supplier         | `http://kgc.eccenca.com/prod-data/suppl-{id}`                   |

</div>
