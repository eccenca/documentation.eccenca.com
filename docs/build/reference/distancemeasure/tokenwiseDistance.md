---
title: "Token-wise distance"
description: "Token-wise string distance using the specified metric."
icon: octicons/cross-reference-24
tags:
    - DistanceMeasure
---

# Token-wise distance

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Token-wise string distance using the specified metric.

## Characteristics

This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Parameter

### Ignore case

No description

- ID: `ignoreCase`
- Datatype: `boolean`
- Default Value: `true`

### Metric name

No description

- ID: `metricName`
- Datatype: `string`
- Default Value: `levenshtein`

### Split regex

No description

- ID: `splitRegex`
- Datatype: `string`
- Default Value: `[\s\d\p{Punct}]+`

### Stopwords

No description

- ID: `stopwords`
- Datatype: `string`
- Default Value: `None`

### Match threshold

No description

- ID: `matchThreshold`
- Datatype: `double`
- Default Value: `0.0`

### Ordering impact

No description

- ID: `orderingImpact`
- Datatype: `double`
- Default Value: `0.0`

### Adjust by token length

No description

- ID: `adjustByTokenLength`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### Stopword weight

Weight assigned to stopwords

- ID: `stopwordWeight`
- Datatype: `double`
- Default Value: `0.01`

### Non stopword weight

Weight assigned to non-stopwords

- ID: `nonStopwordWeight`
- Datatype: `double`
- Default Value: `0.1`

### Use incremental idf weights

Use incremental IDF weights

- ID: `useIncrementalIdfWeights`
- Datatype: `boolean`
- Default Value: `false`

