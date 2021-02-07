import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def init_app(app):
    """在应用实例中注册"""
    app.teardown_appcontext(close_db)       # 在返回响应后进行清理的时候调用此函数
    app.cli.add_command(init_db_command)    # 添加一个新的 可以与 flask 一起工作的命令 e.g. flask init-db

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    # 打开一个文件，该文件名是相对于 flaskr 的
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

"""
Note
g 是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存 可能多个函数都会用到的数据。把连接储存于其中，可以多次使用，而不用在同一个 请求中每次调用 get_db 时都创建一个新的连接。
"""