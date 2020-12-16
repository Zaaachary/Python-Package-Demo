# 查询ip或者域名归属地的程序
# http://m.ip138.com/ip.asp
# http://m.ip138.com/ip.asp?ip=www.zrawberry.com

import requests
url = "http://m.ip138.com/ip.asp"
test_ip ="www.baidu.com"

try:
    kv = {"ip": test_ip}
    r = requests.get(url, params=kv, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.headers)
    print(r.text[-500:-200])
except Exception as e:
    print("爬取失败", Exception.mro())

