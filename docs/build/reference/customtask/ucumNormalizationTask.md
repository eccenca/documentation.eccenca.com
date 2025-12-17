---
title: "Normalize units of measurement"
description: "Custom task that will substitute numeric values and pertaining unit symbols with a SI-system-unit normalized representation."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Normalize units of measurement

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

This custom task substitutes numeric values and pertaining units by its normalized representation in the International System of Units (SI).

The resulting representation consists of the following three columns:

1. The normalized numeric value.
2. The unit symbol of the International System of Units (SI) pertaining to the value.
3. The original unit symbol, from which it was normalized. This information is kept to be able to reverse this action.

## Parameter

### Value properties

The names (comma-separated) of columns containing numeric values interpreted as quantities of the dimension indicated by the pertaining unit.

- ID: `valueProperties`
- Datatype: `string`
- Default Value: `None`

### Unit property

The names (comma-separated) of dedicated columns containing the unit symbol for the pertaining value in the value column (the positions in this list have to align with the pertaining value columns). Either this param or 'static unit' has to be set.

- ID: `unitProperties`
- Datatype: `string`
- Default Value: `None`

### Static units

Unit symbols (comma-separated) defining the unit for all values in the pertaining value column. If set, the 'unitProperty' param will be ignored and all values of the value column have to be numbers without unit symbols (the positions in this list have to align with the pertaining value columns).

- ID: `staticUnits`
- Datatype: `string`
- Default Value: `None`

### Target units

Unit symbols (comma-separated) defining the target unit to which the value column will be converted (Note: Make sure the input unit can be converted to the target unit). By default the pertaining SI-base unit will be used as normalization unit (the positions in this list have to align with the pertaining value columns)

- ID: `targetUnits`
- Datatype: `string`
- Default Value: `None`

### Suppress errors

If true, will ignore any parsing or value conversion error and return an empty result (might happen because of unknown unit symbols or non-numbers as values). Beware, the value will be lost completely!

- ID: `suppressErrors`
- Datatype: `boolean`
- Default Value: `false`

### Configuration file path

An absolute file path for a unit CSV configuration file (for syntax see 'configuration' param). If set, the 'configuration' param will be ignored.

- ID: `configFilePath`
- Datatype: `resource`
- Default Value: `None`

### Configuration

While all SI units and decimal prefixes are supported by default, custom or obsolete units have to be added via this configuration. NOTE: when constructing formulae depending on other units defined in the configuration, make sure to order them dependently. ALSO: Rational numbers are not supported by the UCUM syntax, express them as a fraction (see 'grain' example below).

- ID: `configuration`
- Datatype: `multiline string`
- Default Value:

``` text

# Example configuration, don't forget to remove the '#' in front of each row.
#      CSV COLUMNS:
#       * unit name - the human readable name of the unit
#       * override  - (true|false) if true, any assigned unit to the given symbol will be dropped, else if the unit symbol is already in use, the new definition will be ignored
#       * symbol    - the main symbol used to depict the unit
#       * equals formula - the formula to derive the given unit from already registered units
#       * [all additional columns] - alternative symbols, will be registered for this unit
# Example CSV:
#      unit name, override, symbol, equals formula
#       Are     , true    , are   , 100.m2
#       Denier  , true    , den   , g/(9.km)
#       Grain   , true    , gr    , (45.g)/100
#       Pound   , true    , lb    , (45359237.kg)/100000000 , # , lbm

```

## Advanced Parameter

`None`
