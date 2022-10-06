# Label Resolution and Full-Text Search

## Introduction

Label resolution translates resource identifiers (URI/IRI) into human readable labels. This resolution, and by extends the full text search is configurable for different scenarios.

## Configuration

eccenca DataPlatform offers three configuration options: `labelProperties`(line 2) `languagePreferences` (line 5) and `languagePreferencesAnyLangFallback` (line 8).

```yaml
proxy:
  labelProperties: # (1)
  - "http://www.w3.org/2000/01/rdf-schema#label"
  - "http://www.w3.org/2004/02/skos/core#prefLabel"
  languagePreferences: #(2)
  - "en"
  - ""
  languagePreferencesAnyLangFallback: true #(3)
```

Copy

YML

These properties define not only which properties and languages should be considered, but also define the precedence of languages and properties over each other.

The retrieval process can simplified to the following procedure:

- First, when determining the label for a resource, the language is evaluated, then the property is considered.
- Consequently, for a resource in the default case:
    1. An english value for `rdfs:label` is searched.
    2. A literal without a language tag of the property `rdfs:label` is searched (this is why there is an entry `""`).
    3. An english value of `skos:prefLabel` is searched.
    4. A language-less value for `skos:prefLabel` is searched.
    5. If nothing is found, DataPlatform tries to create a prefixed URI, otherwise the last segment of the resource identifier is used.

Additionally, in case more than one label could be retrieved, for example by conflicting values, the alphabetically first entry is used.

## Example

How labels are resolved is best explained using those default settings and some examples.

```turtle
:Resource1 rdfs:label "Leipzig"@en.

:Resource2 :someOtherProperty "Berlin"@en.

:Resource3 rdfs:label "Stuttgart"@de

:Resource4 rdfs:label "Hanover"@en
:Resource4 rdfs:label "Another Label for Hanover"@en
```

- For `**:Resource1**`  the label will be `Leipzig`, as it will retrieve the english `rdfs:label`.
- For `**:Resource2 **`the label cannot be retrieved from the Knowledge Graph, as no know Property is used. Hence the fallback
- For :**Resource3**the label  will be retrieved as `Stuttgart` , if the (3) `languagePreferencesAnyLangFallback` is `true`*.*
  - While there is a well-known property used, none of the used languages matches. Using the fallback, the alphabetically first match is retrieved anyways.
- For **`:Resource4`**multiple label candidates could be determined.
  - In this case, `Another Label for Hanover` is retrieved, as it is the first value in the alphanumerical comparison.

## Client API

The label resolution functionality can also be used by client systems, the functionality is exposed as an [API endpoint](../../../develop/dataplatform-apis/index.md) (`<dp_url>/api/explore/title`).
