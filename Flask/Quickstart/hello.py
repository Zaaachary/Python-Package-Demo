#! -*- encoding:utf-8 -*-
"""
@File    :   hello.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   
"""
import pdb
from flask import Flask, escape

app = Flask(__name__)       # 应用模块或包名

@app.route('/')
def index():
    return "Index Page\n <a href='/hello'>Hello</a>"

# ====路由====
@app.route('/hello')        # 路由 为函数绑定 url
def hello_world():
    return 'Hello, Flask!'

@app.route('/user/<username>')          # 默认string, 接收不包含斜杠的文本
def show_user_profile(username):
    # show the user profile for that user, e.g.  /user/zachary
    # pdb.set_trace()                   # username  str
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer, e.g. /post/01
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')      # path 类型可以包含斜杠
def show_subpath(subpath):
    # show the subpath after /path/, e.g. /path/path2/22/
    return 'Subpath %s' % escape(subpath)