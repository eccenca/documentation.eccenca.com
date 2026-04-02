---
icon: material/language-python
tags:
    - API
    - Python
---
# cmempy - Python API

## Introduction

cmempy is a Python API wrapper around the eccenca Corporate Memory HTTP APIs which can be used to rapidly script processes which interact with Corporate Memory.
cmempy is also the underlying Python module which powers the [cmemc - Command Line Interface](../../automate/cmemc-command-line-interface/index.md).

## Installation

cmempy is published as an Apache 2 licensed open source python package at [pypi.org](https://pypi.org/project/cmem-cmempy/), hence you are able to install it with a simple pip command:

```shell
pip install cmem-cmempy
```

## Configure a Connection

The used Corporate Memory connection is configured by providing environment variables similar to [cmemc](../../automate/cmemc-command-line-interface/index.md) ([Environment based Configuration](../../automate/cmemc-command-line-interface/configuration/environment-based-configuration/index.md)).

These environment variables can be created and changed in your code or used from the process which executes your python code (e.g. your shell).
If you have a working cmemc [file based configuration](../../automate/cmemc-command-line-interface/configuration/file-based-configuration/index.md) setup already you can export the environment to your shell using [cmemc config eval](../../automate/cmemc-command-line-interface/command-reference/index.md).

The following table lists all processed environment variables:

| Variable            | Description                                           | Default Value                                                |
| ------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| CMEM_BASE_URI       | Base URL of your Corporate Memory                     | <http://docker.localhost>                                      |
| DI_API_ENDPOINT     | Build (Data Integration) API endpoint                 | CMEM_BASE_URI/dataintegration                                |
| DP_API_ENDPOINT     | Explore backend API endpoint                          | CMEM_BASE_URI/dataplatform                                   |
| OAUTH_TOKEN_URI     | OAuth 2.0 Token endpoint                              | CMEM_BASE_URI/auth/realms/cmem/protocol/openid-connect/token |
| OAUTH_GRANT_TYPE    | OAuth 2.0 grant type (password or client_credentials) | client_credentials                                           |
| OAUTH_USER          | Username to retrieve the token                        | admin                                                        |
| OAUTH_PASSWORD      | Password to retrieve the token                        | secret                                                       |
| OAUTH_CLIENT_ID     | OAuth 2.0 client id                                   | cmem-service-account                                         |
| OAUTH_CLIENT_SECRET | OAuth 2.0 client secret                               | secret                                                       |
| SSL_VERIFY          | Verify SSL certs for API requestsv                    | True                                                         |
| REQUESTS_CA_BUNDLE  | Path to the CA Bundle file (.pem)                     | Internal path to included CA bundle                          |

## Commented Example

Here is a commented code example how to configure and use cmempy.

The example demonstrates, how to execute SPARQL queries via Explore backend, as well as how to work with the Build (DataIntegration) workspace and retrieve workflow status information:

```python title="example_usage.py"
"""Basic example, how to use cmempy"""

from os import environ

from cmem.cmempy.workspace.projects.project import get_projects
from cmem.cmempy.workflow import get_workflows
from cmem.cmempy.workspace.activities.taskactivity import get_activity_status
from cmem.cmempy.queries import SparqlQuery

# setup the environment for the connection to Corporate Memory
environ["CMEM_BASE_URI"] = "http://docker.local"
environ["OAUTH_GRANT_TYPE"] = "client_credentials"
environ["OAUTH_CLIENT_ID"] = "cmem-service-account"
environ["OAUTH_CLIENT_SECRET"] = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# this query simply lists 5 resource subjects from the triple store
QUERY_TEXT = "SELECT DISTINCT ?s WHERE {?s ?p ?o} LIMIT 5"

# the default result is a JSON structure according to the W3C standard
# seeAlso: https://www.w3.org/TR/sparql11-results-json/
results = SparqlQuery(QUERY_TEXT).get_results()
print(results)

# loop over project descriptions
for project in get_projects():
    project_id = project["name"]
    print("Project: {}:".format(project_id))

    # loop over workflow ids for a project
    for workflow_id in get_workflows(project_id):
        # get the status object of a specific workflow
        status = get_activity_status(project_id, workflow_id)
        message = status["message"]
        print("- Workflow: {} ({}):".format(workflow_id, message))
```

Starting this script should result in an output similar to this:

``` shell-session
$ python example_usage.py
{
  "head": {
    "vars": [ "s" ]
  } ,
  "results": {
    "bindings": [
      {
        "s": { "type": "uri" , "value": "https://vocab.eccenca.com/dsm/" }
      } ,
      {
        "s": { "type": "uri" , "value": "https://vocab.eccenca.com/dsm/ThesaurusProject" }
      } ,
      {
        "s": { "type": "uri" , "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#" }
      } ,
      {
        "s": { "type": "uri" , "value": "http://www.w3.org/2002/07/owl#" }
      } ,
      {
        "s": { "type": "uri" , "value": "http://www.w3.org/2000/01/rdf-schema#" }
      }
    ]
  }
}

Project: cmem:
- Workflow: my-workflow (Idle):
```
