---
title: "Normalize chars"
description: "Replaces diacritical characters with non-diacritical ones (eg, ö -> o), plus some specialities like transforming æ -> ae, ß -> ss."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Normalize chars

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Replaces diacritical characters with non-diacritical ones (eg, ö -> o), plus some specialities like transforming æ -> ae, ß -> ss.


## Parameter

`None`

## Advanced Parameter

`None`

## Related Plugins

- **removeSpecialChars** — After Normalize chars, a string still contains its original punctuation, spaces, and symbols. Remove special chars removes all of those, keeping only letters, digits, and underscores.
- **alphaReduce** — Normalize chars is a substitution-only plugin: it converts diacritics but does not remove anything. Strip non-alphabetic characters is a removal-only plugin: it strips digits and punctuation while keeping letters and spaces, but leaves diacritical letters in their original form.
