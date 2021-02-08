# WebUrlOpen.py
# coding = utf-8
import urllib.request

# simple example
url = "http://www.zrawberry.com"
# res = urllib.request.urlopen(url)
# print(res.read())

# save webpage
content = urllib.request.urlopen(url)       # content 为一个URL对象
print("http header:",content.info())        # 服务器返回的头信息
print("http status:",content.getcode())     # 返回 http 状态码
print("url:",content.geturl())              # 返回请求的url

i=0
print("content:")
for line in content.readlines():
    #print(line)
    print(line.decode('utf-8'))             # 打印网页内容 用utf-8解码
    i=i+1
    if i>30:                                # 只显示30行
        break