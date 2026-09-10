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

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Substitutes each input variable by its value:**

* Parameters
    * template:
    ```text

    Hello {{input1}} {{input2}},

    How are you today?
    ```

* Input values:
    1. `[John]`
    2. `[Doe]`

* Returns:
    ```text
    [Hello John Doe,

    How are you today?]
    ```


---
**Concatenates all values of a multi-valued input:**

* Parameters
    * template: `Hello {{input1}}`

* Input values:
    1. `[A, B]`

* Returns: `[Hello AB]`


---
**Supports iterating over the values of a multi-valued input:**

* Parameters
    * template: `Hello {% for value in input1 %}{{value}}, {% endfor %}how are you doing?`

* Input values:
    1. `[Bob, Eve]`

* Returns: `[Hello Bob, Eve, how are you doing?]`


---
**Supports method calls on input values:**

* Parameters
    * template: `{{ input1.trim() }}`

* Input values:
    1. `[ John ]`

* Returns: `[John]`


---
**Rejects unscoped variables that are no input variables:**

* Parameters
    * template: `Hello {{badVariable}} {{input1}}`

* Input values:
    1. `[John]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Rejects wrongly numbered input variables, the numbering starts at input1 without leading zeros:**

* Parameters
    * template: `Hello {{input01}}`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Rejects scoped variables from unknown scopes, e.g. misspelled scope names:**

* Parameters
    * template: `Hello {{projekt.myVar}}`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Fails at execution time if a referenced input is not connected:**

* Parameters
    * template: `Hello {{input1}}`

* Returns: `[]`
* **Throws error:** `UnboundVariablesException`




## Parameter

### Template

The template, using Jinja syntax.

* ID: `template`
* Datatype: `template`
* Default Value: `None`



### Language

The template language. Currently, Jinja is supported.

* ID: `language`
* Datatype: `string`
* Default Value: `jinja`

## Advanced Parameter

`None`
