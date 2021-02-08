# 先睹为快
programming python 第一章的代码
## 此前的章节
- dump_db_classes

## OOP
- person_start
- person
- manager
- person_alternative
- make_db_classes
- update_db_classes
## 增加控制台交互
- peopleinteract_query
- peopleinteract_update
## 增加 GUI
- tkinter001
- tkinter101
- tkinter102OOP
- attachgui
- tkinter103
- peoplegui
- peoplegui_02
- peoplegui--old
- peoplegui--frame
## 增加web界面
- cgi101.html
- cgi-bin/cgi101.py
- webserver.py
- peoplecgi.html
- cgi-bin/peoplecgi.py

'http://localhost:8848/cgi-bin/cgi101.py?user=Sue+Smith'

```
from urllib.request import urlopen
conn = urlopen('http://localhost:8848/cgi-bin/cgi101.py?user=Zachary+Lee')
reply = conn.read()
reply

urlopen('http://localhost:8848/cgi-bin/cgi101.py').read()
```
