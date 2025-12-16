---
title: "Fix URI"
description: "Generates valid absolute URIs from the given values. Already valid absolute URIs are left untouched."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Fix URI
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Generates valid absolute URIs from the given values. Already valid absolute URIs are left untouched.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Non-absolute URIs are prefixed with the configured URI prefix:**

* Input values:
    1. `[ab]`

* Returns: `[urn:url-encoded-value:ab]`

---
**URI reserved characters are encoded:**

* Input values:
    1. `[a&b]`

* Returns: `[urn:url-encoded-value:a%26b]`

---
**Valid absolute URIs are forwarded unchanged:**

* Input values:
    1. `[http://example.org/some/path]`

* Returns: `[http://example.org/some/path]`

---
**Query parameters and fragments are left unchanged:**

* Input values:
    1. `[http://example.org/path?query=some+stuff#hashtag]`

* Returns: `[http://example.org/path?query=some+stuff#hashtag]`

---
**Valid URNs are forwarded unchanged:**

* Input values:
    1. `[urn:valid:uri]`

* Returns: `[urn:valid:uri]`

---
**Special characters are encoded:**

* Input values:
    1. `[http://www.broken domain.com/broken weird path äöü/nice/path/andNowSomeFragment#fragmentäöü]`

* Returns: `[http://www.broken%20domain.com/broken%20weird%20path%20%C3%A4%C3%B6%C3%BC/nice/path/andNowSomeFragment#fragment%C3%A4%C3%B6%C3%BC]`

---
**Hash signs are only encoded if they don't denote a fragment:**

* Input values:
    1. `[http://domain/##path#]`

* Returns: `[http://domain/#%23path%23]`

---
**Invalid URIs are fully encoded:**

* Input values:
    1. `[http : invalid URI]`

* Returns: `[urn:url-encoded-value:http+%3A+invalid+URI]`

---
**Leading and trailing spaces are removed:**

* Input values:
    1. `[  http://domain.com/[squareBrackets] ]`

* Returns: `[http://domain.com/%5BsquareBrackets%5D]`

---
**Example 10:**

* Input values:
    1. `[100%]`

* Returns: `[urn:url-encoded-value:100%25]`

## Parameter

### Uri prefix

No description

* ID: `uriPrefix`
* Datatype: `string`
* Default Value: `urn:url-encoded-value:`

## Advanced Parameter

`None`
