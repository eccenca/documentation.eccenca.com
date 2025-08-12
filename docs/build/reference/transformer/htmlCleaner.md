---
title: "Clean HTML"
description: "Cleans HTML using a tag white list and allows selection of HTML sections with XPath or CSS selector expressions. If the tag or attribute white lists are left empty default white lists will be used (this behaviour can be changed). To remove all HTML markup and retain text, keep the defaults and turn off the "Default tags and attributes" toggle. The operator takes two inputs: the page HTML and (optional) the page Url which may be needed to resolve relative links in the page HTML."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Clean HTML
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Cleans HTML using a tag white list and allows selection of HTML sections with XPath or CSS selector expressions. If the tag or attribute white lists are left empty default white lists will be used (this behaviour can be changed). To remove all HTML markup and retain text, keep the defaults and turn off the "Default tags and attributes" toggle. The operator takes two inputs: the page HTML and (optional) the page Url which may be needed to resolve relative links in the page HTML.

## Parameter

### Tag white list

Tags to keep in the cleaned output.

- Datatype: `traversable[string]`
- Default Value: `None`



### Attribute white list

Attributes to keep in the cleaned output.

- Datatype: `traversable[string]`
- Default Value: `None`



### Selectors

CSS or XPath queries for selection of content. CSS selectors can be pipe separated for non-sequential execution.

- Datatype: `traversable[string]`
- Default Value: `None`



### Method

Selects use of XPath or CSS selectors.

- Datatype: `enumeration`
- Default Value: `xPath`



### Default tags and attributes

Use defaults for empty tag and attribute whitelists. If the attribute while list is empty, it will default to: "class", "id", "href", "src" If the tag while list is empty, it will default to: "a", "b", "blockquote", "br", "caption", "cite", "code", "col", "colgroup", "dd", "div", "dl", "dt", "em", "h1", "h2", "h3", "h4", "h5", "h6","i", "img", "li", "ol", "p", "pre", "q", "small", "span", "strike", "strong","sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul".

- Datatype: `boolean`
- Default Value: `true`



