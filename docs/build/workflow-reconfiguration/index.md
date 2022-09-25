# Workflow Reconfiguration

## Introduction

The operators of a workflow can be reconfigured completely in the context of a workflow. During its execution, new parameters are loaded from any possible source and translated by a transformation task to allow an injection into the dataset configuration that overwrites originally set parameters. To reconfigure a workflow operator, the transformation task has to be connected to the red dot at the top of this operator as shown in the following image:

![Workflow config port](wf-config-port.png)

Although this feature has been developed to support the ingestion of database deltas, the possible applications are various since any parameter can be overwritten to make workflow operators even more dynamic and reusable in various contexts. The incremental ingestion of database content that was implemented as a first use-case can be found the application section of this page. However, we intend to add other use-cases that have been implemented. The following parameters seem to be good starting points for possible applications:

- Transformation Task:
    - Source Type
    - Source Restriction
- JDBC endpoint (remote)
    - Source Query
    - Write Strategy
    - Restriction
- Knowledge Graph (embedded)
    - Clear Graph before workflow execution
- Scheduler
    - Interval
    - Enabled
- …

## Implementation

To reconfigure a workflow operator, you need to create a transformation task, the data source of which is the intended source of the dynamic parameters of the workflow operator. Once you have created this task, you need to create a data value mapping for each parameter you want to overwrite.

!!! info

    Only one transformation task can be used to reconfigure the workflow operator and one source can be used for a transformation task's source. Thus, it is necessary to pre-process all parameters that need to be rewritten into one single dataset, e.g. a CSV file or a in-memory dataset. Then, you can use this dataset to inject all parameters with one transformation task.

Once you are sure, that your mapping rule entails the correct value, you can set the workflow operator parameter as the target property of the mapping rule. After this is done, you can reconfigure any workflow operator that uses this parameter as part of its configuration.

!!! info

    The transformation task needs a suffix of the workflow parameter's URI in the workflow operator's serialization as its target property. This differs from the documentation that just refers to the parameter's _name_. If you want to overwrite the source query of a JDBC endpoint, you need to define `sourceQuery` as the target property, which is the suffix of `<[https://vocab.eccenca.com/di/functions/param_Jdbc_sourceQuery](https://vocab.eccenca.com/di/functions/param_Jdbc_sourceQuery)`>.

## Applications

Tutorials that showcase this function in an application context:

- [Loading JDBC datasets incrementally](/build/workflow-reconfiguration/loading-jdbc-datasets-incrementally)