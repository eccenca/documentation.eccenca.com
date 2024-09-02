---
tags:
    - Security
    - cmemc
---
# Access Conditions

## Introduction

Access Conditions specify access rights for users and groups to graphs and actions (1).
{ .annotate }

1.  Graphs identify specific Knowledge Graphs.
    Actions identify specific parts or components of the platform, such as the query catalog or the data integration system (Build).

Access Conditions are managed in a special system graph, so write access to this graph needs to be handled carefully.
The management of access conditions can be done either by using the browser based user interface or the command line based user interface (cmemc).

## Attributes of Access Conditions

In order to understand the different user interfaces to manage access conditions, it is crucial to understand what details can be described with a single access condition.
The following list describes the different attributes, a single access condition can have.
They are all optional except that a single access condition needs to provide at least one grant or has a dynamic access condition query.

### **Metadata**

- **Name** is a short and human readable text you can give to your access condition in order to identify them.

- **Description** is an optional and longer text you can add, to provide more context.

### Define **who** gets access

- Use **Requires account** to specify the user account, which is required by the access condition.
  If the account matches the account of a given request, this access condition is used to identify the grants for this request.
  Instead of an actual account, the following meta account can be used.

| Resource | Explanation |
| ---------| ------------|
| `urn:elds-backend-anonymous-user`| Represents the anonymous user account. You can use it in the **Requires account** field. |

- Use **Requires group** to specify the group, the account must be member of in order to match the access condition.
  If the account of a given request is member of this group, this access condition is used to identify the grants for this request.
  Instead of an actual group, the following meta group can be used.

| Resource | Explanation |
| ---------| ------------|
| `urn:elds-backend-public-group`| Represents the group which every user is member of (incl. anonymous users). You can use it in the *Requires group* field. |

!!! warning "Users and groups cannot have the same name"

    Since both user and group resource are represented in the same namespace in the internal graph representation, users and groups cannot have the same identifier.

### Define **what** grants are given

- **Allow reading graph** is a list of graph IRI to allow to read these graphs.
  Instead of an actual graph, the following meta graph can be used.

| Resource | Explanation |
| ---------| ------------|
| `urn:elds-backend-all-graphs`| Represents all RDF named graphs. You can use it in the *Allow reading graph* or *Allow writing graph* field.|

- **Allow writing graph** is a list of graph IRIs to allow to write these graphs.
  The grant to write to a graph implicitly grants to read the graph.
  Instead of an actual graph, the following meta graph can be used.

| Resource | Explanation |
| ---------| ------------|
| `urn:elds-backend-all-graphs`| Represents all RDF named graphs. You can use it in the *Allow reading graph* or *Allow writing graph* field.|

- **Allowed action** is a list of action IRI to allow to use the components or capabilities which are identified with this action.
  You can use the following actions identifier with this attribute.

| Resource | Explanation |
| ---------| ------------|
| `urn:elds-backend-actions-auth-access-control` | Represents the Authorization Management API (see the Developer Manual).|
| `urn:eccenca:di`| Represents the action needed to use the eccenca DataIntegration component of eccenca Corporate Memory.|
| `urn:eccenca:ThesaurusUserInterface`| Represents the action needed to use the Thesaurus Catalog as well as Thesaurus Project editing interface (needs access to specific thesaurus graphs as well).|
| `urn:eccenca:AccessInternalGraphs`| Represents the action needed to list Corporate Memory Internal graphs in the exploration tab.|
| `urn:eccenca:QueryUserInterface`| Represents the action needed to use the Query Catalog (needs access to query catalog graph as well).|
| `urn:eccenca:VocabularyUserInterface`| Represents the action needed to use the Vocabulary Catalog (needs access to specific vocabulary graphs as well).|
| `urn:eccenca:ExploreUserInterface`| Represents the action needed to use the Explore Tab (needs access to shape catalog graph as well).|

In addition to these attributes, you can use the following special attributes to grant partial access to the access conditions itself:

- **Graph pattern for granting read access** is a pattern to allow users to manage access conditions which grant read access to graphs identified by IRI matching the pattern.

- **Graph pattern for granting write access** is a pattern to allow users to manage access conditions which grant write access to graphs identified by IRI matching the pattern.

- **Pattern for granting actions** is a pattern to allow users to manage access conditions which grant action usage to action identified by IRI matching the pattern.

### Dynamic Conditions

Use this attribute to dynamically compute **who** get access on **which graphs**, based on background information from your Knowledge Graphs:

- **Dynamic access condition** is an attribute which requires a SPARQL Select query which returns the following projection variables: `user`, `group`, `readGraph`, `writeGraph`.

The following example query grants write access to all users which are described as creators (using Dublin Core) in the graph itself.

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX void: <http://rdfs.org/ns/void#>

SELECT  ?user ?group ?readGraph ?writeGraph
WHERE
{
  GRAPH ?writeGraph {
    ?writeGraph rdf:type void:Dataset .
    ?writeGraph dct:creator ?user .
  }
}
```

Given the following Knowledge Graph `https://example.org/my-data/`, the account `tester` will get access to it, because the IRI of the account is related to the graph.

``` turtle
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX void: <http://rdfs.org/ns/void#>

<https://example.org/my-data/>
  rdf:type void:Dataset ;
  rdfs:label "My Data"@en;
  dct:creator <http://eccenca.com/tester> .
```

!!! info "User and group namespace"

    The IRI identifier for users and groups need have the namespace `http://eccenca.com/`.
    If your data does not match this requirement, you can manipulate the IRIs with SPARQL functions on-the-fly.


## Using the web interface

The access control module can be selected in the **Admin** section of the left main menu of the **Explore** component.
After clicking it, you will see a screen similar to this:

<figure markdown>
![Access Control: List Access Conditions](24-1-access-condition-module-list.png)
<figcaption>Access Control: List Access Conditions</figcaption>
</figure>

You have two major application areas (tabs) here:

- In the **Manage** tab, you can view, edit, add and delete all access conditions, which are manageable by your account.
- In the **Review** tab, you can see the **effective rights** based on a selection of an account and groups.

### Manage access conditions

Use the following icon buttons for a specific action with a certain access condition:

- Use :material-eye-outline: to view an access condition.
- Use :material-pencil-outline: to edit an access condition.
- Use :material-trash-can-outline: to delete an access condition.

Use the **Create access condition** button to create a new access condition.

### Review access conditions

In the **Review** tab, you can see the **effective rights** based on a selection of an account and groups.
This allows for debugging your access condition system as a whole.
In order to see the rights select a user and / or group combination from the drop-down list on top (principal).
Then you will see a screen similar to this:

<figure markdown>
![Access Control: Review Access Conditions](24-1-access-condition-module-review.png)
<figcaption>Access Control: Review Access Conditions</figcaption>
</figure>

This screen is split into two main areas:

- First, the effective rights are listed, which summarize the resulting access rights.
    - The **Root access** field shows if the principal has root access.
    - The **Read all** and **Write all** fields show if the principal has read or write access to all graphs.
    - The **All actions are allowed** field shows if the principal has permission to execute all actions.
    - The **Allowed actions** field lists the actions the principal is allowed to execute.
    - The **Readable graphs** and **Writable graphs** fields list the graphs the principal is allowed to read or write.

- Second, the list of all access conditions which contributed to the effective access rights. This section allows to see which access conditions matched the principal and which access rights they grant.


## Using the command line interface (cmemc)

With [cmemc](../../../automate/cmemc-command-line-interface/index.md) you can use an additional command line based interface to manage access conditions.
This interface is primarily used for the automation of provisioning tasks.
The important command groups for managing principals and access conditions are:

- [`admin acl`](../../../automate/cmemc-command-line-interface/command-reference/admin/acl/index.md) - List, create, delete and modify and review access conditions.
- [`admin user`](../../../automate/cmemc-command-line-interface/command-reference/admin/user/index.md) - List, create, delete and modify user accounts.
- [`admin client`](../../../automate/cmemc-command-line-interface/command-reference/admin/client/index.md) - List client accounts, get or generate client account secrets.

The following session demonstrates how to create a new user, set a password and grant access to certain areas.


``` shell-session
∴ cmemc admin acl list
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ URI                        ┃ Name                              ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ :local-admins-group-rights ┃ Rights for the local-admins group ┃
┃ :local-user-group-rights   ┃ Rights for the local-users group  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

∴ cmemc admin user create tester
Creating user tester ... done

∴ cmemc admin user password tester
Changing password for account tester ...
New password:
Retype new password:
done

∴ cmemc admin acl create --id tester-rights --user tester \
    --action urn:eccenca:ExploreUserInterface \
    --read-graph urn:elds-backend-all-graphs
Creating access condition 'Condition for user: tester' ... done

∴ cmemc admin acl list
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ URI                        ┃ Name                              ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ :local-admins-group-rights ┃ Rights for the local-admins group ┃
┃ :local-user-group-rights   ┃ Rights for the local-users group  ┃
┃ :tester-rights             ┃ Condition for user: tester        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

