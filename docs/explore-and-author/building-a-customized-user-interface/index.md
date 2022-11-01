---
tags:
    - KnowledgeGraph
---
# Building a customized User Interface

## Introduction

Working with shapes allows for creation of a customized Linked Data user interface. In addition to the standard PROPERTIES tab that shows all properties of a data resource, you can create custom "form"-like data interfaces. These configurable forms allow for a cleaner interface to view and author data resources. In addition, they enable integration of data from other resources that are linked to the current resource, creating a more concise view on your data.

## Defining forms

You can define forms using SHACL rules. The rules state:

1.  What types of resources the form definition applies to. This is based on the `rdf:type` of a resource.
2.  What fields are shown in the form in which order. Field contents are retrieved from properties connected to the resource.
3.  Which other, linked resources are shown in the form. Linked resources can either be shown as links or as their full form.
4.  Which texts are used to name and describe fields, as well as the tab in the user interface.

Forms are defined in the CMEM Shapes Catalog graph. The graph URI is `https://vocab.eccenca.com/shacl/`.

Form definitions are twofold:

1.  The form itself is defined as so called `NodeShape`. NodeShapes define which types of resources the form applies to (the target class), and which fields are shown in the form (the Properties).
2.  The individual fields are defined as so called `PropertyShape`. PropertyShapes define which property is used to retrieve data for the field (the path), the name of the field, a description, its cardinality (min and max count), its position in the form (the order), and if it should always be shown. In case of object properties, it also defines the type of the linked resource (the class). The full list of features is described in [section PropertyShapes](#propertyshapes).

To define a new form, for example for `foaf:Person` resources, navigate to the CMEM Shapes Catalog graph and select `NodeShape` in Navigation. The list of existing NodeShapes is shown. Click "Create a new SHACL Node shape" in the upper right to create a new NodeShape. Enter a name of the resource. An empty NodeShape resource is created and shown.

[![](./createNodeShape.png)](./createNodeShape.png)

To create the initial definition, click ![](./ic_mode_edit_black_18dp_1x.png){ .off-glb } (Edit). A form is shown to you with input fields Name, Property Shapes, Vocabulary, Target class and Statement Annotation. The initial definition requires the name, and the target class. Fields are attached to the form later. Target class in particular binds the form to the resources it should cover. The Target class field features an auto-complete that displays all classes stored in Corporate Memory. The example form should cover resources of the type `foaf:Person`, so enter `foaf:Person` in the Target class field. Click SAVE to save the NodeShape.

[![](./EditNodeShape.png)](./EditNodeShape.png)

You have now created an "empty" form that covers `foaf:Person` resources with tab name "Person". Navigating to a `foaf:Person` resource, you see a new tab as defined. You can still see all properties of the resource in the PROPERTIES tab.

[![](./nodeshape.png)](./nodeshape.png)

To define new fields, for example showing the email address of the person (defined as `foaf:mbox`), navigate to the CMEM Shapes Catalog graph and select `PropertyShape` in Navigation. The list of existing PropertyShapes is shown. Click CREATE NEW PROPERTYSHAPE in the upper right to create a new PropertyShape. Enter a name of the resource. An empty PropertyShape resource is created and shown.

Edit the form using ![](./ic_mode_edit_black_18dp_1x.png). A form is shown with all relevant properties of a field definition. Required in this step are:

1.  The name of the field, which will be displayed left of the data content or input field in the form.
2.  The description, which will be displayed as tooltip on the question mark to the right of the name.
3.  The path, which states which property the field represents. In this example, it is `foaf:mbox`.
4.  The form the field should be shown in (Property of). The field provides an auto-complete, so just enter "Person" and select the NodeShape resource you defined in the previous step.

Click SAVE after filling out the required fields.

[![](./nodeshapeedit.png)](./nodeshapeedit.png)

### NodeShapes

Node Shapes are resources of type `shacl:NodeShape`. They are used to define custom forms attached to resources of a specific type. The following NodeShape properties are supported:

In addition to these properties, the following non-standard properties from the eccenca SHACL UI extension are supported on Node Shapes:

#### Naming and Presentation

In this group, presentation and naming properties are collected. Most of the properties are straight forward to use.

##### Name

The name of the node is presented to the user only when he needs to distinguish between different shapes for the same resource.

Used Path: `shacl:name`

##### Description

The node description should provide context information for the user when creating a new resource based on this node.

Used Path: `rdfs:comment`

##### Tab Name (deprecated)

Name of the tab (deprecated, only interpreted until 20.06)

Used Path: `shui:tabName`

##### Navigation list query

This property links the node shape to a SPARQL 1.1 Select Query in order to provide a sophisticated user navigation list query e.g. to add specific additional columns.

Used Path: `shui:navigationListQuery`

#### Vocabulary

In this group, the affected vocabulary classes as well as the used property shapes are managed.

##### Property

Properties of this node

Used Path: `shacl:property`

##### Target class

Class this NodeShape applies to.

Used Path: `shacl:targetClass`

#### Processing

In this group, all shape properties are managed, have an effect on how new or existing resources are processed or created.

##### URI template

A compact sequence of characters for describing a range of URIs through variable expansion.

Used Path: `shui:uriTemplate`

##### On update update

A query executed when any value of the resource is added, changed or removed.

Used Path: `shui:onUpdateUpdate`

##### Target Graph Template

Graph templates can be used to enforce writing statement in specific graphs rather than into the selected graph. Graph templates can be added to node and property shapes. A template on a property shape is used only for overwriting a template on a node shape (without a node shape graph template, they do not have an effect).

Used Path: `shui:targetGraphTemplate`

#### Statement Annotation

Statement Annotations provide a way to express knowledge about statements. This group is dedicated to properties which configure the Statement Annotation feature.

##### Enable

A value of true enables visualisation and management capabilities of statement annotations (reification) for all statements which are shown via this shape.

Used Path: `shui:enableStatementLevelMetadata`

##### Provide as Shape

A value of true enables this node shape to be applied as statement annotation (reification).

Used Path: `shui:isApplicableAsStatementLevelMetadata`

### PropertyShapes

Property Shapes are resources of type `[shacl:PropertyShape](http://www.w3.org/ns/shacl#PropertyShape)`. They are used to specify constraints and UI options that need to be met in the context of a Node Shape. The following Property Shape properties of SHACL are supported:

!!! info
    Name and Description are displayed using the configuration of titleHelper. See [Deploy and Configure → Configuration → DataManager](../../deploy-and-configure/configuration/datamanager) for more details.

#### Naming and Presentation

In this group, presentation and naming properties are collected. Most of the properties are straight forward to use, other properties provide more complex features, such as table reports.

##### Name

This name will be shown to the user.

Used Path: `shacl:name`

##### Description

This text will be shown to the user in a tooltip. You can use new and blank lines for basic text structuring.

Used Path: `shacl:description`

##### Query: Table Report

Use this property to provide a tabular read-only report of a custom SPARQL query at the place where this property shape is used in the user interface. The following placeholder can be used in the query text of the sparql query: {{shuiMainResource}} - refers to the main resource rendered in the starte node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage) ; {{shuiResource}} - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape) ; {{shuiGraph}} - the currently used graph.

Used Path: `shui:valueQuery`

##### Query: Table Report (hide header)

If set to true, the report table will be rendered without header (in case you expect only a single value).

Used Path: `shui:valueQueryHideHeader`

##### Query: Table Report (hide footer)

If set to true, the report table will be rendered without footer (in case you expect only a single value or row).

Used Path: `shui:valueQueryHideFooter`

##### Order

Specifies the order of the property in the UI. Ordering is separate for each group.

Used Path: `shacl:order`

##### Group

Group to which the property belongs to.

Used Path: `shacl:group`

##### Show always

Default is false. A value of true let optional properties (min count = 0) show up by default.

Used Path: `shui:showAlways`

##### Read only

Default is false. A value of true means the properties are not editable by the user. Useful for displaying system properties.

Used Path: `shui:readOnly`

#### Vocabulary

In this group, property paths as well cardinality restrictions are managed.

##### Property of

The node shape this property shape belongs to.

Used Path: `shacl:property`

##### Path

The datatype or object property used in this shape.

Used Path: `shacl:path`

##### Node kind

Type of the node.

Used Path: `shacl:nodeKind`

##### Min count

Min cardinality, 0 will show this property under optionals unless 'Show always = true'

Used Path: `shacl:minCount`

##### Max count

Max cardinality

Used Path: `shacl:maxCount`

#### Datatype Property Specific

In this group, all shape properties are managed, which only have effects on datatype properties.

##### Datatype

The datatype of the property.

Used Path: `shacl:datatype`

##### Use textarea

Default is false. A value of true enables multiline editing capabilities for Literals via a textarea widget.

Used Path: `shui:textarea`

##### Regex Pattern

A XPath regular expression (Perl like) that all literal strings need to match.

Used Path: `shacl:pattern`

##### Regex Flags

An optional string of flags for the regular expression pattern (e.g. 'i' for case-insensitive mode)

Used Path: `shacl:flags`

##### Languages allowed

This limits the given Literals to a list of languages. This property works only in combination with the datatype rdf:langString. Note that the expression for this property only allows for '2 Char ISO-639-1-Codes' only (no sub-tags).

Used Path: `shui:languageIn`

##### Languages Unique

Default is false. A value of true enforces that no pair of Literals may use the same language tag.

Used Path: `shacl:uniqueLang`

#### Object Property Specific

In this group, all shape properties are managed, which only have effects on object properties.

##### Class

Class of the connected IRI if nodeKind == sh:IRI.

Used Path: `shacl:class`

##### Query: Selectable Resources

This query allows for listing selectable resources in the dropdown list for this property shape.

Used Path: `shui:uiQuery`

##### Inverse Path

Default is false. A value of true inverts the expected / created direction of a relation.

Used Path: `shui:inversePath`

##### Deny new resources

A value of true disables the option to create new resources.

Used Path: `shui:denyNewResources`

##### Node shape

The shape of the linked resource.

Used Path: `shacl:node`

#### Processing

In this group, all shape properties are managed, have an effect on how new or existing resources are processed or created.

##### URI template

A compact sequence of characters for describing a range of URIs through variable expansion.

Used Path: `shui:uriTemplate`

##### Ignore on copy

Disables reusing the value(s) when creating a copy of the resource.

Used Path: `shui:ignoreOnCopy`

##### Query: On insert update

This query is executed when a property value is added or changed.

The following placeholder can be used in the query text of the sparql query: {{shuiMainResource}} - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage) ; {{shuiResource}} - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape) ; {{shuiGraph}} - the currently used graph.

Used Path: `shui:onInsertUpdate`

##### Query: On delete update

This query is executed when a value is changed or removed.

The following placeholder can be used in the query text of the sparql query: {{shuiMainResource}} - refers to the main resource rendered in the start node shape of the currently displayed node shape tree (only relevant in case of sub-shape usage) ; {{shuiResource}} - refers to the resource which is rendered in the node shape where this property shape is used (maybe a sub-shape) ; {{shuiGraph}} - the currently used graph.

Used Path: `shui:onDeleteUpdate`

##### Target Graph Template

Graph templates can be used to enforce writing statement in specific graphs rather than into the selected graph. Graph templates can be added to node and property shapes. A template on a property shape is used only for overwriting a template on a node shape (without a node shape graph template, they do not have an effect).

Used Path: `shui:targetGraphTemplate`

#### Statement Annotation

Statement Annotations provide a way to express knowledge about statements. This group is dedicated to properties which configure the Statement Annotation feature.

##### Enable

A value of true enables visualisation and management capabilities of statement annotations (reification) for all statements which are shown via this shape.

Used Path: `shui:enableStatementLevelMetadata`

##### Provided Shapes

Instead of providing all possible statement annotation node shapes for the creation of new statement annotations, this property will limit the list to the selected shapes only.

Used Path: `shui:provideStatementLevelMetadataShapes`

### Datatypes

This is a list of supported data types in shapes. Not all datatypes result in specific widgets.

#### anyURI

The -lexical space- of anyURI is finite-length character sequences which, when the algorithm defined in Section 5.4 of [XML Linking Language] is applied to them, result in strings which are legal URIs according to [RFC 2396], as amended by [RFC 2732]. Note: Spaces are, in principle, allowed in the -lexical space- of anyURI, however, their use is highly discouraged (unless they are encoded by %20).

IRI: `http://www.w3.org/2001/XMLSchema#anyURI`

#### base64Binary

The lexical forms of base64Binary values are limited to the 65 characters of the Base64 Alphabet defined in [RFC 2045], i.e., a-z, A-Z, 0-9, the plus sign (+), the forward slash (/) and the equal sign (=), together with the characters defined in [XML 1.0 (Second Edition)] as white space. No other characters are allowed.

IRI: `http://www.w3.org/2001/XMLSchema#base64Binary`

#### boolean

An instance of a datatype that is defined as -boolean- can have the following legal literals {true, false, 1, 0}.

IRI: `http://www.w3.org/2001/XMLSchema#boolean`

#### byte

byte is -derived- from short by setting the value of -maxInclusive- to be 127 and -minInclusive- to be -128. byte has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, '+' is assumed. For example: -1, 0, 126, +100.

IRI: `http://www.w3.org/2001/XMLSchema#byte`

#### date

The -lexical space- of date consists of finite-length sequences of characters of the form: '-'? yyyy '-' mm '-' dd zzzzzz? where the date and optional timezone are represented exactly the same way as they are for dateTime. The first moment of the interval is that represented by: '-' yyyy '-' mm '-' dd 'T00:00:00' zzzzzz? and the least upper bound of the interval is the timeline point represented (noncanonically) by: '-' yyyy '-' mm '-' dd 'T24:00:00' zzzzzz?.

IRI: `http://www.w3.org/2001/XMLSchema#date`

#### dateTime

The -lexical space- of dateTime consists of finite-length sequences of characters of the form: '-'? yyyy '-' mm '-' dd 'T' hh ':' mm ':' ss ('.' s+)? (zzzzzz)? For example, 2002-10-10T12:00:00-05:00 (noon on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) is 2002-10-10T17:00:00Z, five hours later than 2002-10-10T12:00:00Z.

IRI: `http://www.w3.org/2001/XMLSchema#dateTime`

#### dateTimeStamp

The lexical space of dateTimeStamp consists of strings which are in the -lexical space- of dateTime and which also match the regular expression '.*(Z|(+|-)[0-9][0-9]:[0-9][0-9])'

IRI: `http://www.w3.org/2001/XMLSchema#dateTimeStamp`

#### decimal

decimal has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39) separated by a period as a decimal indicator. An optional leading sign is allowed. If the sign is omitted, '+' is assumed. Leading and trailing zeroes are optional. If the fractional part is zero, the period and following zeroes can be omitted. For example: -1.23, 12678967.543233, +100000.00, 210.

IRI: `http://www.w3.org/2001/XMLSchema#decimal`

#### double

double values have a lexical representation consisting of a mantissa followed, optionally, by the character 'E' or 'e', followed by an exponent. The exponent -must- be an integer. The mantissa must be a decimal number. The representations for exponent and mantissa must follow the lexical rules for integer and decimal. If the 'E' or 'e' and the following exponent are omitted, an exponent value of 0 is assumed. The special values positive and negative infinity and not-a-number have lexical representations INF, -INF and NaN, respectively. Lexical representations for zero may take a positive or negative sign. For example, -1E4, 1267.43233E12, 12.78e-2, 12 , -0, 0 and INF are all legal literals for double.

IRI: `http://www.w3.org/2001/XMLSchema#double`

#### duration

The lexical representation for duration is the [ISO 8601] extended format PnYn MnDTnH nMnS, where nY represents the number of years, nM the number of months, nD the number of days, 'T' is the date/time separator, nH the number of hours, nM the number of minutes and nS the number of seconds. The number of seconds can include decimal digits to arbitrary precision.

IRI: `http://www.w3.org/2001/XMLSchema#duration`

#### float

float values have a lexical representation consisting of a mantissa followed, optionally, by the character 'E' or 'e', followed by an exponent. The exponent -must- be an integer. The mantissa must be a decimal number. The representations for exponent and mantissa must follow the lexical rules for integer and decimal. If the 'E' or 'e' and the following exponent are omitted, an exponent value of 0 is assumed. The special values positive and negative infinity and not-a-number have lexical representations INF, -INF and NaN, respectively. Lexical representations for zero may take a positive or negative sign. For example, -1E4, 1267.43233E12, 12.78e-2, 12 , -0, 0 and INF are all legal literals for float.

IRI: `http://www.w3.org/2001/XMLSchema#float`

#### gDay

The lexical representation for gDay is the left truncated lexical representation for date: ---DD . An optional following time zone qualifier is allowed as for date. No preceding sign is allowed. No other formats are allowed. See also ISO 8601 Date and Time Formats (-D).

IRI: `http://www.w3.org/2001/XMLSchema#gDay`

#### gMonth

The lexical representation for gMonth is the left and right truncated lexical representation for date: --MM. An optional following time zone qualifier is allowed as for date. No preceding sign is allowed. No other formats are allowed. See also ISO 8601 Date and Time Formats (-D).

IRI: `http://www.w3.org/2001/XMLSchema#gMonth`

#### gMonthDay

The lexical representation for gMonthDay is the left truncated lexical representation for date: --MM-DD. An optional following time zone qualifier is allowed as for date. No preceding sign is allowed. No other formats are allowed. See also ISO 8601 Date and Time Formats (-D). This datatype can be used to represent a specific day in a month. To say, for example, that my birthday occurs on the 14th of September ever year.

IRI: `http://www.w3.org/2001/XMLSchema#gMonthDay`

#### gYear

The lexical representation for gYear is the reduced (right truncated) lexical representation for dateTime: CCYY. No left truncation is allowed. An optional following time zone qualifier is allowed as for dateTime. To accommodate year values outside the range from 0001 to 9999, additional digits can be added to the left of this representation and a preceding '-' sign is allowed. For example, to indicate 1999, one would write: 1999. See also ISO 8601 Date and Time Formats (-D).

IRI: `http://www.w3.org/2001/XMLSchema#gYear`

#### gYearMonth

The lexical representation for gYearMonth is the reduced (right truncated) lexical representation for dateTime: CCYY-MM. No left truncation is allowed. An optional following time zone qualifier is allowed. To accommodate year values outside the range from 0001 to 9999, additional digits can be added to the left of this representation and a preceding '-' sign is allowed. For example, to indicate the month of May 1999, one would write: 1999-05. See also ISO 8601 Date and Time Formats (-D).

IRI: `http://www.w3.org/2001/XMLSchema#gYearMonth`

#### hexBinary

hexBinary has a lexical representation where each binary octet is encoded as a character tuple, consisting of two hexadecimal digits ([0-9a-fA-F]) representing the octet code. For example, '0FB7' is a hex encoding for the 16-bit integer 4023 (whose binary representation is 111110110111).

IRI: `http://www.w3.org/2001/XMLSchema#hexBinary`

#### HTML

The datatype of RDF literals storing fragments of HTML content

IRI: `http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML`

#### int

int is -derived- from long by setting the value of -maxInclusive- to be 2147483647 and -minInclusive- to be -2147483648. int has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, '+' is assumed. For example: -1, 0, 126789675, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#int`

#### integer

integer has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39) with an optional leading sign. If the sign is omitted, '+' is assumed. For example: -1, 0, 12678967543233, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#integer`

#### Jinja Template String (datatype)

Jinja is a modern and designer-friendly templating language for Python and other languages.

IRI: `https://vocab.eccenca.com/shui/jinja`

#### langString

The datatype of language-tagged string values

IRI: `http://www.w3.org/1999/02/22-rdf-syntax-ns#langString`

#### language

language represents natural language identifiers as defined by by [RFC 3066] . The -value space- of language is the set of all strings that are valid language identifiers as defined [RFC 3066] . The -lexical space- of language is the set of all strings that conform to the pattern [a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})* . The -base type- of language is token.

IRI: `http://www.w3.org/2001/XMLSchema#language`

#### long

long is -derived- from integer by setting the value of -maxInclusive- to be 9223372036854775807 and -minInclusive- to be -9223372036854775808. long has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, '+' is assumed. For example: -1, 0, 12678967543233, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#long`

#### Markdown

In addition to rdf:HTML, this is the datatype RDF literals storing fragments of markdown content.

IRI: `http://ns.ontowiki.net/SysOnt/Markdown`

#### Name

Name represents XML Names. The -value space- of Name is the set of all strings which -match- the Name production of [XML 1.0 (Second Edition)]. The -lexical space- of Name is the set of all strings which -match- the Name production of [XML 1.0 (Second Edition)]. The -base type- of Name is token.

IRI: `http://www.w3.org/2001/XMLSchema#Name`

#### NCName

NCName represents XML 'non-colonized' Names. The -value space- of NCName is the set of all strings which -match- the NCName production of [Namespaces in XML]. The -lexical space- of NCName is the set of all strings which -match- the NCName production of [Namespaces in XML]. The -base type- of NCName is Name.

IRI: `http://www.w3.org/2001/XMLSchema#NCName`

#### negativeInteger

negativeInteger has a lexical representation consisting of a negative sign ('-') followed by a finite-length sequence of decimal digits (#x30-#x39). For example: -1, -12678967543233, -100000.

IRI: `http://www.w3.org/2001/XMLSchema#negativeInteger`

#### NMTOKEN

NMTOKEN represents the NMTOKEN attribute type from [XML 1.0 (Second Edition)]. The -value space- of NMTOKEN is the set of tokens that -match- the Nmtoken production in [XML 1.0 (Second Edition)]. The -lexical space- of NMTOKEN is the set of strings that -match- the Nmtoken production in [XML 1.0 (Second Edition)]. The -base type- of NMTOKEN is token.

IRI: `http://www.w3.org/2001/XMLSchema#NMTOKEN`

#### nonNegativeInteger

nonNegativeInteger has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, the positive sign ('+') is assumed. If the sign is present, it must be '+' except for lexical forms denoting zero, which may be preceded by a positive ('+') or a negative ('-') sign. For example: 1, 0, 12678967543233, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#nonNegativeInteger`

#### nonPositiveInteger

nonPositiveInteger has a lexical representation consisting of an optional preceding sign followed by a finite-length sequence of decimal digits (#x30-#x39). The sign may be '+' or may be omitted only for lexical forms denoting zero, in all other lexical forms, the negative sign ('-') must be present. For example: -1, 0, -12678967543233, -100000.

IRI: `http://www.w3.org/2001/XMLSchema#nonPositiveInteger`

#### normalizedString

normalizedString represents white space normalized strings. The -value space- of normalizedString is the set of strings that do not contain the carriage return (#xD), line feed (#xA) nor tab (#x9) characters. The -lexical space- of normalizedString is the set of strings that do not contain the carriage return (#xD), line feed (#xA) nor tab (#x9) characters. The -base type- of normalizedString is string.

IRI: `http://www.w3.org/2001/XMLSchema#normalizedString`

#### PlainLiteral

The class of plain (i.e. untyped) literal values, as used in RIF and OWL 2

IRI: `http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral`

#### positiveInteger

positiveInteger has a lexical representation consisting of an optional positive sign ('+') followed by a finite-length sequence of decimal digits (#x30-#x39). For example: 1, 12678967543233, +100000.

IRI: `http://www.w3.org/2001/XMLSchema#positiveInteger`

#### short

short is -derived- from int by setting the value of -maxInclusive- to be 32767 and -minInclusive- to be -32768. short has a lexical representation consisting of an optional sign followed by a finite-length sequence of decimal digits (#x30-#x39). If the sign is omitted, '+' is assumed. For example: -1, 0, 12678, +10000.

IRI: `http://www.w3.org/2001/XMLSchema#short`

#### sparqlOperation

sparql operation datatype (query or update)

IRI: `https://vocab.eccenca.com/shui/sparqlOperation`

#### sparqlQuery

SPARQL 1.1 Query

IRI: `https://vocab.eccenca.com/shui/sparqlQuery`

#### sparqlUpdate

SPARQL 1.1 Update

IRI: `https://vocab.eccenca.com/shui/sparqlUpdate`

#### string

The string datatype represents character strings in XML. The -value space- of string is the set of finite-length sequences of characters (as defined in [XML 1.0 (Second Edition)]) that -match- the Char production from [XML 1.0 (Second Edition)]. A character is an atomic unit of communication, it is not further specified except to note that every character has a corresponding Universal Character Set code point, which is an integer.

IRI: `http://www.w3.org/2001/XMLSchema#string`

#### time

The lexical representation for time is the left truncated lexical representation for dateTime: hh:mm:ss.sss with optional following time zone indicator. For example, to indicate 1:20 pm for Eastern Standard Time which is 5 hours behind Coordinated Universal Time (UTC), one would write: 13:20:00-05:00. See also ISO 8601 Date and Time Formats (-D).

IRI: `http://www.w3.org/2001/XMLSchema#time`

#### token

token represents tokenized strings. The -value space- of token is the set of strings that do not contain the carriage return (#xD), line feed (#xA) nor tab (#x9) characters, that have no leading or trailing spaces (#x20) and that have no internal sequences of two or more spaces. The -lexical space- of token is the set of strings that do not contain the carriage return (#xD), line feed (#xA) nor tab (#x9) characters, that have no leading or trailing spaces (#x20) and that have no internal sequences of two or more spaces. The -base type- of token is normalizedString.

IRI: `http://www.w3.org/2001/XMLSchema#token`

#### unsignedByte

unsignedByte is -derived- from unsignedShort by setting the value of -maxInclusive- to be 255. unsignedByte has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39). For example: 0, 126, 100.

IRI: `http://www.w3.org/2001/XMLSchema#unsignedByte`

#### unsignedInt

unsignedInt is -derived- from unsignedLong by setting the value of -maxInclusive- to be 4294967295. unsignedInt has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39). For example: 0, 1267896754, 100000.

IRI: `http://www.w3.org/2001/XMLSchema#unsignedInt`

#### unsignedLong

unsignedLong is -derived- from nonNegativeInteger by setting the value of -maxInclusive- to be 18446744073709551615. unsignedLong has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39). For example: 0, 12678967543233, 100000.

IRI: `http://www.w3.org/2001/XMLSchema#unsignedLong`

#### unsignedShort

unsignedShort is -derived- from unsignedInt by setting the value of -maxInclusive- to be 65535. unsignedShort has a lexical representation consisting of a finite-length sequence of decimal digits (#x30-#x39). For example: 0, 12678, 10000.

IRI: `http://www.w3.org/2001/XMLSchema#unsignedShort`

#### XMLLiteral

The datatype of XML literal values.

IRI: `http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral`

## Using forms

Once a Node Shape is created for a specific class, you are able to use the specified entry form in the Explore component of Corporate Memory.

### Editing existing resources

While browsing your knowledge graph, you will always see your shape in action, when you click on a resource which is an instance of the class which is linked with `shacl:targetClass` from your Node Shape.

The next images demonstrate this behavior :

[![](./nodeshape.png)](./nodeshape.png)

### Creating new resources

You can also create new resources by using a shaped form. One way to achieve this, is to select the class in the navigation tree on the lower left part in the Explore component and then click the Floating Action Button at the bottom or use the context menu on upper right side.

The next images demonstrate this behaviour:

[![](./createsparqlquery.png)](./createsparqlquery.png)

[![](./createsparqlqueryeditor.png)](./createsparqlqueryeditor.png)
