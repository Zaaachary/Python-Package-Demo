#-*- coding:utf-8 -*-
# CrawTaobaoPrice
import requests
import re


# 获取HTML
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("获取失败", e)
        return ""


# 解析页面
def parsePage(ilt, html):
    # <span class="search_now_price">¥价格</span>
    # r'now_price">&yen;[\d]*\.[\d]*</span>'  -> '"search_now_price">&yen;61.40</span>'
    # <a title="商品名" ddclick="act=normalResult
    # r'<a title=".*?"  ddclick' ->'<a title=" Python编程 从入门到实践"  ddclick'
    try:
        plt = re.findall(r'now_price">&yen;[\d]*\.[\d]*</span>', html)
        tlt = re.findall(r'<a title=".*?"  ddclick', html)
        for i in range(len(plt)):
            price = eval(plt[i].split('&yen;')[1].split('<')[0])
            title = tlt[i].split('"')[1]
            ilt.append([price, title])
    except Exception as e:
        print("解析失败", e)


# 输出产品列表
def printGoodsList(ilt):
    #     tplt = "{0:{3}^6}\t{1:{3}^10}\t{2:^6}"
    #     print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    template = "{0:{3}<4}\t{1:{3}<8}\t{2:{3}<16}"
    print(template.format("序号", "价格", "商品名", chr(12288)))
    count = 0
    for g in ilt:
        count += 1
        print(template.format(count, g[0], g[1], chr(12288)))


if __name__ == '__main__':
    print("当当网商品列表爬取程序")
    goods = input("请输入商品的关键词，如'机器学习':")
    depth = 2
    # python&page_index=1
    start_url = 'http://search.dangdang.com/?key=' + goods
    infoList = []
    for i in range(1):
        try:
            url = start_url + '&page_index=' + str(i+1)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except Exception as e:
            print(e)
            continue
        printGoodsList(infoList)
    input("输入任意键结束")