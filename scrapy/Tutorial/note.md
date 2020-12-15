# Tutorial

This tutorial will walk you through these tasks:

1. Creating a new Scrapy project

2. Writing a spider to crawl a site and extract data

3. Exporting the scraped data using the command line

4. Changing spider to recursively follow links

5. Using spider arguments

## 创建项目

`scrapy startproject tutorial`

```
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

## 第一个爬虫
`spiders/qutes_spider.py`

运行：到项目顶层 `scrapy crawl quotes`

可以不定义`start_requests`函数，改为定义`start_urls`列表。

### 提取数据

通过 `Scrapy shell` 来尝试选择器 `scrapy shell 'url' `

- `response.css('title')` 返回一个类似列表的对象。

- `response.css('title::text').getall()` 提取文本，`title::text` 限定了只要文本不要tag，返回的是一个列表。 `get()` 返回第一个结果。

使用正则

```shell
>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']
```

`view(response)` 用浏览器查看

### XPath: a brief intro

`response.xpath('//title')`

`response.xpath('//title/text()').get()`

[xpath](https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors)
[xpath example](http://zvon.org/comp/r/tut-XPath_1.html)

### 提取 quotes 和 authors

`<div class='quote'></div>`  -> `response.css('div.quote')`

```shell
>>> text = quote.css("span.text::text").get()
>>> text
'“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
>>> author = quote.css("small.author::text").get()
>>> author
'Albert Einstein'

>>> tags = quote.css("div.tags a.tag::text").getall()
>>> tags
['change', 'deep-thoughts', 'thinking', 'world']
```

```python
for quote in response.css('div.quote'):
    text = quote.css("span.text::text").get()
    author = quote.css("small.author::text").get()
    tags = quote.css("div.tags a.tag::text").getall()
    print(dict(text=text, author=author, tags=tags))
```

### 在爬虫中提取数据

`parse` 中写 for

## 存储数据
`scrapy crawl quotes -O quotes.json`

`scrapy crawl quotes -O quotes.jl` stream like 可以直接增加新的记录，可以用 `jq` 来处理 [jq](https://stedolan.github.io/jq/)

> In small projects (like the one in this tutorial), that should be enough. However, if you want to perform more complex things with the scraped items, you can write an Item Pipeline. A placeholder file for Item Pipelines has been set up for you when the project is created, in tutorial/pipelines.py. Though you don’t need to implement any item pipelines if you just want to store the scraped items.

### Following links

pagination example

`yield scrapy.Request(next_page, callback=self.parse)`
What you see here is Scrapy’s mechanism of following links: when you yield a Request in a callback method, Scrapy will schedule that request to be sent and register a callback method to be executed when that request finishes.

yield Request instance

`response.follow`

`anchors = response.css('ul.pager a')`

`yield from response.follow_all(anchors, callback=self.parse)`

`yield from response.follow_all(css='ul.pager a', callback=self.parse)`


