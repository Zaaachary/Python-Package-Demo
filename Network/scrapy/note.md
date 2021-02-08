# Note.md

记录

## Docs

![clipboard.png](https://i.loli.net/2020/12/17/ldob3KFjC6Mxq8a.png)

1.  **引擎**(Scrapy): 用来处理整个系统的数据流处理, 触发事务(框架核心)。
2.  **调度器(**Scheduler): 用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址。
3.  **下载器** (Downloader): 用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)。
4.  **爬虫**(Spiders): 爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面。
5.  **项目管道**(Pipeline): 负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。
6.  **下载器中间件**(Downloader Middlewares): 位于Scrapy引擎和下载器之间的框架，主要是处理Scrapy引擎与下载器之间的请求及响应。
7.  **爬虫中间件**(Spider Middlewares): 介于Scrapy引擎和爬虫之间的框架，主要工作是处理蜘蛛的响应输入和请求输出。
8.  **调度中间件**(Scheduler Middewares): 介于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应。



## Questions

1. 为 scrapy 添加headers
```python
class BaikeSpider(scrapy.Spider):
    name = 'Baike'

    def start_requests(self):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
            }
        urls = [
            "https://baike.baidu.com/item/武大靖",
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)
```

2. `settings.py` 设置

    - 解决 `robot.txt` 限制: `ROBOTSTXT_OBEY = False`
    - 输出时候编码: `FEED_EXPROT_ENCODING='UTF-8'`