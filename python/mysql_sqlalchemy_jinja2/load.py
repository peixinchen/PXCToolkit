import re
from jinja2 import Environment, FileSystemLoader 
from engine import engine


def load_fields(conn, table_name):
    fields = []

    result = conn.execute('SHOW COLUMNS FROM `{}`'.format(table_name))
    for i, (column, *unused) in enumerate(result):
        fields.append({
            'name': column,
            'column': i,
        })

    return fields


def fetch_all_tables(conn):
    pattern = re.compile(r'^tp_v2_user_.+')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('templates/template.py')

    result = conn.execute('SHOW TABLES')
    for table_name, *unused in result:
        if not (pattern.match(table_name) 
            and table_name not in ('tp_v2_user_wxinfo', 'tp_v2_user_basic')):
            continue

        fields = load_fields(conn, table_name)

        content = template.render(table_name=table_name, fields=fields)
        name = table_name[11:]
        with open('output/{}.py'.format(name), 'w') as fp:
            fp.write(content)


with engine.connect() as conn:
    fetch_all_tables(conn)
