"""
一个HTTP Web服务器，他知道如何运行服务器端的CGI脚本
从当前工作目录提供文本和脚本
python脚本必须存储再 webdir\cgi-bin或webdir\htbin中
"""
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'   # 存放HTML文件和cgi-bin脚本文件夹的所在
port = 8848     # 缺省http://localhost:xxx/

os.chdir(webdir)                # 在HTML根目录中运行
srvradder = ("", port)          # 主机名和端口号
srvrobj = HTTPServer(srvradder, CGIHTTPRequestHandler)
srvrobj.serve_forever()         # 以永久地守护进程运行