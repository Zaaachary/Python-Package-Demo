#! -*- encoding:utf-8 -*-
"""
@File    :   quotes_spider.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   

run>  scrapy runspider quotes_spider.py -o quotes.jl

"""


import scrapy


class PagedownloadSpider(scrapy.Spider):  # spider子类
    name = "quotes"  # unique

    def start_requests(self):
        # 迭代器 生成请求 request
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 可调用的用于处理响应 response
        # 解析响应，提取需要爬取的数据作为一个字典
        # 找到新的 URLs 作为新的 request
        page = response.url.split("/")[-2]      # [..., 'page', '1', '']
        filename = f'quotes-{page}.html'

        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log(f'Saved file {filename}')


