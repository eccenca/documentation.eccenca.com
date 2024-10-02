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
