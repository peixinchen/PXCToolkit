TABLE_NAME = '{{ table_name }}'

FIELDS = [
    {%- for field in fields %}
    ('{{ field["name"] }}', {{ field["column"] }}),
    {%- endfor %}
]
