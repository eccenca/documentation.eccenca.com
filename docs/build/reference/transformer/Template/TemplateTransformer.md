---
title: "Evaluate template"
description: "Evaluates a template. Input values can be addressed using the variables 'input1', 'input2', etc. Global variables are available in the 'global' scope, e.g., 'global.myVar'."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Evaluate template
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Evaluates a template. Input values can be addressed using the variables 'input1', 'input2', etc. Global variables are available in the 'global' scope, e.g., 'global.myVar'.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * template: 
    ```
    Hello {{input1}} {{input2}},
    
    How are you today?
    ```

* Input values:
    1. `[John]`
    2. `[Doe]`

* Returns: 
    ```
    [Hello John Doe,
    
    How are you today?]
    ```


---
**Example 2:**

* Parameters
    * template: `Hello {{badVariable}} {{input1}}`

* Input values:
    1. `[John]`
    2. `[Doe]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Example 3:**

* Parameters
    * template: `Hello {{input01}}`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Example 4:**

* Parameters
    * template: `Hello {{input1}}`

* Returns: `[]`
* **Throws error:** `UnboundVariablesException`


---
**Example 5:**

* Parameters
    * template: `Hello {{input1}}`

* Input values:
    1. `[A, B]`

* Returns: `[Hello AB]`


---
**Example 6:**

* Parameters
    * template: `Hello {% for value in input1 %}{{value}}, {% endfor %}how are you doing?`

* Input values:
    1. `[Bob, Eve]`

* Returns: `[Hello Bob, Eve, how are you doing?]`




## Parameter

### Template

The template

- ID: `template`
- Datatype: `template`
- Default Value: `None`



### Language

The template language. Currently, Jinja is supported.

- ID: `language`
- Datatype: `string`
- Default Value: `jinja`





## Advanced Parameter

`None`