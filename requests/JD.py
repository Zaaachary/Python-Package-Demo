import requests as rqs


def get_htmltext(url):
    try:
        r = rqs.get(url, timeout=30,headers={'user-agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常,爬取失败"



if __name__ == "__main__":
    url = "https://item.jd.com/5537833.html"
    print(get_htmltext(url))