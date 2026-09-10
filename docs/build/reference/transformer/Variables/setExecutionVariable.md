---
title: "Set execution variable"
description: "Sets an execution variable to the first value of the (single) input and passes the input values through unchanged. The variable is written to the 'execution' scope and can be read downstream as 'execution.<name>'. Only works while running inside a workflow execution."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Set execution variable

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Sets an execution variable to the first value of the (single) input and passes the input values through unchanged. The variable is written to the 'execution' scope and can be read downstream as 'execution.<name>'. Only works while running inside a workflow execution.


## Parameter

### Variable name

Name of the execution variable to set. It is written to the 'execution' scope and addressed downstream as 'execution.<name>'.

- ID: `variableName`
- Datatype: `string`
- Default Value: `myVariable`

## Advanced Parameter

`None`
