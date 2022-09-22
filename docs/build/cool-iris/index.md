# Cool IRIs

## Introduction

URIs and IRIs are character strings identifying the nodes and edges in the graph. Defining them is an important step in creating an exploitable Knowledge Graph for your Company.

[RFC 3986](http://tools.ietf.org/html/rfc3986) defines a generic syntax for URIs:

- `<scheme>:<scheme-specific-part>`
- Scheme-specific part often structured: `<authority>/<path>?<query>`

URIs are limited to ASCII characters. IRIs (Internationalized Resource Identifiers) allow Unicode ([RFC 3987](https://tools.ietf.org/html/rfc3987)).

The following list of example IRIs demonstrate the broad scope of this concept:

- `ftp://ftp.is.co.za/rfc/rfc1808.txt`
- `http://www.ietf.org/rfc/rfc2396.txt`
- `ldap://[2001:db8::7]/c=GB?objectClass?one`
- `mailto:John.Doe@example.com`
- `news:comp.infosystems.www.servers.unix`
- `tel:+1-816-555-1212`
- `telnet://192.0.2.16:80/`
- `urn:oasis:names:specification:docbook:dtd:xml:4.1.2`

## Best practices in Corporate Memory

A good IRI is unique, stable, simple and manageable.

Define a useful IRI-Scheme that can be used for resources.

- Define a Base URI which is the common authority for all resources in your graph.
    - Example: `https://data.company.org/`
- Define subspaces where necessary, e.g. for each subproject or domain. Provide a [prefix](/build/define-prefixes-namespaces) for each subspace. Examples:
    - `https://data.company.org/hardware/` for hardware artifacts
    - `https://data.company.org/software/` for software artifacts
    - `PREFIX cohw: <https://data.company.org/hardware/>`
    - `PREFIX cosw: <https://data.company.org/software/>`
- Based on these build consistent schemes that define how your IRIs have to be build. Examples:
    - `https://data.company.org/hardware/<ProductClass>/<Serialnumber>` to identify an individual product
    - `https://data.company.org/hardware/<ProductClass>/<Modelnumber>` to identify a product model

!!! warning

    Do not put a trailing slash on the end of IRIs. IRIs with a trailing slash can not be used with prefix definitions in Turtle or SPARQL, which makes them more difficult to use.

## More information

- Spanish Government, URIs for Open Data resources: [https://www.boe.es/diario_boe/txt.php?id=BOE-A-2013-2380](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2013-2380)
- European Union, URIs for Legal Resources: [https://eur-lex.europa.eu/eli-register/technical_information.html](https://eur-lex.europa.eu/eli-register/technical_information.html)
- UK, "Designing URI sets for the UK public sector": [https://www.gov.uk/government/publications/designing-uri-sets-for-the-uk-public-sector](https://www.gov.uk/government/publications/designing-uri-sets-for-the-uk-public-sector)
- Other Resources
    - [https://www.w3.org/TR/cooluris/](https://www.w3.org/TR/cooluris/)
    - [https://www.w3.org/Provider/Style/URI.html](https://www.w3.org/Provider/Style/URI.html)
    - [https://www.w3.org/wiki/GoodURIs](https://www.w3.org/wiki/GoodURIs)
    - [https://www.w3.org/TR/dwbp/](https://www.w3.org/TR/dwbp/)
    - [https://www.w3.org/TR/ld-bp/](https://www.w3.org/TR/ld-bp/)
