#! -*- encoding:utf-8 -*-
"""
@File    :   url_for.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   
"""
from flask import Flask, escape, url_for, request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # return do_the_login() 
        pass
    else:
        # reutrn show_the_login_form()
        pass

@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)} \'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    # 静态文件
    print(url_for('static', filename='style.css'))  # 对应位置 static/style.css



# 渲染模板
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)