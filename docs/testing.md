<!-- markdownlint-disable MD012 MD013 MD024 MD033 -->
# Testing

...

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---

### Example from Geometric mean: 1

* Weights: [1, 2, 1]
* Input values: [0.0, 0.0, 0.0]
* Returns: `0.0`

!!! example "Example from Geometric mean: 1"

    | ... | ... |
    |------------------------:| :--------- |
    | Weights: | `[1, 2, 1]` |
    | Input values: | `[0.0, 0.0, 0.0]` |
    | Returns: | `0.0` |

!!! example "Example from Geometric mean: 1"

    === "Weights"

        ``` json
        [1, 2, 1]
        ```

    === "Input Values"

        ``` json
        [0.0, 0.0, 0.0]
        ```

    === "Returns"

        ``` json
        0.0
        ```


### Example from Handle missing values: Outputs the default score, if no input score is provided

* Parameters
  * *defaultValue*: `1.0`

* Input values: [(none)]
* Returns: `1.0`

!!! example "Outputs the default score, if no input score is provided"

    === "Parameters"

        ``` json title="defaultValue"
        1.0
        ```

    === "Input Values"

        ``` json
        [(none)]
        ```

    === "Returns"

        ``` json
        1.0
        ```

### Example from Date: Returns 0 if both dates are equal

* Input values:
  * Source: `[2003-03-01]`
  * Target: `[2003-03-01]`

* Returns: → `0.0`

!!! example "Returns 0 if both dates are equal"

    === "Input values"

        ``` json title="Source"
        [2003-03-01]
        ```
        ``` json title="Target"
        [2003-03-01]
        ```

    === "Returns"

        ``` json
        0.0
        ```

### Example from Camel Case: A sentence with several words is converted to a single word written in UpperCamelCase

* Parameters
  * *isDromedary*: `false`

* Input values:
  1. `[hello world]`

* Returns:

  → `[HelloWorld]`


### Example from Coalesce: 5

* Input values:
  1. `[]`
  2. `[first A, first B]`
  3. `[second]`

* Returns:

  → `[first A, first B]`

!!! example "Example 5"

    === "Input values"

        ``` json title="1."
        []
        ```
        ``` json title="2."
        [first A, first B]
        ```
        ``` json title="3."
        [second]
        ```

    === "Returns"

        ``` json
        [first A, first B]
        ```


### Example of Concatenate: 4

* Parameters
  * *glue*: `-`

* Input values:
  1. `[First]`
  2. `[Last]`

* Returns:

  → `[First-Last]`


### Example of Concatenate multiple values: 6

* Parameters
  * *glue*: `\n\t\\`

* Input values:
  1. `[a
	\b, c]`

* Returns:

  → `[a
	\b
	\c]`


!!! example "Example 5"

    === "Parameters"

        ``` json title="glue"
        \n\t\\
        ```

    === "Input values"

        ``` json title="1."
        [a
        \b, c]
        ```

    === "Returns"

        ``` json
        [a
        \b
        \c]
        ```

