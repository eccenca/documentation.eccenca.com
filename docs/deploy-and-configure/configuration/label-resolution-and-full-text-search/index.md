# Label Resolution and Full-Text Search

## Introduction

Label resolution translates resource identifiers (URI/IRI) into human readable labels.
This resolution and, by extension, the full text search is configurable for different scenarios.

## Configuration

eccenca Explore backend (DataPlatform) offers three configuration options:

- `labelProperties` (line 2) 
- `languagePreferences` (line 6) and 
- `languagePreferencesAnyLangFallback` (line 10).

``` yaml linenums="1"
proxy:
  labelProperties:
  - "http://www.w3.org/2000/01/rdf-schema#label"
  - "http://www.w3.org/2004/02/skos/core#prefLabel"
  languagePreferences:
  - "en"
  - ""
  languagePreferencesAnyLangFallback: true
```

These properties define not only which properties and languages should be considered, but also the precedence of properties and languages over each other.

The retrieval process can be simplified to the following procedure:

- When `languagePreferencesAnyLangFallback` is `true`, the **property order takes precedence over the language order**. For each property, Explore backend (DataPlatform) first tries the configured languages in their listed order and then any other language. Only if that property has no value does it continue with the next property.
- Consequently, for a resource with the settings above, the candidates are tried in this order:
    1. An English, German, or untagged value for `rdfs:label` is searched, in that order.
    2. If none exists, an `rdfs:label` in any other language is used.
    3. The same language lookup is repeated for `skos:prefLabel` and then for `skos:notation`.
    4. If no configured property has a value, Explore backend (DataPlatform) tries to create a prefixed URI; otherwise, the last segment of the resource identifier is used.

Additionally, in case more than one label could be retrieved for the same property and language, for example by conflicting values, the alphabetically first entry is used.

!!! note "Any-language fallback preserves property precedence"

    With `languagePreferencesAnyLangFallback: true`, a value in any language on an earlier property is preferred over a value in a configured language on a later property.

    Consider the following configuration and resource:

    ``` yaml
    proxy:
      labelProperties:
      - "http://www.w3.org/2000/01/rdf-schema#label"
      - "http://www.w3.org/2004/02/skos/core#prefLabel"
      - "http://www.w3.org/2004/02/skos/core#notation"
      languagePreferences:
      - "en"
      - "de"
      - ""
      languagePreferencesAnyLangFallback: true
    ```

    ``` turtle
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX owl:     <http://www.w3.org/2002/07/owl#>
    PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos:    <http://www.w3.org/2004/02/skos/core#>
    PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>

    <http://docker.localhost/my-onto/label%20en>
        rdf:type          owl:Class ;
        rdfs:label        "label es"@es ;
        dcterms:modified  "2026-03-10"^^xsd:date ;
        skos:notation     "notation" .
    ```

    The resolved label is `label es`. Although Spanish is not listed in `languagePreferences`, `rdfs:label` is the first configured property. Its Spanish value is therefore selected by the any-language fallback before label resolution considers the untagged `skos:notation` value.

## Example

How labels are resolved is best explained using these default settings and some examples.

``` turtle
:Resource1 rdfs:label "Leipzig"@en.
:Resource2 :someOtherProperty "Berlin"@en.
:Resource3 rdfs:label "Stuttgart"@fr.
:Resource4 rdfs:label "Hanover"@en.
:Resource4 rdfs:label "Another Label for Hanover"@en.
```

- For `:Resource1` the label will be `Leipzig` as the english `rdfs:label` will be retrieved.
- For `:Resource2` the label cannot be retrieved from the Knowledge Graph since no known property is used. Hence the fallback.
- For `:Resource3` the label will be retrieved as `Stuttgart`, if the `languagePreferencesAnyLangFallback` is `true`.
    - While there is a well-known property used, none of the used languages match. Using the fallback, the alphabetically first match is retrieved in this case.
- For `:Resource4` multiple label candidates could be determined.
    - In this case, `Another Label for Hanover` is retrieved as it is the first value in the alphanumerical comparison.

## Client API

The label resolution functionality can also be used by client systems.
This functionality is exposed as an [API endpoint](../../../develop/dataplatform-apis/index.md) (`<dp_url>/api/explore/title`).
