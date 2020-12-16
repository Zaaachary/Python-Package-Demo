# Note.md

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