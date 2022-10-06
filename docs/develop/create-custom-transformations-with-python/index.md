---
status: deprecated
tags:
    - Python
---
# Create Custom Transformations with Python

???+ caution
    This section describes the obsolete Python 2 plugin system. We recommend to migrate to the new Python 3 plugin system: [Python Plugins](../python-plugins/index.md)

## Introduction

Beside the fact that there are over 180 built-in operators available for your data transformations, there will be the moment where you need a new special operator to solve a specific problem which can't be solved with the built-ins or which is just easier to solve when you simply program it.This page gives an overview on the Script Transform Operator and how to use it to create Python based custom transformations.

## General Working Model

The python script operator has two parameters: A multi-text field for the script and a function field for the name of the function to be executed. The operator performs the following two steps:

- first, it loads the script
- then, it executes the function for each "row" of the transformation.

Each input value is always given as an array of strings (such as ["Eve", "Alice", "Bob"], more specifically - as an instance of [org.python.core.PyArray](https://www.javadoc.io/doc/org.python/jython-standalone/2.7-b2/org/python/core/PyArray.html)). If there are no values for the current iteration, an empty array is given. The number of input arrays (of strings) depends on the number of incoming connections in the transformation operator. These connections are ordered, means the first connected building block delivers parameter one (as an array of strings), the second building block delivers parameter two (as an array of strings), etc.

In the same way as the input parameters, the result value should be a list of strings. The operator will try its best to map whatever is returned to a proper list of strings but this could fail, so don't try it too hard ...

## Preliminaries

### Enabling the script operators

Because the script operators allow potentially unsafe operations (such as writing to the file system), they are disabled by default. In order to use those plugins, they need to be enabled explicitly in the config:

```bash
pluginRegistry.plugins.python2Script.enabled = true
```

The following script operators are available:

- `python2Script`: Python 2 transform operator.
- `scalaScript`: Scala transform operator.
- `script`: Scala script operator to be used in workflows.

### Using Python libraries

External python libraries can be configured and will be loaded from the the following folder by default:

```hocow
com.eccenca.di.scripting.transformer.Python2ScriptTransformer = {
  modulePath = ${elds.home}"/etc/dataintegration/pythonModules/"
}
```

The configured modulePath will be added to the Python `sys.path`.

## Parameter Validation

Some parameter value validation should be done inside the defined function. This includes

- test how many strings are in the list
- test if these strings have a specific format

## Error Handling and Logging

Syntax errors are instantly shown in the transformation editor while execution errors or exceptions are shown in the evaluation and execution report. Both type of errors are also logged.

In addition to error logging, the function can create print-output which is added to the logging as well.

## Example: Days between Two Dates

The following well commented and very verbose code example calculates the difference between two dates and returns the number of dates as a result:

```py title="dates_difference.py  " linenums="1"

"""Example transform operators for data integration."""

# imports can be done normally in the script, but only from the standard lib

import array
from datetime import datetime


def days_between_dates(first_input, second_input):
    """Compare two dates and return number of days between them.

    The date values need to be in the form  YYYY-MM-DD
    """
    # check for arrays (actually not needed since DI will always give arrays)
    # more specifically: the type of inputs is org.python.core.PyArray
    if not isinstance(first_input, array.array):
        raise ValueError(
            "First input should be a list of strings, but was {}."
            .format(type(first_input))
        )
    if not isinstance(second_input, array.array):
        raise ValueError(
            "First input should be a list of strings, but was {}."
            .format(type(second_input))
        )

    # check list element count
    if len(first_input) != 1:
        raise ValueError(
            "First input should be exactly one value (but had {} values)"
            .format(len(first_input))
        )
    if len(second_input) != 1:
        raise ValueError(
            "Second input should be exactly one value (but had {} values)"
            .format(len(second_input))
        )

    first_input = str(first_input[0])
    second_input = str(second_input[0])
    date_format = "%Y-%m-%d"

    # create dates from strings
    try:
        first_date = datetime.strptime(first_input, date_format)
    except ValueError:
        raise ValueError(
            "Error: First input date has wrong format. "
            "Must be 'yyyy-mm-dd' (ex: '2016-10-01')."
        )
    try:
        second_date = datetime.strptime(second_input, date_format)
    except ValueError:
        raise ValueError(
            "Error: First input date has wrong format. "
            "Must be 'yyyy-mm-dd' (ex: '2016-10-01')."
        )

    # calculate and return delta - casted to a list of one string
    return [str((second_date - first_date).days)]

```

Based on this example the following pytest test suite is "green" (given here for clarification of the operator behaviour):

```py title="test_dates_difference.py  " linenums="1"

import pytest

from transform_operators import days_between_dates


def test_valid_inputs():
    """test valid inputs"""
    assert days_between_dates(["2022-05-02"], ["2022-05-01"]) == ["-1"]
    assert days_between_dates(["2022-05-01"], ["2022-05-22"]) == ["21"]
    assert days_between_dates(["2022-01-01"], ["2021-12-31"]) == ["-1"]


def test_missing_inputs():
    """test missing inputs"""
    with pytest.raises(TypeError):
        days_between_dates(["2022-05-02"])
    with pytest.raises(ValueError):
        days_between_dates([], ["2022-05-02"])
    with pytest.raises(ValueError):
        days_between_dates(["2022-05-02"], [])


def test_invalid_inputs():
    """invalid test inputs"""
    with pytest.raises(ValueError):
        days_between_dates(["2022-05-02"], ["..."])
    with pytest.raises(ValueError):
        days_between_dates(["2022-05-02"], "...")
    with pytest.raises(ValueError):
        days_between_dates(["..."], ["2022-05-02"])
    with pytest.raises(ValueError):
        days_between_dates("2022-05-02", "...")
    with pytest.raises(TypeError):
        days_between_dates(10, 20)
```

This well tested operator can now be used in your transformation (left: the transformation flow, right: the evaluation report)

![transformation-plugin-example](21-1-PythonOperatorExample.png)

## Special environment variables

A number of useful variables are injected and can be accessed from the Python script as follows:

```py title="example_inject_env.py  " linenums="1"
from os import environ as env
env['VARIABLE_NAME']
```

The following variables are available:

- **CMEM_BASE_URI**: The base URI of the current CorporateMemory deployment.
- **OAUTH_ACCESS_TOKEN**: The current super user token. Note that this is only available, if a super user is configured.
- **OAUTH_GRANT_TYPE**: The corresponding OAuth grant type. Set to: `prefetched_token`
