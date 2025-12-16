---
title: "Compare physical quantities"
description: "Computes the distance between two physical quantities."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Compare physical quantities
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Computes the distance between two physical quantities.
This "distance" is to be understood in a mathematical or abstract sense of _absolute difference_.
The distance is normalized to the SI base unit of the dimension.
For instance: for lengths, the distance will be in metres.
Comparing incompatible units will yield a validation error.

## Supported units

### Time

Time is expressed in seconds (symbol: `s`).
The following alternative symbols are supported:

* `mo_s`: day*29.53059
* `mo_g`: year/12.0
* `a`: day*365.25
* `min`: min
* `a_g`: year
* `mo`: (day*365.25)/12.0
* `mo_j`: (day*365.25)/12.0
* `a_j`: day*365.25
* `h`: h
* `a_t`: day*365.24219
* `d`: day

### Length

Length is expressed in metres (symbol: `m`).
The following alternative symbols are supported:

* `in`: c(cm*254.0)
* `nmi`: m*1852.0
* `Ao`: dnm
* `mil`: m(c(cm*254.0))
* `yd`: ((c(cm*254.0))*12.0)*3.0
* `AU`: m*1.49597871E11
* `ft`: (c(cm*254.0))*12.0
* `pc`: m*3.085678E16
* `fth`: ((c(cm*254.0))*12.0)*6.0
* `mi`: ((c(cm*254.0))*12.0)*5280.0
* `hd`: (c(cm*254.0))*4.0

### Mass

Mass is expressed in kilograms (symbol: `kg`).
The following alternative symbols are supported:

* `lb`: lb
* `ston`: hlb*20.0
* `t`: Mg
* `stone`: lb*14.0
* `u`: AMU
* `gr`: (mg*6479891.0)/100000.0
* `lcwt`: lb*112.0
* `oz`: oz
* `g`: g
* `scwt`: hlb
* `dr`: oz/16.0
* `lton`: (lb*112.0)*20.0

### Electric current

Electric current is expressed in amperes (symbol: `A`).
The following alternative symbols are supported:

* `Bi`: daA
* `Gb`: cm·(A/m)*250.0/[one?]

### Temperature

Temperature is expressed in kelvins (symbol: `K`).
The following alternative symbols are supported:

* `Cel`: ℃

### Amount of substance

Amount of substance is expressed in moles (symbol: `mol`).

### Luminous intensity

Luminous intensity is expressed in candelas (symbol: `cd`).

### Area

Area is expressed in square metres (symbol: `m²`).
The following alternative symbols are supported:

* `m2`: m²
* `ar`: hm²
* `syd`: ((c(cm*254.0))*12.0)*3.0²
* `cml`: [one?]/4.0·m(c(cm*254.0))²
* `b`: hfm²
* `sft`: (c(cm*254.0))*12.0²
* `sin`: c(cm*254.0)²

### Volume

Volume is expressed in cubic metres (symbol: `㎥`).
The following alternative symbols are supported:

* `st`: [㎥?]
* `bf`: (c(cm*254.0)³)*144.0
* `cyd`: ((c(cm*254.0))*12.0)*3.0³
* `cr`: ((c(cm*254.0))*12.0³)*128.0
* `L`: L
* `l`: l
* `cin`: c(cm*254.0)³
* `cft`: (c(cm*254.0))*12.0³
* `m3`: ㎥

### Energy

Energy is expressed in joules (symbol: `J`).
The following alternative symbols are supported:

* `cal_IT`: (J*41868.0)/10000.0
* `eV`: J*1.602176487E-19
* `cal_m`: (J*419002.0)/100000.0
* `cal`: m(J*4184.0)
* `cal_th`: m(J*4184.0)

### Angle

Angle is expressed in radians (symbol: `rad`).
The following alternative symbols are supported:

* `circ`: [one?]·rad*2.0
* `gon`: ([one?]·rad/180.0)*0.9
* `deg`: [one?]·rad/180.0
* `'`: ([one?]·rad/180.0)/60.0
* `''`: (([one?]·rad/180.0)/60.0)/60.0

### Others

* `1/m`, derived units: `Ky`: c(1/m)
* `kg/(m·s)`, derived units: `P`: g/(s·cm)
* `bit/s`, derived units: `Bd`: bit/s
* `bit`, derived units: `By`: bit*8.0
* `Sv`
* `N`
* `Ω`, derived units: `Ohm`: Ω
* `T`, derived units: `G`: T/10000.0
* `sr`, derived units: `sph`: [one?]·sr*4.0
* `F`
* `C/kg`, derived units: `R`: (C/kg)*2.58E-4
* `cd/m²`, derived units: `sb`: cd/cm², `Lmb`: cd/([one?]·cm²)
* `Pa`, derived units: `bar`: Pa*100000.0, `atm`: Pa*101325.0
* `kg/(m·s²)`, derived units: `att`: k(g·(m/s²)*9.80665)/cm²
* `m²/s`, derived units: `St`: cm²/s
* `A/m`, derived units: `Oe`: (A/m)*250.0/[one?]
* `kg·m²/s²`, derived units: `erg`: cm²·g/s²
* `kg/m³`, derived units: `g%`: g/dl
* `mho`
* `V`
* `lx`, derived units: `ph`: lx/10000.0
* `m/s²`, derived units: `Gal`: cm/s², `m/s2`: m/s²
* `m/s`, derived units: `kn`: m*1852.0/h
* `m·kg/s²`, derived units: `gf`: g·(m/s²)*9.80665, `lbf`: lb·(m/s²)*9.80665, `dyn`: cm·g/s²
* `m²/s²`, derived units: `RAD`: cm²·g/(s²·hg), `REM`: cm²·g/(s²·hg)
* `C`
* `Gy`
* `Hz`
* `H`
* `lm`
* `W`
* `Wb`, derived units: `Mx`: Wb/1.0E8
* `Bq`, derived units: `Ci`: Bq*3.7E10
* `S`

## Characteristics

This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Convert SI unit prefixes:**

* Input values:
    * Source: `[1 km]`
    * Target: `[500 m]`

* Returns: `500.0`

---
**Convert imperial and metric values:**

* Input values:
    * Source: `[1 km]`
    * Target: `[1 mi]`

* Returns: `609.344`

---
**Validate if the compared units of measurement are compatible:**

* Input values:
    * Source: `[1 km]`
    * Target: `[1 kg]`

* Returns: `NaN`
* **Throws error:** `ValidationException`

## Parameter

### Number format

The IETF BCP 47 language tag, e.g., 'en'.

* ID: `numberFormat`
* Datatype: `string`
* Default Value: `en`

## Advanced Parameter

`None`
