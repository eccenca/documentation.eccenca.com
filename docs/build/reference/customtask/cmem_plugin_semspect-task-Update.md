---
title: "Update SemSpect"
description: "Tell SemSpect to prepare a Knowledge Graph for visualization."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Update SemSpect
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

Tell SemSpect to prepare a Knowledge Graph for visualization.

## Parameter

### The URL of the SemSpect application.This needs to be accessible from 'within' DataIntegration.



- ID: `base_url`
- Datatype: `string`
- Default Value: `http://semspect:8080/semspect/`



### The SemSpect database ID. Not existing databases will be created.



- ID: `database_id`
- Datatype: `string`
- Default Value: `cmem`



### Knowledge Graph



- ID: `graph`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

### The URL of the DataPlatform application.This needs to be accessible from 'within' SemSpect.



- ID: `dataplatform_base`
- Datatype: `string`
- Default Value: `None`



### Timeout (in seconds) for the overall indexing activity.



- ID: `timeout`
- Datatype: `Long`
- Default Value: `300`



### Timeout (in seconds) for individual Semspect requests



- ID: `request_timeout`
- Datatype: `Long`
- Default Value: `10`



### ignore_proxy: Ignore system settings for HTTP proxies for the requests to semspect.



- ID: `ignore_proxy`
- Datatype: `boolean`
- Default Value: `false`



### verify_ssl: If disabled, the plugin will accept any TLS certificate presented by the server and will ignore hostname mismatches and/or expired certificates, which will make the requests vulnerable to man-in-the-middle (MitM) attacks. (use for testing only)



- ID: `verify_ssl`
- Datatype: `boolean`
- Default Value: `true`



