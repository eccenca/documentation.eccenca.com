---
title: "Search addresses"
description: "Looks up locations from textual descriptions using the configured geocoding API. Outputs results as RDF."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Search addresses

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

## Configuration

The Geocoding service to be queried for searches can be set up in the configuration.
The default configuration is as follows:

    com.eccenca.di.geo = {
      # The URL of the geocoding service
      # url = "https://nominatim.eccenca.com/search"
      url = "https://photon.komoot.de/api"
      # url = https://api-adresse.data.gouv.fr/search

      # Additional URL parameters to be attached to all HTTP search requests. Example: '&countrycodes=de&addressdetails=1'.
      # Will be attached in addition to the parameters set on each search operator directly.
      searchParameters = ""

      # The minimum pause time between subsequent queries
      pauseTime = 1s

      # Number of coordinates to be cached in-memory
      cacheSize = 10
    }

In general, all services adhering to the [Nominatim search API](https://nominatim.org/release-docs/develop/api/Search/) should be usable.
Please note that when using public services, the pause time should be set to avoid overloading.

## Logging

By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:

    logging.level {
      com.eccenca.di.geo=DEBUG
    }

## Parameter

### Search attributes

List of attributes that contain search terms. Multiple attributes (comma-separated) will be concatenated into a single search.

- ID: `searchAttributes`
- Datatype: `traversable[string]`
- Default Value: `None`

### Limit

Optionally limits the number of results for each search.

- ID: `limit`
- Datatype: `option[int]`
- Default Value: `None`

## Advanced Parameter

### JSON-LD context

Optional JSON-LD context to be used for converting the returned JSON to RDF. If not provided, a default context will be used.

- ID: `jsonLdContext`
- Datatype: `resource`
- Default Value: `None`

### Additional parameters

Additional URL parameters to be attached to each HTTP search request. Example: '&countrycodes=de&addressdetails=1'. Consult the API documentation for a list of available parameters.

- ID: `additionalParameters`
- Datatype: `string`
- Default Value: `None`

