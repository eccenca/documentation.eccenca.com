---
icon: material/memory
title: "Triple Store Sizing"
---

# Triple Store Sizing

The following table provides a generic sizing orientation when planning the triple store hardware.

## Sizing Factors

The actual hardware requirements depend on several factors, including:

- **Data Model Complexity**: The number of statements and the complexity of the ontology.
- **Workload**: The types of queries (e.g., analytical vs. transactional) and update frequency.
- **Users**: The number of concurrent users and their usage patterns.
- **Hardware**: The specific performance characteristics of the server hardware (CPU, Disk, RAM).

## Sizing Table

| Statements | RAM | Disk Usage |
| ---: | ---: | ---: |
| ~130 M | 8 GB | ~15 GB |
| ~280 M | 16 GB | ~32 GB |
| ~1.100 M | 32 GB | ~110 GB |
| ~2.500 M | 64 GB | ~290 GB |
| ~20.000 M | 128 GB | ~2.000 GB |

## Performance Considerations

When planning your infrastructure, consider the following performance priorities:

- **CPU**: Single-core performance is critical for query execution speed.
- **Disk I/O**: High IOPS and throughput are essential for load and indexing performance. SSDs are strongly recommended.
- **RAM**: While CPU and Disk influence performance, RAM is the mostly limiting factor in terms of the maximum amount of triples that can be loaded and queried efficiently.
