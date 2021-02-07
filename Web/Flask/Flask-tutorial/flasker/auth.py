import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flasker.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')        # 参数2告诉蓝图对象在何处定义



@bp.route('/register', methods=['GET', 'POST']) # 关联 url "/auth/register"
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        # 判断是否合法（有名字、密码、未使用）
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        # 合法则插入
        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))        # 将密码转成哈希值
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)    # 验证失败提示，flash存储渲染模板时可调用的信息

    return render_template('auth/register.html')    # 用户最初范访问的时候返回

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        # 查询用户
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            # 比较密码
            error = 'Incorrect password.'

        # 存储用户的 id 到 session
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request                  # 在视图函数之前运行的函数
def load_logged_in_user():
    '''检查用户id是否已经存储在session'''
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

def login_required(view):
    '''定义一个装饰器，可在其他视图中验证'''
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view