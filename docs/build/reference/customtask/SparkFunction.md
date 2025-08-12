---
title: "Execute Spark function"
description: "Applies a specified Scala function to a specified field."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Execute Spark function
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Applies a specified Scala function to a specified field. E.g. when the inputField is 'name', the inputFunction is 'any => "Arrrrgh!" and the alias is 'xxx',)'
a query corresponding to 'Function existingField1, existingFiled2, ... "Arrrrgh!" as "xxx"'  will be generated.
If alias is empty the inputField will be overwritten, otherwise a new field will be added and the rest of the schema stays the same.


## Parameter

### Function

Scala function expression.

- Datatype: `multiline string`
- Default Value: `None`



### Input field

Input field.

- Datatype: `string`
- Default Value: `None`



### Alias

Alias.

- Datatype: `string`
- Default Value: `None`



