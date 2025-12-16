---
title: "Parse date"
description: "Parses and normalizes dates in different formats."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Parse date
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Parses and normalizes dates in different formats.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * inputDateFormatId: `German style date format`
    * outputDateFormatId: `w3c Date`

* Input values:
    1. `[20.03.1999]`

* Returns: `[1999-03-20]`

---
**Example 2:**

* Parameters
    * inputDateFormatId: `w3c Date`
    * outputDateFormatId: `German style date format`

* Input values:
    1. `[1999-03-20]`

* Returns: `[20.03.1999]`

---
**Example 3:**

* Parameters
    * inputDateFormatId: `common ISO8601`
    * outputDateFormatId: `w3c Date`

* Input values:
    1. `[2017-04-04T00:00:00.000+02:00]`

* Returns: `[2017-04-04]`

---
**Example 4:**

* Parameters
    * inputDateFormatId: `common ISO8601`
    * outputDateFormatId: `w3c Date`

* Input values:
    1. `[2017-04-04T00:00:00+02:00]`

* Returns: `[2017-04-04]`

---
**Example 5:**

* Parameters
    * inputDateFormatId: `common ISO8601`
    * outputDateFormatId: `dateTime with month abbr. (US)`

* Input values:
    1. `[2021-06-24T14:50:05.895+02:00]`

* Returns: `[24-Jun-2021 14:50:05 +02:00]`

---
**Example 6:**

* Parameters
    * inputDateFormatId: `dateTime with month abbr. (US)`
    * outputDateFormatId: `dateTime with month abbr. (DE)`

* Input values:
    1. `[24-Dec-2021 14:50:05 +02:00]`

* Returns: `[24-Dez.-2021 14:50:05 +02:00]`

---
**Example 7:**

* Parameters
    * alternativeInputFormat: `dd.MM.yyyy HH:mm.ss`
    * alternativeOutputFormat: `yyyy-MM-dd'T'HH:mm.ss`

* Input values:
    1. `[20.03.1999 20:34.44]`

* Returns: `[1999-03-20T20:34.44]`

---
**Example 8:**

* Parameters
    * inputDateFormatId: `excelDateTime`
    * outputDateFormatId: `xsdTime`

* Input values:
    1. `[12:20:00.000]`

* Returns: `[12:20:00.000]`

---
**Example 9:**

* Parameters
    * inputDateFormatId: `w3c YearMonth`
    * outputDateFormatId: `w3c Month`

* Input values:
    1. `[2020-01]`

* Returns: `[--01]`

---
**Example 10:**

* Parameters
    * inputDateFormatId: `w3c MonthDay`
    * outputDateFormatId: `w3c Day`

* Input values:
    1. `[--12-31]`

* Returns: `[---31]`

---
**Example 11:**

* Parameters
    * inputDateFormatId: `w3c Date`
    * outputDateFormatId: `w3c MonthDay`

* Input values:
    1. `[2020-12-31]`

* Returns: `[--12-31]`

---
**Example 12:**

* Parameters
    * inputDateFormatId: `w3c MonthDay`
    * outputDateFormatId: `w3c Date`

* Input values:
    1. `[--12-31]`

* Returns: `[]`
* **Throws error:** `DateTimeException`

---
**Example 13:**

* Parameters
    * alternativeInputFormat: `yyyy-MM-dd HH:mm:ss.SSS`
    * outputDateFormatId: `w3cDateTime`

* Input values:
    1. `[2020-02-22 16:34:14.000]`

* Returns: `[2020-02-22T16:34:14]`

---
**Example 14:**

* Parameters
    * inputDateFormatId: `dateTime with month abbr. (DE)`
    * outputDateFormatId: `dateTime with month abbr. (US)`
    * inputLocale: `en_US`
    * outputLocale: `de`

* Input values:
    1. `[24-Dec-2021 14:50:05 +02:00]`

* Returns: `[24-Dez.-2021 14:50:05 +02:00]`

---
**Example 15:**

* Parameters
    * inputDateFormatId: `dateTime with month abbr. (US)`
    * outputDateFormatId: `dateTime with month abbr. (DE)`
    * inputLocale: `de`
    * outputLocale: `en`

* Input values:
    1. `[24-Dez.-2021 14:50:05 +02:00]`

* Returns: `[24-Dec-2021 14:50:05 +02:00]`

---
**Example 16:**

* Parameters
    * outputLocale: `fr`
    * alternativeInputFormat: `MMM yyyy`
    * outputDateFormatId: `dateTime with month abbr. (DE)`
    * inputLocale: `de`
    * alternativeOutputFormat: `MMM uuuu`
    * inputDateFormatId: `dateTime with month abbr. (US)`

* Input values:
    1. `[Dez. 2021]`

* Returns: `[déc. 2021]`

---
**Example 17:**

* Parameters
    * alternativeInputFormat: `MMMM, uuuu`
    * alternativeOutputFormat: `MMMM, uuuu`
    * inputLocale: `en_US`
    * outputLocale: `de`

* Input values:
    1. `[February, 2024]`

* Returns: `[Februar, 2024]`

## Parameter

### Input format

The input date/time format used for parsing the date/time string.

* ID: `inputDateFormatId`
* Datatype: `option[enumeration]`
* Default Value: `w3c Date`

### Alternative input format

An input format string that should be used instead of the selected input format. Java DateFormat string.

* ID: `alternativeInputFormat`
* Datatype: `string`
* Default Value: `None`

### Alternative input locale

Optional locale for the (alternative) input format. If not set the system's locale will be used or the locale of the input format, if set.

* ID: `inputLocale`
* Datatype: `option[locale]`
* Default Value: `None`

### Output format

The output date/time format used for parsing the date/time string.

* ID: `outputDateFormatId`
* Datatype: `option[enumeration]`
* Default Value: `w3c Date`

### Alternative output format

An output format string that should be used instead of the selected output format. Java DateFormat string.

* ID: `alternativeOutputFormat`
* Datatype: `string`
* Default Value: `None`

### Alternative output locale

Optional locale for the (alternative) output format. If not set the system's locale will be used or the locale of the output format, if set.

* ID: `outputLocale`
* Datatype: `option[locale]`
* Default Value: `None`

## Advanced Parameter

`None`
