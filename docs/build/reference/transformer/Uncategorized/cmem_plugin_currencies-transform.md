---
title: "Convert currency values"
description: "Converts currencies values with current and historical exchange rates"
icon: octicons/cross-reference-24
tags:
    - TransformOperator
    - PythonPlugin
---

# Convert currency values

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This transform plugin allows you to convert currencies from one currency to another.
It uses the Euro foreign exchange reference rates from the
[European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)
to first convert a currency value to EUR (if needed) and then to another currency.

The plugin contains a data dump which starts with data from 1999-01-04
(and ends the day before it was downloaded) see the
[change log](https://github.com/eccenca/cmem-plugin-currencies/blob/main/CHANGELOG.md)
for more details. It will use the [frankfurter.app](https://www.frankfurter.app/docs/)
API to receive rates from dates which are not part of the data dump.
This API will throw an error for future days and returns data from the last trading
day for dates where it has no data.
The API reference rates are usually updated at around 16:00 CET every working day
(so you get different rates before and after 16:00 CET in case you ask for TODAYs rates).

The plugins can work with up-to 4 inputs:

1. Input: The values which you want to convert.
1. Input: The currency code of your values. If this is not `EUR`,
    the plugin will first convert your value to `EUR`.
1. Input: The date from when you want to use the exchange rate.
1. Input: The target currency code.

For the inputs 2-4, you can define static options as well.
In addition to that, there is a debug switch which outputs more background data than
just the plain values.

Here is an example of the plugin in action:
![cmem-plugin-currencies Example](https://raw.githubusercontent.com/eccenca/cmem-plugin-currencies/main/README.png)

The
[following currency codes](https://github.com/eccenca/cmem-plugin-currencies/blob/cf2ee5332ad5243da8c70ade1ed8f4612f48ba33/cmem_plugin_currencies/eurofxref-hist.csv#L1)
can be used with the plugin.
Please be aware that not all of the rates are available for all dates
(e.g. after 2022-03-01 there is no RUB rate available anymore).

## Parameter

### 1. Source Currency

The currency code you want to convert from (e.g. USD).

- ID: `from_currency`
- Datatype: `string`
- Default Value: `USD`

### 2. Date

Set date (e.g.YYYY-MM-DD) to convert currencies based on historic rates.

- ID: `date`
- Datatype: `string`
- Default Value: `2025-11-26`

### 3. Target Currency

Enter the currency code you want to convert to (e.g.USD).

- ID: `to_currency`
- Datatype: `string`
- Default Value: `EUR`

## Advanced Parameter

### Debug Output

Instead of plain values, output additional background information.

- ID: `debug`
- Datatype: `boolean`
- Default Value: `false`
