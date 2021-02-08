#! -*- encoding:utf-8 -*-
"""
@File    :   __init__.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   

# Linux
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run

# Windows
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
"""


import os

from flask import Flask


def create_app(test_config=None):
    # 工厂函数
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)        # 创建实例, 告知的是相对路径, 实例文件夹在flasker外
    app.config.from_mapping(                                    # 应用的缺省配置
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)        # 使用 config.py 中的值重载缺省值
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)                    # 使用传入的 测试配置

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db, auth, blog
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)     # 没有 url_prefix
    app.add_url_rule('/', endpoint='index') # url_for('index) == url_for('blog.index')


    return app