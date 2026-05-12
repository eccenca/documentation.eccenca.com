---
title: "Number to duration"
description: "Converts a number to an xsd:duration."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Number to duration

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Converts a number to an xsd:duration.


## Parameter

### Unit

No description

- ID: `unit`
- Datatype: `enumeration`
- Default Value: `day`

## Advanced Parameter

`None`

## Related Plugins

- **durationInDays** — Number to duration and Duration in days form a round-trip: one builds a duration from days, the other extracts days from a duration.
- **durationInSeconds** — Duration in seconds produces the finest-grained numeric output among the duration converters. Number to duration is its reverse when configured for seconds: it constructs a duration from a second count.
- **durationInYears** — Duration in years extracts a year count from a duration value. Number to duration reconstructs the duration from that count.
- **duration** — The two plugins produce durations by different means. Duration measures the gap between a start and an end date; Number to duration builds one from a time span expressed as a number.
