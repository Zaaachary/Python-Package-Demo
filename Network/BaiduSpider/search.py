# https://github.com/BaiduSpider/BaiduSpider

# 导入BaiduSpider
from baiduspider import BaiduSpider
from pprint import pprint

# 实例化BaiduSpider
spider = BaiduSpider()

# 搜索网页
result = spider.search_web(query='武大靖')  # dict
f = open('result.txt', 'w', encoding='utf-8')
pprint(result, f, indent=4)
f.close()

# 搜索咨询
try:
    result = spider.search_news(query='武大靖', pn=5)
except AttributeError as exp:
    print('get None')
else:
    f = open('result2.txt', 'w', encoding='utf-8')
    pprint(result, f, indent=4)
    f.close()
