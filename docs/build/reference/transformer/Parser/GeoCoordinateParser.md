---
title: "Parse geo coordinate"
description: "Parses and normalizes geo coordinates."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Parse geo coordinate

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Description of the plugin

This plugin parses and normalizes geographic coordinates.

The input is a **geographic coordinate** (or "geocoordinate") expressed as a _single text string_, and the output is the normalization of the geographic coordinate, consisting of both **latitude** and **longitude**, in the form `(latitude, longitude)`. For this to work, the input must contain a **separating comma** (`,`) between the latitude and the longitude. Otherwise, the coordinates (0, 0) are returned by convention, instead of throwing an error.

### Geographic coordinate system

The term "geocoordinates" is a shortened form of "geographic coordinates", specifically used in technical contexts such as ours. Both —"geocoordinates" and "geographic coordinates"— are synonyms that refer to a **location on Earth**, expressed by the (angular) coordinates of **latitude** (north/south) and **longitude** (east/west).

The origin of this coordinate system is known as the [Null Island](https://en.wikipedia.org/wiki/Null_Island). The positive direction of _latitude_ is —by definition— the cardinal direction **north**, whereas the positive direction of _longitude_ is **east**. Lines of constant longitude are known as **meridians**, whereas lines of constant latitude are known as **parallels** or **circles of latitude**. The meridian with 0° longitude is known  —informally— as the **prime meridian**, and —formally— as the **IERS Reference Meridian (IRM)**, or **International Reference Meridian**. The acronym "IERS" stands for "International Earth Rotation and Reference Systems Service". The parallel with 0° latitude is the **equator**.

Geographic coordinates are dimensionless numbers for measuring and expressing **angles**. By convention, these angles are expressed in **degrees**, not in radians. This means, for the range of values for **latitude** and **longitude**, the following:

* **Latitude (φ):** range **–90° ≤ φ ≤ +90°**
    * **–90°** → South Pole
    * **0°** → Equator
    * **+90°** → North Pole

* **Longitude (λ):** range **–180° ≤ λ ≤ +180°**
    * **0°** → Prime Meridian (Greenwich)
    * **+180°** → directly east of Greenwich (International Date Line eastward)
    * **–180°** → directly west of Greenwich (International Date Line westward)

The meridian at 180° is known as the **antimeridian** or, simply, the **180th meridian**.

### Normalization of geographic coordinates

**Normalization** converts varied geolocation formats into a **standard numeric form** in decimal degrees: (latitude, longitude).

The input is expressed in degrees-minutes-seconds (DMS). Each portion is accompanied by the corresponding symbol:

* **Degrees (°)**
* **Minutes (′)**
* **Seconds (″)**

#### Example

An example of the normalization of the geographic coordinates `"51°20.519' N,12°22.443' E"` is `(51.3419833, 12.37405)`. This stems from the following calculation:

    Latitude = 51 + 1⁄60 · 20.519 = 51.3419833° N,
    Longitude = 12 + 1⁄60 · 22.443 = 12.37405° E.

A bit more detailed:

1. First, the input is _parsed_: The **latitude** is `51°20.519' N`, the **longitude** is `51°20.519' N`. As stated, **north** (`N`) and **east** (`E`) are _positive_ by convention. Correspondingly, **south** (`S`) and **west** (`w`) are _negative_.
2. Next, _each_ of these **components** is split into their **portions**:
    * `51°20.519' N` corresponds to 51 degrees and 20.519 minutes.
        * Notice that the portion **`20.519` minutes** contains, itself, a _decimal_ number, instead of the degrees-**minutes-seconds** format. This is because decimal degrees and minutes are permitted as a form of mixed format by our plugin.
        * Fully written in DMS format, this would be `51°20'31.14''N`. This comes from the conversion of the fractional part: 0.519' · 60 = 31.14''.
    * `12°22.443' E` corresponds to 12 degrees, 22.443 minutes.
        * Once more, the portion `22.443 minutes` is a mixed format, where instead of minutes and seconds, we write the minutes in decimal format to include the seconds.
3. Finally, the DMS format of the input is **normalized** according to the following conversion formula:
   decimal degrees = _degrees_ + 1⁄60 · minutes + 1⁄3600 · seconds.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[51°20.519' N, 12°22.443' E]`

* Returns: `[GeoCoordinate(51.34198333333333,12.37405)]`


---
**Example 2:**

* Input values:
    1. `[51°20'31.14'' N, 12°22'26.58'' E]`

* Returns: `[GeoCoordinate(51.34198333333334,12.37405)]`


---
**Example 3:**

* Input values:
    1. `[0°0'0'' N, 0°0'0'' E]`

* Returns: `[GeoCoordinate(0.0,0.0)]`


---
**Example 4:**

* Input values:
    1. `[47° 45' 3.8736'' N, 120° 44' 24.4860'' W]`

* Returns: `[GeoCoordinate(47.751076,-120.740135)]`


---
**Example 5:**

* Input values:
    1. `[35° 39' 10.1952'' N, 139° 50' 22.1208'' E]`

* Returns: `[GeoCoordinate(35.652832,139.839478)]`




## Parameter

`None`

## Advanced Parameter

`None`
