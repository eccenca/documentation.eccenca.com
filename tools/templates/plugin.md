---
title: "{{plugin.title | replace('"', "'") }}"
description: "{{plugin.description | replace('"', "'") }}"
icon: octicons/cross-reference-24
tags: {% for tag in plugin.tags %}
    - {{tag}}{% endfor %}
---
# {{plugin.title}}
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

{% if plugin.backendType == "python" -%}
!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.
{%- endif %}

{{ plugin.markdownDocumentation if plugin.markdownDocumentation else plugin.description }}

## Parameter

{{parameters if plugin.properties else "`None`"}}

## Advanced Parameter

{{parameters_advanced if plugin.properties_advanced else "`None`"}}
