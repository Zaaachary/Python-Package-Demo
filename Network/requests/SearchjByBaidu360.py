import requests

keyword = "python"
try:
    kv = {'wd': keyword}
    r = requests.request('get', "http://www.baidu.com/s", params=kv)
    r.raise_for_status()
    print(r.request.url)
    print(len(r.text))
except Exception as e:
    print("百度抓取失败:", Exception)

try:
    kv = {'q': keyword}
    r = requests.request('get', "http://www.so.com/s", params=kv)
    r.raise_for_status()
    print(r.request.url)
    print(len(r.text))
except Exception as e:
    print("360抓取失败:", Exception)


# 百度关键词接口：
# http://www.baidu.com/s?wd=keyword
# 360关键词接口：
# http://www.so.com/s?q=keyword