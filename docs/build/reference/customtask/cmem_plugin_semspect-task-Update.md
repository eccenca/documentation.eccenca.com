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

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

Tell SemSpect to prepare a Knowledge Graph for visualization.

## Parameter

### The URL of the SemSpect application.This needs to be accessible from 'within' DataIntegration.



- Datatype: `string`
- Default Value: `http://semspect:8080/semspect/`



### The SemSpect database ID. Not existing databases will be created.



- Datatype: `string`
- Default Value: `cmem`



### Knowledge Graph



- Datatype: `string`
- Default Value: `None`



### The URL of the DataPlatform application.This needs to be accessible from 'within' SemSpect.



- Datatype: `string`
- Default Value: `None`



### Timeout (in seconds) for the overall indexing activity.



- Datatype: `Long`
- Default Value: `300`



### Timeout (in seconds) for individual Semspect requests



- Datatype: `Long`
- Default Value: `10`



### ignore_proxy: Ignore system settings for HTTP proxies for the requests to semspect.



- Datatype: `boolean`
- Default Value: `false`



### verify_ssl: If disabled, the plugin will accept any TLS certificate presented by the server and will ignore hostname mismatches and/or expired certificates, which will make the requests vulnerable to man-in-the-middle (MitM) attacks. (use for testing only)



- Datatype: `boolean`
- Default Value: `true`



