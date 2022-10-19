# System Architecture

This section describes the general system architecture of eccenca Corporate Memory and its components.

![cmem-System-Architecture](22-1-cmem-System-Architecture.png)

eccenca Corporate Memory consists of five core components:

- (2) [eccenca DataIntegration](../configuration/dataintegration/index.md)
- (3) [eccenca DataManager](../configuration/datamanager/index.md),
- (4) [eccenca DataPlatform](../configuration/dataplatform/index.md),
- (8) [Keycloak](../configuration/keycloak/index.md), and
- (12) [cmemc (Corporate Memory Control)](../../automate/cmemc-command-line-interface/index.md)

DataIntegration (2) is a Corporate Memory component which enables integration of multiple databases into a single consistent knowledge graph. Datasets in their original format are mapped and linked to RDF schemata and then linked to and persisted into a knowledge graph. The data integration is performed semi-automatically based on domain-specific integration rules and vocabularies (OWL ontologies). Corporate Memory supports multiple kinds of source integration data sources (6) such as SQL databases or files of different formats. These files can be processed with DataIntegration either locally or on a remote Spark cluster (7).

DataManager (3) is a single-page JavaScript application which enables creating and managing knowledge graphs based on established W3C standards. It is a generic data browser suitable to edit, explore and query the created knowledge graph. DataManager provides convenient options to create specific data views by using [Shapes Constraint Language](https://www.w3.org/TR/shacl/) (SHACL).

DataPlatform (4) is a semantic middleware application which provides a unified access to semantic graph data. Additionally, DataPlatform manages authorization of the users according to the access control lists defined in the Triple Store. The knowledge graph is stored in a triple store (5) connected to DataPlatform. This can either be a physical store like [Complexible Stardog](https://www.stardog.com/docs/), [GraphDB](http://graphdb.ontotext.com/), [Virtuoso](https://virtuoso.openlinksw.com/) or a remotely accessible SPARQL 1.1 compliant HTTP endpoint.

Keycloak (8) provides authentication. Keycloak can act as an authentication broker for already existing, external OpenId Connect or SAML infrastructures (9). In addition to that, Keycloak supports a wide variety of internal user management configuration scenarios and the option to connect to an external LDAP server for user and group synchronization (10). Keycloak uses the embedded Java-based relational database H2 as a default to store its configuration data. However, it is highly recommended to [use a relational database](https://www.keycloak.org/server/db) (11) for production use instead. Refer to the [Keycloak manual](https://www.keycloak.org/guides#server) for further information on possible setups.

[cmemc](../../automate/cmemc-command-line-interface/index.md) (12) (Corporate Memory Control) is the eccenca Corporate Memory Command Line Interface (CLI). cmemc is intended for system administrators and Linked Data Experts who wants to automate and remote control activities on Corporate Memory.
