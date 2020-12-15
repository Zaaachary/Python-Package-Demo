#! -*- encoding:utf-8 -*-
"""
@File    :   a_glance_spider.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   

run>  scrapy runspider a_glance_spider.py -o glance.jl

"""


import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

