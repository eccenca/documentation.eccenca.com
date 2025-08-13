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

|         Name | Description              |
|-------------:|:-------------------------|
 | [And](min.md) | All input scores must be within the threshold. Selects the minimum score. |
 | [Average](average.md) | Computes the weighted average. |
 | [Euclidian distance](quadraticMean.md) | Calculates the Euclidian distance. |
 | [First non-empty score](firstNonEmpty.md) | Forwards the first input that provides a non-empty similarity score. |
 | [Geometric mean](geometricMean.md) | Compute the (weighted) geometric mean. |
 | [Handle missing values](handleMissingValues.md) | Generates a default similarity score, if no similarity score is provided (e.g., due to missing values). Using this operator can have a performance impact, since it lowers the efficiency of the underlying computation. |
 | [Negate](negate.md) | Negates the result of the input comparison. A single input is expected. Using this operator can have a performance impact, since it lowers the efficiency of the underlying computation. |
 | [Or](max.md) | At least one input score must be within the threshold. Selects the maximum score. |
 | [Scale](scale.md) | Scales a similarity score by a factor. |
