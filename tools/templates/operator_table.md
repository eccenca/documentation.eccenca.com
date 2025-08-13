|         Name | Description              |
|-------------:|:-------------------------|
{% for plugin in plugins if not plugin.is_deprecated %} | [{{plugin.title}}]({{plugin.pluginId}}.md) | {{plugin.description}} |
{% endfor %}
