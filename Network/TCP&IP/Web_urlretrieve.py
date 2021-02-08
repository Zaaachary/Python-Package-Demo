# Web_urlretrieve.py
import urllib.request
content = urllib.request.urlretrieve("http://www.xjtu.edu.cn","xjtu.htm")
print(content)
url="http://www.xa.gov.cn/attached/image/20140704/20140704140040_544_1111927.jpg"
content = urllib.request.urlretrieve(url,"c:\\develop\\python\\xian.jpg")