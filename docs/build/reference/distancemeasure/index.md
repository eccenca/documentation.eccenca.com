---
title: "Distance Measures"
icon: octicons/cross-reference-24
tags:
    - Build
    - Reference
---
# Distance Measures
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Distance Measures compute a distance metric between two sets of strings.

**:octicons-people-24: Intended audience:** Linked Data Experts and Domain Experts

|                                                    Name |                                                Category                                                 | Description              |
|--------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|:-------------------------|
 | [CJK reading distance](cjkReadingDistance.md) | None | CJK Reading Distance. |
 | [Compare physical quantities](PhysicalQuantitiesDistance.md) | None | Computes the distance between two physical quantities. The distance is normalized to the SI base unit of the dimension. For instance for lengths, the distance will be in metres. Comparing incompatible units will yield a validation error. |
 | [Constant similarity value](constantDistance.md) | None | Always returns a constant similarity value. |
 | [Cosine](cosine.md) | None | Cosine Distance Measure. |
 | [Date](date.md) | None | The distance in days between two dates ('YYYY-MM-DD' format). |
 | [DateTime](dateTime.md) | None | Distance between two date time values (xsd:dateTime format) in seconds. |
 | [Dice coefficient](dice.md) | None | Dice similarity coefficient. |
 | [Geographical distance](wgs84.md) | None | Computes the geographical distance between two points. Author: Konrad Höffner (MOLE subgroup of Research Group AKSW, University of Leipzig) |
 | [Greater than](greaterThan.md) | None | Checks if the source value is greater than the target value. If both strings are numbers, numerical order is used for comparison. Otherwise, alphanumerical order is used. |
 | [Inequality](inequality.md) | None | Returns success if values are not equal, failure otherwise. |
 | [Inside numeric interval](insideNumericInterval.md) | None | Checks if a number is contained inside a numeric interval, such as '1900 - 2000'. |
 | [Is substring](isSubstring.md) | None | Checks if a source value is a substring of a target value. |
 | [Jaccard](jaccard.md) | None | Jaccard similarity coefficient. Divides the matching tokens by the number of distinct tokens from both inputs. |
 | [Jaro distance](jaro.md) | None | Matches strings based on the Jaro distance metric. |
 | [Jaro-Winkler distance](jaroWinkler.md) | None | Matches strings based on the Jaro-Winkler distance measure. |
 | [Korean phoneme distance](koreanPhonemeDistance.md) | None | Korean phoneme distance. |
 | [Korean translit distance](koreanTranslitDistance.md) | None | Transliterated Korean distance. |
 | [Levenshtein distance](levenshteinDistance.md) | None | Levenshtein distance. Returns a distance value between zero and the size of the string. |
 | [Lower than](lowerThan.md) | None | Checks if the source value is lower than the target value. |
 | [Normalized Levenshtein distance](levenshtein.md) | None | Normalized Levenshtein distance. Divides the edit distance by the length of the longer string. |
 | [Numeric equality](numericEquality.md) | None | Compares values numerically instead of their string representation as the 'String Equality' operator does. Allows to set the needed precision of the comparison. A value of 0.0 means that the values must represent exactly the same (floating point) value, values higher than that allow for a margin of tolerance. |
 | [Numeric similarity](num.md) | None | Computes the numeric distance between two numbers. |
 | [qGrams](qGrams.md) | None | String similarity based on q-grams (by default q=2). |
 | [Relaxed equality](relaxedEquality.md) | None | Return success if strings are equal, failure otherwise. Lower/upper case and differences like ö/o, n/ñ, c/ç etc. are treated as equal. |
 | [Soft Jaccard](softjaccard.md) | None | Soft Jaccard similarity coefficient. Same as Jaccard distance but values within an levenhstein distance of 'maxDistance' are considered equivalent. |
 | [Starts with](startsWith.md) | None | Returns success if the first string starts with the second string, failure otherwise. |
 | [String equality](equality.md) | None | Checks for equality of the string representation of the given values. Returns success if string values are equal, failure otherwise. For a numeric comparison of values use the 'Numeric Equality' comparator. |
 | [Substring comparison](substringDistance.md) | None | Return 0 to 1 for strong similarity to weak similarity. Based on the paper: Stoilos, Giorgos, Giorgos Stamou, and Stefanos Kollias. "A string metric for ontology alignment." The Semantic Web-ISWC 2005. Springer Berlin Heidelberg, 2005. 624-637. |
 | [Token-wise distance](tokenwiseDistance.md) | None | Token-wise string distance using the specified metric. |
