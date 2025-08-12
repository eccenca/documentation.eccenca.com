---
title: "Substring comparison"
description: "Return 0 to 1 for strong similarity to weak similarity. Based on the paper: Stoilos, Giorgos, Giorgos Stamou, and Stefanos Kollias. "A string metric for ontology alignment." The Semantic Web-ISWC 2005. Springer Berlin Heidelberg, 2005. 624-637."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Substring comparison
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->




### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Parameter

### Granularity

The minimum length of a possible substring match.

- Datatype: `string`
- Default Value: `3`



