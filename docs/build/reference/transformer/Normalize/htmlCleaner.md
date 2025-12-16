---
title: "Clean HTML"
description: "Cleans HTML markup using a tag whitelist and allows selection of HTML sections with XPath or CSS selector expressions."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Clean HTML
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

This transformer cleans HTML markup using a whitelist of HTML tags.
It allows the selection of HTML sections with XPath or CSS selector expressions.
If the tag or attribute whitelists are left empty, default whitelists will be used. This behaviour can be changed.
To remove all the HTML tags and retain plain text, keep the defaults and turn off the "Default tags and attributes" toggle.
The operator takes two inputs: the page HTML and, optionally, the page URL which may be needed to resolve relative links in the HTML page.

## Parameter

### Tag white list

Tags to keep in the cleaned output.

- ID: `tagWhiteList`
- Datatype: `traversable[string]`
- Default Value: `None`

### Attribute white list

Attributes to keep in the cleaned output.

- ID: `attributeWhiteList`
- Datatype: `traversable[string]`
- Default Value: `None`

### Selectors

CSS or XPath queries for selection of content. CSS selectors can be pipe separated for non-sequential execution.

- ID: `selectors`
- Datatype: `traversable[string]`
- Default Value: `None`

### Method

Selects use of XPath or CSS selectors.

- ID: `method`
- Datatype: `enumeration`
- Default Value: `xPath`

### Default tags and attributes

Use defaults for empty tag and attribute whitelists. If the attribute while list is empty, it will default to: "class", "id", "href", "src" If the tag while list is empty, it will default to: "a", "b", "blockquote", "br", "caption", "cite", "code", "col", "colgroup", "dd", "div", "dl", "dt", "em", "h1", "h2", "h3", "h4", "h5", "h6","i", "img", "li", "ol", "p", "pre", "q", "small", "span", "strike", "strong","sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul".

- ID: `defaultTagsAndAttributes`
- Datatype: `boolean`
- Default Value: `true`

## Advanced Parameter

`None`
