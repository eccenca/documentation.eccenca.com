---
title: "Parse geo location"
description: "Parses and normalizes geo locations like continents, countries, states and cities."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Parse geo location

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## What does this plugin do?

This plugin **parses and normalizes geolocations**.

### What is Geolocation?

The term "geolocation" means two things. Usually, it is used primarily as a noun referring to the **process** or technique of _determining the physical location_ of a person or an item, e.g. by means of GPS or IP addresses. On the other hand – and this is the meaning of the word that _we_'ll use – it is also used to describe the _actual location_ that is identified.

In short: For our purposes, the term "geolocation" won't be the act of _geoloca**ting**_, but the _outcome_ of this act: the _geoloca**tion**_, the physical or actual _location_.

This plugin takes thus a given geolocation and normalizes it into a standard-conforming geolocation. This is the same principle as in the parsing and normalization of _geocoordinates_, but with the difference that, now, the input isn't numerical, but textual. A geolocation is, in our case, one of the following input possibilities: A **continent**, a **country**, a **state** or a **city**.

## How does this plugin work?

This plugin uses lookup-tables as a mechanism for parsing and normalizing geolocations. Rather than converting the input via a prescribed formula, as in the case of geocoordinates, a tabular dataset provides the standard output for the given input. Which tabular dataset is used, depends on the parameter values.

### Parameter values

The parameter `parseTypeId` tells the plugin which parser to use, as well as which normalization logic to apply to the parsed result.
The `parseTypeId` must be one of the following:

* `continent`
* `country`
* `numericCountry`
* `state`
* `city`

#### Description of parameter values

##### Continent

The `continent` parameter refers to a _continent code_. Although these contintnet codes are not standardized, the de-facto standard is the following table:

| Continent     | Code | Notes                                                             |
| ------------- | ---- | ----------------------------------------------------------------- |
| Africa        | AF   | [Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) style |
| Antarctica    | AN   |                                                                   |
| Asia          | AS   |                                                                   |
| Europe        | EU   |                                                                   |
| North America | NA   |                                                                   |
| Oceania       | OC   | We don't use the alternative `UA`                                 |
| South America | SA   |                                                                   |

##### Country and Numeric Country

Both `country` and `numericCountry` refer to the [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country code, such as `AND` for Andorra, as can be found in the list of [officially assigned ISO 3166-1 alpha-3 codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Officially_assigned_code_elements).

##### State

For the `state` parse type ID, the behavior of the plugin depends on the value of the second parameter, `fullStateName`. This parameter controls whether the plugin returns the _state name_ (if set to `true`) or the _state code_.

The underlying lookup table is the **[GeoNames](https://www.geonames.org/) database**, a widely used geospatial dataset. Specifically, the plugin uses its **country-specific dump**. In this dataset, each row represents a _geographical feature_: a city, village, administrative region, mountain, river, etc.

For concreteness, an exemplary row in this dataset is the following:

```tsv
3039162 Sant Julià de Lòria    Sant Julia de Loria    Parochia de Sant Julia de Loria,Parochia de Sant Julià de Lòria,Parroquia de Sant Julia de Loria,Parroquia de Sant Julià de Lòria,San Dzhulija de Lorija,San Julian de Loria,San Julián de Loria,San Zhulija de Lorija,San-Zhulia-de-Lorija,Sant Chulija de Lorija,Sant Julia de Loria,Sant Julia de Loria koezoesseg,Sant Julià de Loria,Sant Julià de Lòria,Sant Julià de Lòria közösség,Sant Zhulija de Lorija,Sant-Zhulija-de-Lorija,sanjulliadelolia,sant jwlya dr lwrya,sant jwlya dy lwrya,santa juliya di loriya palli,sheng hu li ya-de luo li ya,sn gwlyh dh lwryh,snt hwlya dh lwrya,Сан Джулия де Лория,Сан Жулија де Лорија,Сан-Жулиа-де-Лория,Сант Жулија де Лорија,Сант-Жулія-де-Лорія,Սանթ Ժուլիա դե Լորիա,סן גוליה דה לוריה,سانت جوليا دي لوريا,سانت جولیا در لوریا,سنت حولیا ده لوریا,संत जूलिया डी लोरिया पल्ली,სანტ-ჟულია-დე-ლორია,サン・ジュリア・デ・ロリア教区,圣胡利娅-德洛里亚,산줄리아데로리아  42.46247   1.48247    A  ADM1   AD    06          9448      1143   Europe/Andorra 2014-07-30
```

Each row in the dataset, such as the previous one, contains the following information:

| Column            | Description                                                    | Example (Sant Julià de Lòria, Andorra)                                                                |
| ----------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| geonameid         | Unique identifier in the GeoNames database                     | 3039162                                                                                               |
| name              | Official name of the feature                                   | Sant Julià de Lòria                                                                                   |
| asciiname         | ASCII-only version of the name                                 | Sant Julia de Loria                                                                                   |
| alternatenames    | Comma-separated list of alternate names in different languages | Parochia de Sant Julia de Loria, Parochia de Sant Julià de Lòria, Parroquia de Sant Julia de Loria, … |
| latitude          | Latitude coordinate                                            | 42.46247                                                                                              |
| longitude         | Longitude coordinate                                           | 1.48247                                                                                               |
| feature class     | Broad type of feature                                          | A                                                                                                     |
| feature code      | More detailed classification                                   | ADM1                                                                                                  |
| country code      | ISO 3166-1 alpha-2 country code                                | AD                                                                                                    |
| cc2               | Secondary country codes                                        | (empty)                                                                                               |
| admin1 code       | First-level subdivision code                                   | 06                                                                                                    |
| admin2 code       | Second-level subdivision code                                  | (empty)                                                                                               |
| admin3 code       | Third-level subdivision                                        | (empty)                                                                                               |
| admin4 code       | Fourth-level subdivision                                       | (empty)                                                                                               |
| population        | Population of the feature                                      | 9448                                                                                                  |
| elevation         | Elevation in meters                                            | (empty)                                                                                               |
| dem               | Digital elevation model value                                  | 1143                                                                                                  |
| timezone          | IANA timezone ID                                               | Europe/Andorra                                                                                        |
| modification date | Date of last update in GeoNames                                | 2014-07-30                                                                                            |

In our case, the _state code_ corresponds to the `admin1` code of the GeoNames country-specific dataset (11th column), whereas the `name` corresponds to the `name` column (2nd column).

##### City

As a last level of geospatial precision, we have the `city`. Currently, this does nothing, really. The plugin returns the same input as output.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * parseTypeId: `continent`

* Input values:
    1. `[Africa]`

* Returns: `[AF]`


---
**Example 2:**

* Parameters
    * parseTypeId: `continent`

* Input values:
    1. `[Europe]`

* Returns: `[EU]`


---
**Example 3:**

* Parameters
    * parseTypeId: `continent`

* Input values:
    1. `[Oceania]`

* Returns: `[OC]`


---
**Example 4:**

* Parameters
    * parseTypeId: `continent`

* Input values:
    1. `[AF]`

* Returns: `[AF]`


---
**Example 5:**

* Parameters
    * parseTypeId: `continent`

* Input values:
    1. `[EU]`

* Returns: `[EU]`


---
**Example 6:**

* Parameters
    * parseTypeId: `continent`

* Input values:
    1. `[OC]`

* Returns: `[OC]`


---
**Example 7:**

* Parameters
    * parseTypeId: `country`

* Input values:
    1. `[Andorra, AND]`

* Returns: `[AND, AND]`


---
**Example 8:**

* Parameters
    * parseTypeId: `country`

* Input values:
    1. `[Germany, DEU]`

* Returns: `[DEU, DEU]`


---
**Example 9:**

* Parameters
    * parseTypeId: `country`

* Input values:
    1. `[United States of America]`

* Returns: `[United States of America]`


---
**Example 10:**

* Parameters
    * parseTypeId: `country`

* Input values:
    1. `[USA]`

* Returns: `[USA]`


---
**Example 11:**

* Parameters
    * parseTypeId: `state`
    * fullStateName: `false`

* Input values:
    1. `[Sant Julià de Lòria]`

* Returns: `[06]`


---
**Example 12:**

* Parameters
    * parseTypeId: `state`
    * fullStateName: `true`

* Input values:
    1. `[Sant Julià de Lòria]`

* Returns: `[Sant Julià de Lòria]`


---
**Example 13:**

* Parameters
    * parseTypeId: `state`
    * fullStateName: `false`

* Input values:
    1. `[nonExistentStateHere, asdf]`

* Returns: `[nonExistentStateHere, asdf]`


---
**Example 14:**

* Parameters
    * parseTypeId: `city`

* Input values:
    1. `[Leipzig, London, Paris, Barcelona]`

* Returns: `[Leipzig, London, Paris, Barcelona]`




## Parameter

### Parse type id

What type of location should be parsed.

* ID: `parseTypeId`
* Datatype: `enumeration`
* Default Value: `None`



### Full state name

Set to true if the full state name should be output instead of the 2-letter code.

* ID: `fullStateName`
* Datatype: `boolean`
* Default Value: `true`





## Advanced Parameter

`None`
