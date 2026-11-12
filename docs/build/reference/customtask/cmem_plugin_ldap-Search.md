---
title: "Search LDAP directory"
description: "Query LDAP directory services such as OpenLDAP or Active Directory."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Search LDAP directory

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Searches a directory server over LDAP and returns each matching entry as an entity. It works with
any LDAPv3 directory, among them OpenLDAP, Active Directory and Apple Open Directory.

## What the task produces

The task consumes nothing and produces one entity per directory entry. Each entity carries the
distinguished name of the entry as its first value, followed by the values of the requested
attributes, in the order they were requested.

A search is normally followed by a transformation which maps the entries into a Knowledge Graph,
with the distinguished name serving as the stable identifier of a person, group or device.

## How an entry is identified

The URI of an entity is the LDAP URL of the entry as defined by RFC 4516, built from the URL of
the directory and the percent-encoded distinguished name:

```text
ldaps://directory.example.org/uid%3Djdoe%2Cou%3Dpeople%2Cdc%3Dexample%2Cdc%3Dorg
```

Such a URI stays the same between runs and identifies the entry on its own directory, so two
directories holding the same distinguished name do not collide. The distinguished name is also
available as an ordinary value, which is what a mapping usually builds its own identifier from.

## How values are returned

An LDAP attribute may hold several values, and all of them are returned. An attribute an entry
does not carry produces no value at all, which keeps it distinguishable from an attribute that is
present and empty.

Values arrive in the lexical form a Knowledge Graph expects: timestamps as ISO 8601 dates,
booleans as `true` and `false`, numbers in decimal. A value which is not text - `jpegPhoto`,
`objectSid`, `objectGUID` or `userCertificate`, for instance - is Base64 encoded.

This works because the schema of the directory is read while connecting, at the cost of one
request. A directory sends every value as text, and only its schema says which of them is a
timestamp, a boolean or a number.

## Naming the attributes

The attributes have to be named one by one. `*` and `+` are rejected, because the entities are
described to the workflow while it is being drawn, and a wildcard is only resolved by the
directory once the search runs - there would be nothing to connect the next task to.

Directories differ in what they call the same thing. A person's login is `uid` on OpenLDAP and
`sAMAccountName` on Active Directory, and group membership is `memberOf` on Active Directory but
often `isMemberOf` elsewhere, so an attribute list is rarely portable between directories.

## Searching large directories

Searching is always paged, so a result set is not cut short by the maximum result size of the
directory, which is 1000 entries on a default Active Directory installation. A search which
reaches the configured maximum number of entries stops there and reports a warning saying so, and
a search which exceeds the configured time ends with an error from the directory.

References to other directory servers are not followed unless this is asked for. Following one
opens a new, anonymous connection to a server named by the directory rather than by this task,
which commonly fails or stalls; Active Directory returns such a reference for every search below
the root of a domain.

## Connecting securely

An `ldaps://` URL is encrypted from the start, and an `ldap://` URL can be upgraded before
authenticating where the directory offers no separate encrypted port. Certificates are validated
in both cases. Where the directory uses an internal certificate authority, configure that
authority rather than switching validation off - a connection which accepts any certificate also
accepts one presented by a machine in the middle, and the bind password is sent to it.

Leaving both the bind name and the password empty binds anonymously, which many directories allow
for a limited part of their data.

## Example searches

All people who have a mail address, below one organizational unit:

```text
(&(objectClass=person)(mail=*))
```

The enabled users of an Active Directory, without the disabled ones:

```text
(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))
```

The members of one group, read from the group entry itself with a base scope:

```text
(objectClass=groupOfNames)
```


## Parameter

### LDAP URL

The URL of the directory server, e.g. `ldaps://directory.example.org:636`. Use `ldaps://` for an encrypted connection (port 636 by default), or `ldap://` for an unencrypted one (port 389 by default), which can be upgraded with the StartTLS parameter.

- ID: `ldap_url`
- Datatype: `string`
- Default Value: `None`



### Bind DN

The distinguished name used to authenticate, e.g. `cn=reader,ou=services,dc=example,dc=org`. Leave empty together with the password to bind anonymously.

- ID: `bind_dn`
- Datatype: `string`
- Default Value: `None`



### Bind password

The password of the bind DN. Leave empty together with the bind DN to bind anonymously.

- ID: `bind_password`
- Datatype: `password`
- Default Value: `None`



### Search base

The distinguished name the search starts at, e.g. `ou=people,dc=example,dc=org`. An empty value is only accepted by directories which allow a search over all naming contexts.

- ID: `base_dn`
- Datatype: `string`
- Default Value: `None`



### Search filter

The LDAP filter which selects the entries, in the string representation of RFC 4515, e.g. `(&(objectClass=person)(mail=*))`.

- ID: `search_filter`
- Datatype: `multiline string`
- Default Value: `(objectClass=*)`



### Scope

How far below the search base the directory is searched.

- ID: `scope`
- Datatype: `string`
- Default Value: `SUBTREE`



### Attributes

The attributes to return, as a comma-separated list, e.g. `cn, mail, memberOf`. Each attribute becomes one value of the produced entities, in the order given here. `*` and `+` are not accepted.

- ID: `attributes`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### Use StartTLS

If enabled, an `ldap://` connection is upgraded to an encrypted one before authenticating. Enable this where the directory offers encryption on the unencrypted port instead of a separate `ldaps://` endpoint. It cannot be combined with an `ldaps://` URL, which is encrypted already.

- ID: `start_tls`
- Datatype: `boolean`
- Default Value: `false`



### Verify certificates

If enabled, the certificate of the directory server is validated against the trusted certificate authorities. Disabling this accepts any certificate, including one presented by a machine-in-the-middle, and sends the bind password to it. Where the directory uses a private certificate authority, provide that authority below instead of disabling validation.

- ID: `verify_certificates`
- Datatype: `boolean`
- Default Value: `true`



### Certificate authority

The certificate authority which issued the certificate of the directory server, in PEM format. Needed only when that authority is not among the trusted ones, which is the usual case for a directory with an internal certificate authority.

- ID: `ca_certificate`
- Datatype: `multiline string`
- Default Value: `None`



### Follow referrals

If enabled, references to other directory servers are followed. A referral is followed with a new, anonymous connection to a server named by the directory rather than by this task, which commonly fails or stalls. Enable it only for a directory whose data is genuinely partitioned across servers.

- ID: `follow_referrals`
- Datatype: `boolean`
- Default Value: `false`



### Page size

How many entries are fetched from the directory per request. This does not limit the number of entries returned overall, only how often the task talks to the directory while collecting them.

- ID: `page_size`
- Datatype: `Long`
- Default Value: `500`



### Maximum entries

The maximum number of entries to return, or 0 for no limit. When a search reaches this number, it stops and reports a warning, so that a subtree search over a large directory cannot fill a workflow unnoticed.

- ID: `size_limit`
- Datatype: `Long`
- Default Value: `0`



### Time limit

How many seconds the directory may spend on the search, or 0 to leave the decision to the directory.

- ID: `time_limit`
- Datatype: `Long`
- Default Value: `0`
