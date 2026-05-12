---
title: "Compare numbers"
description: "Compares the numbers of two sets. Returns 1 if the comparison yields true and 0 otherwise. If there are multiple numbers in both sets, the comparator must be true for all numbers. For instance, {1,2} < {2,3} yields 0 as not all numbers in the first set are smaller than in the second."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Compare numbers

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Compares the numbers of two sets.
Returns 1 if the comparison yields true and 0 otherwise.
If there are multiple numbers in both sets, the comparator must be true for all numbers.
For instance, {1,2} < {2,3} yields 0 as not all numbers in the first set are smaller than in the second.


## Parameter

### Comparator

No description

- ID: `comparator`
- Datatype: `enumeration`
- Default Value: `<`

## Advanced Parameter

`None`

## Related Plugins

- **compareDates** — Compare numbers and Compare dates both return 1 or 0 by applying the same ordering and equality comparators across two input sets. Compare dates is not a date-aware extension of Compare numbers — each plugin accepts only its own value type, doubles for one and XSD date literals for the other.
