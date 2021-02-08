# 网络图片的爬取与储存
import requests
import os
url = "http://photocdn.sohu.com/20110818/Img316628690.jpg"
root = "D://Project//Python//bee"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except Exception as e:
    print("爬取失败", Exception)
