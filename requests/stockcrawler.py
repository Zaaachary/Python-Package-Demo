# stockcrawler.py
"""
东方财富网获取股票列表     http://quote.eastmoney.com/stocklist.html
百度股市通查询个股信息     https://gupiao.baidu.com/stock/sz002132.html
"""
import requests
from bs4 import BeautifulSoup
import traceback
import re


def get_html_text(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def get_stock_list(lst, stockURL):
    html = get_html_text(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

def get_stock_info(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = get_html_text(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock_bets'})

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.txet.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst)))
        except:
            traceback.print_exc()
            continue


if __name__ == '__main__':
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_path = 'BaiduStockInfo.txt'
    slist = []
    get_stock_list(slist, stock_list_url)
    print(slist)
    get_stock_info(slist, stock_info_url, output_path)
