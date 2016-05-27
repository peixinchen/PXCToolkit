import os


DB = dict(
    driver='mysql',
    host=os.environ.get('MYSQL_HOST', 'localhost'),
    port=os.environ.get('MYSQL_PORT', '3306'),
    user=os.environ.get('MYSQL_USER', 'root'),
    password=os.environ.get('MYSQL_PASSWORD', 'password'),
    instance=os.environ.get('MYSQL_INSTANCE', 'instance'),
)
