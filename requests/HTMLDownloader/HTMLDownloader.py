# coding=utf-8
# 一个下载网页的程序
import requests as rqs
import re
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}


def get_html(url):
    try:
        r = rqs.get(url, timeout=30, header=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text, r.content
    except Exception as e:
        return "none", "html 获取失败"


def get_title(text):
    pattern = r'<title>.*</title>'
    try:
        m = re.search(pattern, text)
        title = m.group(0).split("<title>")[1].split("</title>")[0]
    except Exception as e:
        title = 'TitleNoFound'

    return title


def save_html(title , content):
    root = 'webpage/'
    path = root + '/' + title + '.html'
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)
            print("文件保存成功")
    else:
        print("文件已经存在")


if __name__ == '__main__':
    url = input("请输入要下载的网址")
    # url = "http://www.baidu.com"
    text, content = get_html(url)
    title = get_title(text)
    save_html(title, content)

