### {{property.title}}

{{property.description}}

{% if property.parameterType != "objectParameter" -%}- ID: `{{property.name}}`
- Datatype: `{{property.parameterType}}`
{% if property.value and '\n' in property.value -%}- Default Value:
``` {{ property.get_pygments_code() }}
{{ property.value }}
```
{%- else %}- Default Value: `{{property.value if property.value != "" else "None"}}`
{%- endif %}{%- endif %}

{% for sub_property in property.properties.values() %}
#### {{sub_property.title}}

{{sub_property.description}}

- ID: `{{property.name}}.{{sub_property.name}}`
- Datatype: `{{sub_property.parameterType}}`
{% if sub_property.value and '\n' in sub_property.value -%}- Default Value:
``` {{ sub_property.get_pygments_code() }}
{{ sub_property.value }}
```
{%- else %}- Default Value: `{{sub_property.value if sub_property.value != "" else "None"}}`
{%- endif %}

{% endfor %}
