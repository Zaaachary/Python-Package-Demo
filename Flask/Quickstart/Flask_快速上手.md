# Flask 快速上手

[TOC]

## 1 一个最小的应用
运行应用

```shell
Linux
$ export FLASK_APP=hello.py
$ flask run

windows
- cmd
> set FLASK_APP=hello.py
> python -m flask run

> python -m flask run --host=0.0.0.0   # 监听所有公开的IP
```

## 2 调试模式

```
$ export FLASK_ENV=development
> set FLASK_ENV=development
```

## 3 路由

e.g. `@app.route('/path/<path:subpath>')`

| `<type:name>`| info |
|-|-|
|string | 缺省，不含斜杠|
|int| |
| float | |
| path | 类似 string 但可包含斜杠|
| uuid| UUID字符串|

`/projects/` 和 `/about`：最后 `/` 有无

### URL 构建

`url_for()` 函数用于构建指定函数的 URL。它把函数名称作为第一个 参数。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。未知变量 将添加到 URL 中作为查询参数。
`test_request_context`

### HTTP 方法
`@app.route('/login', methods=['GET', 'POST'])`
在函数中可以用 `request.method` 来判断请求方式

## 4 静态文件

在包或者模块旁边创建一个名为`static`的文件夹即可。

## 5 渲染模板

`render_template()` 方法可渲染模板，仅需要提供名称和参数传递。

Flask 会在 `templates` 文件夹内寻找模板。因此，如果你的应用是一个模块， 那么模板文件夹应该在模块旁边；如果是一个包，那么就应该在包里面：

-   一个模块

```shell
/application.py
/templates
	/hello.html
```

-   一个包

```python
/application
	/__init__.py
	/templates
		/hello.html
```

在模板内部可以和访问 [`get_flashed_messages()`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.get_flashed_messages) 函数一样访问 [`request`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.request) 、 [`session`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.session) 和 [`g`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.g) 对象。

g对象：它是某个可以根据需要储存信息的 东西

 [模板继承](https://dormousehole.readthedocs.io/en/latest/patterns/templateinheritance.html#template-inheritance) 

自动转义默认开启。因此，如果 `name` 包含 HTML ，那么会被自动转义。如果你可以 信任某个变量，且知道它是安全的 HTML （例如变量来自一个把 wiki 标记转换为 HTML 的模块），那么可以使用 [`Markup`](https://jinja.palletsprojects.com/en/2.10.x/api/#jinja2.Markup) 类把它标记为安全的，或者在模板 中使用 `|safe` 过滤器。更多例子参见 Jinja 2 文档。

[`Markup`](https://jinja.palletsprojects.com/en/2.10.x/api/#jinja2.Markup) 类的基本使用方法:

```shell
>>> from flask import Markup
>>> Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

>>> Markup.escape('<blink>hacker</blink>')		# 
Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')

>>> Markup('<em>Marked up</em> &raquo; HTML').striptags()
u'Marked up \xbb HTML'
```



## 6 操作请求数据

[link](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id14)

## 7 重定向和错误

## 8 关于响应

## 9 会话

## 10 消息闪现

## 11 日志

## 12 集成 WSGI 中间件

## 13 使用 Flask 扩展

## 14 部署到网络服务器