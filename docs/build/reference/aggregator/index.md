---
title: "Aggregators"
icon: octicons/cross-reference-24
tags:
    - Build
    - Reference
---
# Aggregators
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

This kind of task aggregates multiple similarity scores.

**:octicons-people-24: Intended audience:** Linked Data Experts and Domain Experts

|                                                    Name |                                                Category                                                 | Description              |
|--------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|:-------------------------|
 | [And](min.md) | None | All input scores must be within the threshold. Selects the minimum score. |
 | [Average](average.md) | None | Computes the weighted average. |
 | [Euclidian distance](quadraticMean.md) | None | Calculates the Euclidian distance. |
 | [First non-empty score](firstNonEmpty.md) | None | Forwards the first input that provides a non-empty similarity score. |
 | [Geometric mean](geometricMean.md) | None | Compute the (weighted) geometric mean. |
 | [Handle missing values](handleMissingValues.md) | None | Generates a default similarity score, if no similarity score is provided (e.g., due to missing values). Using this operator can have a performance impact, since it lowers the efficiency of the underlying computation. |
 | [Negate](negate.md) | None | Negates the result of the input comparison. A single input is expected. Using this operator can have a performance impact, since it lowers the efficiency of the underlying computation. |
 | [Or](max.md) | None | At least one input score must be within the threshold. Selects the maximum score. |
 | [Scale](scale.md) | None | Scales a similarity score by a factor. |
