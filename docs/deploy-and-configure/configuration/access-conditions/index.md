---
tags:
    - Security
    - cmemc
---
# Access Conditions

!!! warning "Users and groups cannot have the same name"

    Since both user and group resources use the same IRI prefix in DataPlatform, users and groups cannot have the same name.

## Introduction

The Access control module shows the list of all access conditions manageable by your account.
Access conditions specify access rights for users and groups to graphs and actions.
To open the Access control, open the menu :fontawesome-solid-ellipsis-vertical: in the Module bar and click Access control.

## Access conditions

The main window shows the list of all access conditions manageable by your account.
Access conditions specify access rights for users and groups to graphs and actions.

Click a specific condition to get an expanded view with more details.

<figure markdown>
![Expanded view of an access condition](22-1-expanded-access-condition.png)
<figcaption>Expanded view of an access condition</figcaption>
</figure>

## Adding a new condition

To add a new access condition:

-   Click the context menu :fontawesome-solid-ellipsis-vertical: in the upper right
-   Select "Create access condition"
-   In the dialog box, enter the new access condition rule as needed. Each access condition can have a **Name** and a **Description** as well as conditions and grants for actions and graphs.

???+ note
    The application uses a set of specific URIs with a precise meaning as listed below:

| Resource                                       | Explanation                                                                                                                                                                                                    |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `urn:elds-backend-all-graphs`                  | Represents all RDF named graphs. You can use it in the Allow reading graph or Allow writing graph field.                                                                                                       |
| `urn:elds-backend-all-actions`                 | Represents all actions. You can use it in the **Allowed actions** field.                                                                                                                                       |
| `urn:elds-backend-public-group`                | Represents the group which every user is member of (incl. anonymous users). You can use it in the Requires group field.                                                                                        |
| `urn:elds-backend-anonymous-user`              | Represents the anonymous user account. You can use it in the **Requires account** field.                                                                                                                       |                                                                                     |
| `urn:elds-backend-actions-auth-access-control` | Represents the Authorization management API (see the Developer Manual). You can use it in the Allowed actions field.                                                                                           |
| `urn:eccenca:di`                               | Represents the action needed to use the eccenca DataIntegration component of eccenca Corporate Memory. You can use it in the **Allowed actions** field.                                                            |
| `urn:eccenca:ThesaurusUserInterface`           | Represents the action needed to use the Thesaurus Catalog as well as Thesaurus Project editing interface (needs access to specific thesaurus graphs as well). You can use it in the **Allowed actions** field. |
| `urn:eccenca:AccessInternalGraphs`             | Represents the action needed to list Corporate Memory Internal graphs in the exploration tab. You can use it in the **Allowed actions** field.                                                                 |
| `urn:eccenca:QueryUserInterface`               | Represents the action needed to use the Query Catalog (needs access to catalog graph as well if changes should be allowed). You can use it in the **Allowed actions** field.                                   |
| `urn:eccenca:VocabularyUserInterface`          | Represents the action needed to use the Vocabulary Catalog (needs access to specific vocabulary graphs as well). You can use it in the **Allowed actions** field.                                              |
| `urn:eccenca:ExploreUserInterface`             | Represents the action needed to use the Explore Tab (needs access to at least one graph as well). You can use it in the **Allowed actions** field.                                                             |

Click CREATE to create the new condition or abort your action with CANCEL.

<figure markdown>
![Create a new condition](22-1-new-access-condition.png)
<figcaption>Create a new condition</figcaption>
</figure>

## Edit an existing condition

In the expanded view of an access condition, click DELETE to remove the access condition or EDIT to apply changes.

Click on SAVE to apply your changes or discard them with CANCEL.

## Adding Access Conditions with cmemc

In addition to the Access Control module you can add the access conditions directly to the triple store.
In this case, the access conditions need to be defined in a Turtle file, for example:

```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix eccurn: <urn:eccenca:> .
@prefix ecc: <http://eccenca.com/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix eccauth: <https://vocab.eccenca.com/auth/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ecc:f7f3b9c5-4e94-4e7f-a14b-15e39ae046ed
    dcterms:created "2020-06-12T11:10:19Z"^^xsd:dateTime ;
    dcterms:creator ecc:admin ;
    a eccauth:AccessCondition ;
    rdfs:comment "single access condition which describes all rights for users in the local-admins group" ;
    rdfs:label "Active: access rights of all users of the local-admins group" ;
    eccauth:allowedAction eccurn:AccessInternalGraphs, eccurn:QueryUserInterface, eccurn:ThesaurusUserInterface, eccurn:VocabularyUserInterface, eccurn:di, <urn:elds-backend-actions-auth-access-control> ;
    eccauth:requiresGroup ecc:local-admins ;
    eccauth:writeGraph <urn:elds-backend-all-graphs> .

ecc:5318ffd4-4ca7-46bb-8e0c-8a910376c6b9
    dcterms:created "2020-06-12T11:10:32Z"^^xsd:dateTime ;
    dcterms:creator ecc:admin ;
    a eccauth:AccessCondition ;
    rdfs:comment "single access conditions which describes the rights of users from the local-users group" ;
    rdfs:label "Active: access rights of all users of the local-users group" ;
    eccauth:allowedAction eccurn:ExploreUserInterface, eccurn:QueryUserInterface, eccurn:ThesaurusUserInterface, eccurn:VocabularyUserInterface, eccurn:di ;
    eccauth:requiresGroup ecc:local-users ;
    eccauth:writeGraph <urn:elds-backend-all-graphs> .
```

In this example, we have listed default access conditions for the [`docker compose` based orchestration](../docker-orchestration/index.md).

The file defines two access conditions.
The `eccauth:allowedActions` correspond to the URIs listed in the table above.
Both access conditions allow the corresponding users (admins or non-admins) to write to all graphs.

You can define several access conditions for the same group.

When you are finished with creating your access conditions Turtle file, you can add it directly to the `urn:elds-backend-access-conditions-graph` graph (defined in [DataPlatform configuration](./../dataplatform/index.md)).

With [cmemc](../../../automate/cmemc-command-line-interface/index.md) you can do this with the following command line:

``` shell-session
$ cmemc -c my-cmem-instance graph import --replace access-conditions.ttl urn:elds-backend-access-conditions-graph
Import graph 1/1: urn:elds-backend-access-conditions-graph from access-conditions.ttl ... done
```
