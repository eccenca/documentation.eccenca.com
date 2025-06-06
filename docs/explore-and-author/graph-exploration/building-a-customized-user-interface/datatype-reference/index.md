---
icon: octicons/cross-reference-24
tags:
    - Reference
    - Vocabulary
---
# Datatypes
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

This is a list of supported data types in shapes.

!!! warning

    Not all datatypes result in specific widgets.


#### anyURI


The ·lexical space· of anyURI is finite-length character sequences which, when the algorithm defined in Section 5.4 of [XML Linking Language] is applied to them, result in strings which are legal URIs according to [RFC 2396], as amended by [RFC 2732]. Note:  Spaces are, in principle, allowed in the ·lexical space· of anyURI, however, their use is highly discouraged (unless they are encoded by %20).

IRI: `http://www.w3.org/2001/XMLSchema#anyURI`

#### base64Binary


The lexical forms of base64Binary values are limited to the 65 characters of the Base64 Alphabet defined in [RFC 2045], i.e., a-z, A-Z, 0-9, the plus sign (+), the forward slash (/) and the equal sign (=), together with the characters defined in [XML 1.0 (Second Edition)] as white space. No other characters are allowed.

IRI: `http://www.w3.org/2001/XMLSchema#base64Binary`

#### boolean


An instance of a datatype that is defined as ·boolean· can have the following legal literals {true, false, 1, 0}.

IRI: `http://www.w3.org/2001/XMLSchema#boolean`

#### byte


byte is ·derived· from short by setting the value of ·maxInclusive· to be 127 and ·minInclusive· to be -128. byte has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, '+' is assumed. For example: -1, 0, 126, +100.

IRI: `http://www.w3.org/2001/XMLSchema#byte`

#### date


The lexical space of date consists of finite-length sequences of characters of the form: `'-'? yyyy '-' mm '-' dd zzzzzz?` where the date and optional timezone are represented exactly the same way as they are for dateTime. The first moment of the interval is that represented by: `'-' yyyy '-' mm '-' dd 'T00:00:00' zzzzzz?` and the least upper bound of the interval is the timeline point represented (noncanonically) by: `'-' yyyy '-' mm '-' dd 'T24:00:00' zzzzzz?`.

IRI: `http://www.w3.org/2001/XMLSchema#date`

#### dateTime


The ·lexical space· of dateTime consists of finite-length sequences of characters of the form: `'-'? yyyy '-' mm '-' dd 'T' hh ':' mm ':' ss ('.' s+)? (zzzzzz)?` For example, `2002-10-10T12:00:00-05:00` (noon on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) is `2002-10-10T17:00:00Z`, five hours later than `2002-10-10T12:00:00Z`.

IRI: `http://www.w3.org/2001/XMLSchema#dateTime`

#### dateTimeStamp


The lexical space of dateTimeStamp consists of strings which are in the ·lexical space· of dateTime and which also match the regular expression '.*(Z|(+|-)[0-9][0-9]:[0-9][0-9])'

IRI: `http://www.w3.org/2001/XMLSchema#dateTimeStamp`

#### decimal


decimal has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39) separated by a period as a decimal indicator. An optional leading sign is allowed. If the sign is omitted, '+' is assumed. Leading and trailing zeroes are optional. If the fractional part is zero, the period and following zeroes can be omitted. For example: -1.23, 12678967.543233, +100000.00, 210.

IRI: `http://www.w3.org/2001/XMLSchema#decimal`

#### double


double values have a lexical representation consisting of a mantissa followed, optionally, by the character 'E' or 'e', followed by an exponent. The exponent ·must· be an integer. The mantissa must be a decimal number. The representations for exponent and mantissa must follow the lexical rules for integer and decimal. If the 'E' or 'e' and the following exponent are omitted, an exponent value of 0 is assumed. The special values positive and negative infinity and not-a-number have lexical representations INF, -INF and NaN, respectively. Lexical representations for zero may take a positive or negative sign. For example, -1E4, 1267.43233E12, 12.78e-2, 12 , -0, 0 and INF are all legal literals for double.

IRI: `http://www.w3.org/2001/XMLSchema#double`

#### duration


The lexical representation for duration is the ISO 8601 extended format `PnYnMnDTnHnMnS`, where `nY` represents the number of years, `nM` the number of months, `nD` the number of days, `T` is the date/time separator, `nH` the number of hours, `nM` the number of minutes and `nS` the number of seconds. The number of seconds can include decimal digits to arbitrary precision.

IRI: `http://www.w3.org/2001/XMLSchema#duration`

#### float


float values have a lexical representation consisting of a mantissa followed, optionally, by the character 'E' or 'e', followed by an exponent. The exponent ·must· be an integer. The mantissa must be a decimal number. The representations for exponent and mantissa must follow the lexical rules for integer and decimal. If the 'E' or 'e' and the following exponent are omitted, an exponent value of 0 is assumed. The special values positive and negative infinity and not-a-number have lexical representations INF, -INF and NaN, respectively. Lexical representations for zero may take a positive or negative sign. For example, -1E4, 1267.43233E12, 12.78e-2, 12 , -0, 0 and INF are all legal literals for float.

IRI: `http://www.w3.org/2001/XMLSchema#float`

#### gDay


The lexical representation for gDay is the left truncated lexical representation for date: `---DD` . An optional following time zone qualifier is allowed as for date. No preceding sign is allowed. No other formats are allowed. See also ISO 8601 Date and Time Formats.

IRI: `http://www.w3.org/2001/XMLSchema#gDay`

#### gMonth


The lexical representation for gMonth is the left and right truncated lexical representation for date: `--MM`. An optional following time zone qualifier is allowed as for date. No preceding sign is allowed. No other formats are allowed. See also ISO 8601 Date and Time Formats.

IRI: `http://www.w3.org/2001/XMLSchema#gMonth`

#### gMonthDay


The lexical representation for gMonthDay is the left truncated lexical representation for date: `--MM-DD`. An optional following time zone qualifier is allowed as for date. No preceding sign is allowed. No other formats are allowed. See also ISO 8601 Date and Time Formats. This datatype can be used to represent a specific day in a month. To say, for example, that my birthday occurs on the 14th of September ever year.

IRI: `http://www.w3.org/2001/XMLSchema#gMonthDay`

#### gYear


The lexical representation for gYear is the reduced (right truncated) lexical representation for dateTime: `CCYY`. No left truncation is allowed. An optional following time zone qualifier is allowed as for dateTime. To accommodate year values outside the range from `0001` to `9999`, additional digits can be added to the left of this representation and a preceding `-` sign is allowed. For example, to indicate 1999, one would write: `1999`. See also ISO 8601 Date and Time Formats.

IRI: `http://www.w3.org/2001/XMLSchema#gYear`

#### gYearMonth


The lexical representation for gYearMonth is the reduced (right truncated) lexical representation for dateTime: CCYY-MM. No left truncation is allowed. An optional following time zone qualifier is allowed. To accommodate year values outside the range from 0001 to 9999, additional digits can be added to the left of this representation and a preceding '-' sign is allowed. For example, to indicate the month of May 1999, one would write: 1999-05. See also ISO 8601 Date and Time Formats (·D).

IRI: `http://www.w3.org/2001/XMLSchema#gYearMonth`

#### hexBinary


hexBinary has a lexical representation where each binary octet is encoded as a character tuple, consisting of two hexadecimal digits ([0-9a-fA-F]) representing the octet code. For example, '0FB7' is a hex encoding for the 16-bit integer 4023 (whose binary representation is 111110110111).

IRI: `http://www.w3.org/2001/XMLSchema#hexBinary`

#### HTML


The datatype of RDF literals storing fragments of HTML content

IRI: `http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML`

#### int


int is ·derived· from long by setting the value of ·maxInclusive· to be 2147483647 and ·minInclusive· to be -2147483648. int has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, '+' is assumed. For example: -1, 0, 126789675, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#int`

#### integer


integer has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39) with an optional leading sign. If the sign is omitted, '+' is assumed. For example: -1, 0, 12678967543233, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#integer`

#### Jinja Template String


Jinja is a modern and designer-friendly templating language for Python and other languages.

IRI: `https://vocab.eccenca.com/shui/jinja`

#### langString


The datatype of language-tagged string values

IRI: `http://www.w3.org/1999/02/22-rdf-syntax-ns#langString`

#### language


language represents natural language identifiers as defined by by [RFC 3066] . The ·value space· of language is the set of all strings that are valid language identifiers as defined [RFC 3066] . The ·lexical space· of language is the set of all strings that conform to the pattern [a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})* . The ·base type· of language is token.

IRI: `http://www.w3.org/2001/XMLSchema#language`

#### long


long is ·derived· from integer by setting the value of ·maxInclusive· to be 9223372036854775807 and ·minInclusive· to be -9223372036854775808. long has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, '+' is assumed. For example: -1, 0, 12678967543233, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#long`

#### Markdown


In addition to rdf:HTML, this is the datatype of RDF literals storing fragments of markdown content. eccenca Corporate Memory user interfaces support the rendering of all basic Markdown syntax features as well as the extensions for tables, code blocks, strikethrough, task lists and footnotes.

IRI: `http://ns.ontowiki.net/SysOnt/Markdown`

#### Name


Name represents XML Names. The ·value space· of Name is the set of all strings which ·match· the Name production of [XML 1.0 (Second Edition)]. The ·lexical space· of Name is the set of all strings which ·match· the Name production of [XML 1.0 (Second Edition)]. The ·base type· of Name is token.

IRI: `http://www.w3.org/2001/XMLSchema#Name`

#### NCName


NCName represents XML 'non-colonized' Names. The ·value space· of NCName is the set of all strings which ·match· the NCName production of [Namespaces in XML]. The ·lexical space· of NCName is the set of all strings which ·match· the NCName production of [Namespaces in XML]. The ·base type· of NCName is Name.

IRI: `http://www.w3.org/2001/XMLSchema#NCName`

#### negativeInteger


negativeInteger has a lexical representation consisting of a negative sign ('-') followed by a finite-length sequence of decimal digits (#x30-#x39). For example: -1, -12678967543233, -100000.

IRI: `http://www.w3.org/2001/XMLSchema#negativeInteger`

#### NMTOKEN


NMTOKEN represents the NMTOKEN attribute type from [XML 1.0 (Second Edition)]. The ·value space· of NMTOKEN is the set of tokens that ·match· the Nmtoken production in [XML 1.0 (Second Edition)]. The ·lexical space· of NMTOKEN is the set of strings that ·match· the Nmtoken production in [XML 1.0 (Second Edition)]. The ·base type· of NMTOKEN is token.

IRI: `http://www.w3.org/2001/XMLSchema#NMTOKEN`

#### nonNegativeInteger


nonNegativeInteger has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, the positive sign ('+') is assumed. If the sign is present, it must be '+' except for lexical forms denoting zero, which may be preceded by a positive ('+') or a negative ('-') sign. For example: 1, 0, 12678967543233, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#nonNegativeInteger`

#### nonPositiveInteger


nonPositiveInteger has a lexical representation consisting of an optional preceding sign followed by a finite-length sequence of decimal digits (#x30-#x39). The sign may be '+' or may be omitted only for lexical forms denoting zero, in all other lexical forms, the negative sign ('-') must be present. For example: -1, 0, -12678967543233, -100000.

IRI: `http://www.w3.org/2001/XMLSchema#nonPositiveInteger`

#### normalizedString


normalizedString represents white space normalized strings. The ·value space· of normalizedString is the set of strings that do not contain the carriage return (#xD), line feed (#xA) nor tab (#x9) characters. The ·lexical space· of normalizedString is the set of strings that do not contain the carriage return (#xD), line feed (#xA) nor tab (#x9) characters. The ·base type· of normalizedString is string.

IRI: `http://www.w3.org/2001/XMLSchema#normalizedString`

#### positiveInteger


positiveInteger has a lexical representation consisting of an optional positive sign ('+') followed by a finite-length sequence of decimal digits (#x30-#x39). For example: 1, 12678967543233, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#positiveInteger`

#### short


short is ·derived· from int by setting the value of ·maxInclusive· to be 32767 and ·minInclusive· to be -32768. short has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, '+' is assumed. For example: -1, 0, 12678, +10000.

IRI: `http://www.w3.org/2001/XMLSchema#short`

#### string


The string datatype represents character strings in XML. The ·value space· of string is the set of finite-length sequences of characters (as defined in [XML 1.0 (Second Edition)]) that ·match· the Char production from [XML 1.0 (Second Edition)]. A character is an atomic unit of communication, it is not further specified except to note that every character has a corresponding Universal Character Set code point, which is an integer.

IRI: `http://www.w3.org/2001/XMLSchema#string`

#### time


The lexical representation for time is the left truncated lexical representation for dateTime: `hh:mm:ss.sss` with optional following time zone indicator. For example, to indicate 1:20 pm for Eastern Standard Time which is 5 hours behind Coordinated Universal Time (UTC), one would write: `13:20:00-05:00`. See also ISO 8601 Date and Time Formats.

IRI: `http://www.w3.org/2001/XMLSchema#time`

#### token


token represents tokenized strings. The ·value space· of token is the set of strings that do not contain the carriage return (#xD), line feed (#xA) nor tab (#x9) characters, that have no leading or trailing spaces (#x20) and that have no internal sequences of two or more spaces. The ·lexical space· of token is the set of strings that do not contain the carriage return (#xD), line feed (#xA) nor tab (#x9) characters, that have no leading or trailing spaces (#x20) and that have no internal sequences of two or more spaces. The ·base type· of token is normalizedString.

IRI: `http://www.w3.org/2001/XMLSchema#token`

#### unsignedByte


unsignedByte is ·derived· from unsignedShort by setting the value of ·maxInclusive· to be 255. unsignedByte has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39). For example: 0, 126, 100.

IRI: `http://www.w3.org/2001/XMLSchema#unsignedByte`

#### unsignedInt


unsignedInt is ·derived· from unsignedLong by setting the value of ·maxInclusive· to be 4294967295. unsignedInt has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39). For example: 0, 1267896754, 100000.

IRI: `http://www.w3.org/2001/XMLSchema#unsignedInt`

#### unsignedLong


unsignedLong is ·derived· from nonNegativeInteger by setting the value of ·maxInclusive· to be 18446744073709551615. unsignedLong has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39). For example: 0, 12678967543233, 100000.

IRI: `http://www.w3.org/2001/XMLSchema#unsignedLong`

#### unsignedShort


unsignedShort is ·derived· from unsignedInt by setting the value of ·maxInclusive· to be 65535. unsignedShort has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39). For example: 0, 12678, 10000.

IRI: `http://www.w3.org/2001/XMLSchema#unsignedShort`

#### XMLLiteral


The datatype of XML literal values.

IRI: `http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral`

