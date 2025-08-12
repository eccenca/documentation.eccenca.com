---
title: "{{plugin.title}}"
description: "{{plugin.description}}"
icon: octicons/cross-reference-24
tags: {% for tag in plugin.tags %}
    - {{tag}}{% endfor %}
---
# {{plugin.title}}
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

{% if plugin.is_python -%}
!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).
{%- endif %}

{{ plugin.markdownDocumentation if plugin.markdownDocumentation else plugin.description }}

## Parameter

{{parameters if plugin.properties else "`None`"}}
