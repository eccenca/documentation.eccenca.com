# Label Resolution and Full-Text Search

## Introduction

Label resolution translates resource identifiers (URI/IRI) into human readable labels. This resolution and, by extension, the full text search is configurable for different scenarios.

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

These properties define not only which properties and languages should be considered, but also the precedence of languages and properties over each other.

The retrieval process can be simplified to the following procedure:

- First, when determining the label for a resource, the language is evaluated, then the property is considered.
- Consequently, for a resource in the default case:
    1. An english value for `rdfs:label` is searched.
    2. A literal of the property `rdfs:label` without a language tag is searched (which is why there is an entry `""`).
    3. An english value of `skos:prefLabel` is searched.
    4. A literal of the property `skos:prefLabel` without a language tag is searched.
    5. If nothing is found, DataPlatform tries to create a prefixed URI, otherwise the last segment of the resource identifier is used.

Additionally, in case more than one label could be retrieved, for example by conflicting values, the alphabetically first entry is used.

## Example

How labels are resolved is best explained using these default settings and some examples.

```turtle
:Resource1 rdfs:label "Leipzig"@en.

:Resource2 :someOtherProperty "Berlin"@en.

:Resource3 rdfs:label "Stuttgart"@de

:Resource4 rdfs:label "Hanover"@en
:Resource4 rdfs:label "Another Label for Hanover"@en
```

- For `**:Resource1**` the label will be `Leipzig` as the english `rdfs:label` will be retrieved.
- For `**:Resource2 **` the label cannot be retrieved from the Knowledge Graph since no known property is used. Hence the fallback.
- For :**Resource3** the label will be retrieved as `Stuttgart`, if the (3) `languagePreferencesAnyLangFallback` is `true`*.*
  - While there is a well-known property used, none of the used languages match. Using the fallback, the alphabetically first match is retrieved in this case.
- For **`:Resource4`** multiple label candidates could be determined.
  - In this case, `Another Label for Hanover` is retrieved as it is the first value in the alphanumerical comparison.

## Client API

The label resolution functionality can also be used by client systems. This functionality is exposed as an [API endpoint](../../../develop/dataplatform-apis/index.md) (`<dp_url>/api/explore/title`).
