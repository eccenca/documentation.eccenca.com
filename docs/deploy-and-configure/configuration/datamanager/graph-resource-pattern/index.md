---
#icon: octicons/cross-reference-24
tags:
  - Reference
---

# Graph Resource Pattern

This chapter specifies the JSON object used to provide a Business Knowledge Editor search (query) configuration.
The `GraphResourcePattern` is part of an optional advanced configuration of the Business Knowledge Editor module.
It can be used to provide search filter / facets in order to tailor the search results presented to the end user.

The `GraphResourcePattern` object reference is provided in different ways depending on your preferences:

=== "Type Script"

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
=== "JSON Schema"

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

=== "GraphResourcePattern"

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

A _human friendly_ representation can be generatled using [json-schema-for-humans](https://json-schema-viewer.vercel.app/view?url=https%3A%2F%2Fdev.documentation.eccenca.com%2Fexplore-and-author%2Feasynav-module%2FGraphResourcePattern%2Fschema.json&description_is_markdown=on&expand_buttons=on&show_breadcrumbs=on&with_footer=on&template_name=js#pathFilters).

A valid configuration must use a `subjectVarName` called `resource`. This is the binding that yields results.

This configuration produces the following result, it only shows results where:

-   `resource` is of type `http://example.com/vocab/Company`
-   a `subResource` exists which is related to `resource` via the `http://example.com/vocab/hasParent` property
