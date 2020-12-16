# UniversityRanking.py

'''
功能描述：
    输入：大学排名url链接
    输出：大学排名信息的屏幕输出（排名，大学名称，总分）
    技术路线：requests -> bs4
    定向爬虫：仅针对输入URL进行爬取，不扩展爬取

程序结构设计：
    1. 获取大学排名网页内容   get_html_content()
    2. 提取网页内容中信息到合适的数据结构    fillUnivList()
    3. 利用数据结构展示并输出结果    printUnivList()

'''
import bs4
import requests
from bs4 import BeautifulSoup


def save_html(url):
    pass


def get_htmltext(url):
    try:
        r = requests.request('GET', url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("爬取失败")
        return "error"


def fillUnivList(ulist, html):
    # 将页面放到一个list中
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


# 将ulist中的东西打印出来 num是数量
def printUnivList(ulist, num):
    tplt = "{0:{3}^6}\t{1:{3}^10}\t{2:^6}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    print("Suc" + str(num))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    print("有人的地方就有江湖\n有大学的地方就有排名\n")
    html = get_htmltext(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 30)    # 20 univs
    print("数据使用python爬取自", url)

main()
while eval(input("输入0结束")) != 0:
    pass

