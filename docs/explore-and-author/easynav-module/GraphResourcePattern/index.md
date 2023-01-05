---
icon: octicons/cross-reference-24
tags:
  - Reference
---

# GraphResourcePattern

This chapter specifies the JSON object used to provide a EasyNav Search (query) configuration.
The `GraphResourcePattern` is part of an optional advanced configuration of the EasyNav module.
It can be used to provide search filter / facets in order to tailor the search results presented to the end user.

The `GraphResourcePattern` object reference is provided in different ways depending on your preferences:

??? example "Type Script"

    ```ts
    export type GraphResourcePattern = {
        paths: Path[];
        pathFilters?: PathVariableFilter[];
    };

    export type Path = {
        subjectVarName?: string;
        objectVarName?: string;
        inverted: boolean;
        predicate: string;
    };

    export type PathVariableFilter = {
        varname?: string;
        varIsAnyOneOfResource?: string[];
        varIsAnyOneOfLiteral?: Literal[];
        isNoneOfResource?: string[];
        isNoneOfLiteral?: Literal[];
        literalFilters?: PathVariableLiteralFilter[];
    };

    export type Literal = {
        value: string;
        lang?: string;
        datatype?: string;
    };

    export type PathVariableLiteralFilter = {
        operation:
            | "GreaterThan"
            | "LessThan"
            | "GreaterEqualsThan"
            | "LessEqualThan"
            | "NotEquals"
            | "Contains"
            | "Regex";
        value: Literal;
    };
    ```

??? example "JSON Schema"

    ```json
    {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title" : "GraphResourcePattern",
        "description" : "Description of the GraphResourcePattern JSON data structure",
        "properties": {
            "pathFilters": {
                "items": {
                    "properties": {
                        "isNoneOfLiteral": {
                            "items": {
                                "properties": {
                                    "datatype": {
                                        "type": "string"
                                    },
                                    "lang": {
                                        "type": "string"
                                    },
                                    "value": {
                                        "type": "string"
                                    }
                                },
                                "type": "object"
                            },
                            "type": "array"
                        },
                        "isNoneOfResource": {
                            "items": {
                                "type": "string"
                            },
                            "type": "array"
                        },
                        "literalFilters": {
                            "items": {
                                "properties": {
                                    "operation": {
                                        "enum": [
                                            "Contains",
                                            "GreaterEqualsThan",
                                            "GreaterThan",
                                            "LessEqualThan",
                                            "LessThan",
                                            "NotEquals",
                                            "Regex"
                                        ],
                                        "type": "string"
                                    },
                                    "value": {
                                        "properties": {
                                            "datatype": {
                                                "type": "string"
                                            },
                                            "lang": {
                                                "type": "string"
                                            },
                                            "value": {
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    }
                                },
                                "type": "object"
                            },
                            "type": "array"
                        },
                        "varIsAnyOneOfLiteral": {
                            "items": {
                                "properties": {
                                    "datatype": {
                                        "type": "string"
                                    },
                                    "lang": {
                                        "type": "string"
                                    },
                                    "value": {
                                        "type": "string"
                                    }
                                },
                                "type": "object"
                            },
                            "type": "array"
                        },
                        "varIsAnyOneOfResource": {
                            "items": {
                                "type": "string"
                            },
                            "type": "array"
                        },
                        "varname": {
                            "type": "string"
                        }
                    },
                    "type": "object"
                },
                "type": "array"
            },
            "paths": {
                "items": {
                    "properties": {
                        "inverted": {
                            "type": "boolean"
                        },
                        "objectVarName": {
                            "type": "string"
                        },
                        "predicate": {
                            "type": "string"
                        },
                        "subjectVarName": {
                            "type": "string"
                        }
                    },
                    "type": "object"
                },
                "type": "array"
            }
        },
        "type": "object"
    }
    ```

??? example "json-schema-for-humans"

    The following section are a _human friendly_ representation generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

    **Title:** GraphResourcePattern

    |                           |                                                         |
    | ------------------------- | ------------------------------------------------------- |
    | **Type**                  | `object`                                                |
    | **Required**              | No                                                      |
    | **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
    | **Defined in**            | #/definitions/GraphResourcePattern                      |

    **Description:** Description of the GraphResourcePattern JSON data structure

    | Property                       | Pattern | Type  | Deprecated | Definition | Title/Description |
    | ------------------------------ | ------- | ----- | ---------- | ---------- | ----------------- |
    | - [pathFilters](#pathFilters ) | No      | array | No         | -          | -                 |
    | + [paths](#paths )             | No      | array | No         | -          | -                 |

    ## <a name="pathFilters"></a>pathFilters

    |              |         |
    | ------------ | ------- |
    | **Type**     | `array` |
    | **Required** | No      |

    |                      | Array restrictions |
    | -------------------- | ------------------ |
    | **Min items**        | N/A                |
    | **Max items**        | N/A                |
    | **Items unicity**    | False              |
    | **Additional items** | False              |
    | **Tuple validation** | See below          |

    | Each item of this array must be          | Description |
    | ---------------------------------------- | ----------- |
    | [PathVariableFilter](#pathFilters_items) | -           |

    ### <a name="autogenerated_heading_2"></a>PathVariableFilter

    |                           |                                                         |
    | ------------------------- | ------------------------------------------------------- |
    | **Type**                  | `object`                                                |
    | **Required**              | No                                                      |
    | **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
    | **Defined in**            | #/definitions/PathVariableFilter                        |

    | Property                                                             | Pattern | Type            | Deprecated | Definition | Title/Description |
    | -------------------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
    | - [isNoneOfLiteral](#pathFilters_items_isNoneOfLiteral )             | No      | array           | No         | -          | -                 |
    | - [isNoneOfResource](#pathFilters_items_isNoneOfResource )           | No      | array of string | No         | -          | -                 |
    | - [literalFilters](#pathFilters_items_literalFilters )               | No      | array           | No         | -          | -                 |
    | - [varIsAnyOneOfLiteral](#pathFilters_items_varIsAnyOneOfLiteral )   | No      | array           | No         | -          | -                 |
    | - [varIsAnyOneOfResource](#pathFilters_items_varIsAnyOneOfResource ) | No      | array of string | No         | -          | -                 |
    | - [varname](#pathFilters_items_varname )                             | No      | string          | No         | -          | -                 |

    #### <a name="pathFilters_items_isNoneOfLiteral"></a>isNoneOfLiteral

    |              |         |
    | ------------ | ------- |
    | **Type**     | `array` |
    | **Required** | No      |

    |                      | Array restrictions |
    | -------------------- | ------------------ |
    | **Min items**        | N/A                |
    | **Max items**        | N/A                |
    | **Items unicity**    | False              |
    | **Additional items** | False              |
    | **Tuple validation** | See below          |

    | Each item of this array must be                     | Description |
    | --------------------------------------------------- | ----------- |
    | [Literal](#pathFilters_items_isNoneOfLiteral_items) | -           |

    ##### <a name="autogenerated_heading_3"></a>Literal

    |                           |                                                         |
    | ------------------------- | ------------------------------------------------------- |
    | **Type**                  | `object`                                                |
    | **Required**              | No                                                      |
    | **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
    | **Defined in**            | #/definitions/Literal                                   |

    | Property                                                         | Pattern | Type   | Deprecated | Definition | Title/Description |
    | ---------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
    | - [datatype](#pathFilters_items_isNoneOfLiteral_items_datatype ) | No      | string | No         | -          | -                 |
    | - [lang](#pathFilters_items_isNoneOfLiteral_items_lang )         | No      | string | No         | -          | -                 |
    | + [value](#pathFilters_items_isNoneOfLiteral_items_value )       | No      | string | No         | -          | -                 |

    ###### <a name="pathFilters_items_isNoneOfLiteral_items_datatype"></a>datatype

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | No       |

    ###### <a name="pathFilters_items_isNoneOfLiteral_items_lang"></a>lang

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | No       |

    ###### <a name="pathFilters_items_isNoneOfLiteral_items_value"></a>value

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | Yes      |

    #### <a name="pathFilters_items_isNoneOfResource"></a>isNoneOfResource

    |              |                   |
    | ------------ | ----------------- |
    | **Type**     | `array of string` |
    | **Required** | No                |

    |                      | Array restrictions |
    | -------------------- | ------------------ |
    | **Min items**        | N/A                |
    | **Max items**        | N/A                |
    | **Items unicity**    | False              |
    | **Additional items** | False              |
    | **Tuple validation** | See below          |

    | Each item of this array must be                                     | Description |
    | ------------------------------------------------------------------- | ----------- |
    | [isNoneOfResource items](#pathFilters_items_isNoneOfResource_items) | -           |

    ##### <a name="autogenerated_heading_4"></a>isNoneOfResource items

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | No       |

    #### <a name="pathFilters_items_literalFilters"></a>literalFilters

    |              |         |
    | ------------ | ------- |
    | **Type**     | `array` |
    | **Required** | No      |

    |                      | Array restrictions |
    | -------------------- | ------------------ |
    | **Min items**        | N/A                |
    | **Max items**        | N/A                |
    | **Items unicity**    | False              |
    | **Additional items** | False              |
    | **Tuple validation** | See below          |

    | Each item of this array must be                                      | Description |
    | -------------------------------------------------------------------- | ----------- |
    | [PathVariableLiteralFilter](#pathFilters_items_literalFilters_items) | -           |

    ##### <a name="autogenerated_heading_5"></a>PathVariableLiteralFilter

    |                           |                                                         |
    | ------------------------- | ------------------------------------------------------- |
    | **Type**                  | `object`                                                |
    | **Required**              | No                                                      |
    | **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
    | **Defined in**            | #/definitions/PathVariableLiteralFilter                 |

    | Property                                                          | Pattern | Type             | Deprecated | Definition                                                                                   | Title/Description |
    | ----------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------------------------------- | ----------------- |
    | + [operation](#pathFilters_items_literalFilters_items_operation ) | No      | enum (of string) | No         | -                                                                                            | -                 |
    | + [value](#pathFilters_items_literalFilters_items_value )         | No      | object           | No         | Same as [pathFilters_items_isNoneOfLiteral_items](#pathFilters_items_isNoneOfLiteral_items ) | -                 |

    ###### <a name="pathFilters_items_literalFilters_items_operation"></a>operation

    |              |                    |
    | ------------ | ------------------ |
    | **Type**     | `enum (of string)` |
    | **Required** | Yes                |

    Must be one of:

    *   "GreaterThan"
    *   "LessThan"
    *   "GreaterEqualsThan"
    *   "LessEqualThan"
    *   "NotEquals"
    *   "Contains"
    *   "Regex"

    ###### <a name="pathFilters_items_literalFilters_items_value"></a>value

    |                           |                                                                                     |
    | ------------------------- | ----------------------------------------------------------------------------------- |
    | **Type**                  | `object`                                                                            |
    | **Required**              | Yes                                                                                 |
    | **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.")                             |
    | **Same definition as**    | [pathFilters_items_isNoneOfLiteral_items](#pathFilters_items_isNoneOfLiteral_items) |

    #### <a name="pathFilters_items_varIsAnyOneOfLiteral"></a>varIsAnyOneOfLiteral

    |              |         |
    | ------------ | ------- |
    | **Type**     | `array` |
    | **Required** | No      |

    |                      | Array restrictions |
    | -------------------- | ------------------ |
    | **Min items**        | N/A                |
    | **Max items**        | N/A                |
    | **Items unicity**    | False              |
    | **Additional items** | False              |
    | **Tuple validation** | See below          |

    | Each item of this array must be                          | Description |
    | -------------------------------------------------------- | ----------- |
    | [Literal](#pathFilters_items_varIsAnyOneOfLiteral_items) | -           |

    ##### <a name="autogenerated_heading_6"></a>Literal

    |                           |                                                                                     |
    | ------------------------- | ----------------------------------------------------------------------------------- |
    | **Type**                  | `object`                                                                            |
    | **Required**              | No                                                                                  |
    | **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.")                             |
    | **Same definition as**    | [pathFilters_items_isNoneOfLiteral_items](#pathFilters_items_isNoneOfLiteral_items) |

    #### <a name="pathFilters_items_varIsAnyOneOfResource"></a>varIsAnyOneOfResource

    |              |                   |
    | ------------ | ----------------- |
    | **Type**     | `array of string` |
    | **Required** | No                |

    |                      | Array restrictions |
    | -------------------- | ------------------ |
    | **Min items**        | N/A                |
    | **Max items**        | N/A                |
    | **Items unicity**    | False              |
    | **Additional items** | False              |
    | **Tuple validation** | See below          |

    | Each item of this array must be                                               | Description |
    | ----------------------------------------------------------------------------- | ----------- |
    | [varIsAnyOneOfResource items](#pathFilters_items_varIsAnyOneOfResource_items) | -           |

    ##### <a name="autogenerated_heading_7"></a>varIsAnyOneOfResource items

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | No       |

    #### <a name="pathFilters_items_varname"></a>varname

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | No       |

    ## <a name="paths"></a>paths

    |              |         |
    | ------------ | ------- |
    | **Type**     | `array` |
    | **Required** | Yes     |

    |                      | Array restrictions |
    | -------------------- | ------------------ |
    | **Min items**        | N/A                |
    | **Max items**        | N/A                |
    | **Items unicity**    | False              |
    | **Additional items** | False              |
    | **Tuple validation** | See below          |

    | Each item of this array must be | Description |
    | ------------------------------- | ----------- |
    | [Path](#paths_items)            | -           |

    ### <a name="autogenerated_heading_8"></a>Path

    |                           |                                                         |
    | ------------------------- | ------------------------------------------------------- |
    | **Type**                  | `object`                                                |
    | **Required**              | No                                                      |
    | **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
    | **Defined in**            | #/definitions/Path                                      |

    | Property                                         | Pattern | Type    | Deprecated | Definition | Title/Description |
    | ------------------------------------------------ | ------- | ------- | ---------- | ---------- | ----------------- |
    | + [inverted](#paths_items_inverted )             | No      | boolean | No         | -          | -                 |
    | - [objectVarName](#paths_items_objectVarName )   | No      | string  | No         | -          | -                 |
    | + [predicate](#paths_items_predicate )           | No      | string  | No         | -          | -                 |
    | - [subjectVarName](#paths_items_subjectVarName ) | No      | string  | No         | -          | -                 |

    #### <a name="paths_items_inverted"></a>inverted

    |              |           |
    | ------------ | --------- |
    | **Type**     | `boolean` |
    | **Required** | Yes       |

    #### <a name="paths_items_objectVarName"></a>objectVarName

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | No       |

    #### <a name="paths_items_predicate"></a>predicate

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | Yes      |

    #### <a name="paths_items_subjectVarName"></a>subjectVarName

    |              |          |
    | ------------ | -------- |
    | **Type**     | `string` |
    | **Required** | No       |

    ----------------------------------------------------------------------------------------------------------------------------
    Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2022-11-10 at 21:15:54 +0100

An concrete example object is shown here:

!!! example "Example `GraphResourcePattern`"

    ```json
    {
        "paths": [
            {
                "subjectVarName": "subResource",
                "objectVarName": "resource",
                "predicate": "http://example.com/vocab/hasParent"
            },
            {
                "subjectVarName": "resource",
                "predicate": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
                "objectVarName": "class"
            }
        ],
        "pathFilters": [
            {
                "varname": "class",
                "varIsAnyOneOfResource": [
                    "http://example.com/vocab/Company"
                ]
            }
        ]
    }
    ```

A valid configuration must use a `subjectVarName` called `resource`. This is the binding that yields results.

This configuration produces the following result, it only shows results where:

-   `resource` is of type `http://example.com/vocab/Company`
-   a `subResource` exists which is related to `resource` via the `http://example.com/vocab/hasParent` property
