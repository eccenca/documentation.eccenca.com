---
title: "Retrieve coordinates"
description: "Retrieves geographic coordinates using Nominatim."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Retrieve coordinates
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->




**Configuration**

The geocoding service to be queried for searches can be set up in the configuration.
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

**Logging**

By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:

    logging.level {
      com.eccenca.di.geo=DEBUG
    }


## Parameter

### Additional parameters

Additional URL parameters to be attached to each HTTP search request. Example: '&countrycodes=de&addressdetails=1'. Consult the API documentation for a list of available parameters.

- Datatype: `string`
- Default Value: `None`



