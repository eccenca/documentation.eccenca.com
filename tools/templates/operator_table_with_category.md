|                                                    Name |                                                Category                                                 | Description              |
|--------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|:-------------------------|
{% for plugin in plugins if not plugin.is_deprecated %} | [{{plugin.title}}]({{plugin.main_category + "/" if plugin.main_category else ""}}{{plugin.pluginId}}.md) | {{plugin.main_category}} | {{plugin.description}} |
{% endfor %}
