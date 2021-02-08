# TCP_Server.py
from socket import *        
from time import ctime      # 引入ctime函数

HOST = '127.0.0.1'          # 绑定的IP
PORT = 4700                 # 端口号
BUFSIZ = 1024               # 缓冲大小
ADDR = (HOST,PORT)

ss = socket(AF_INET,SOCK_STREAM,0)  # 服务器套接字
ss.bind(ADDR)                       # 套接字绑定IP
ss.listen(20)                       # 最大连接数为20

while True:
    print('等待客户端连接...\r\n')
    cs,caddr = ss.accept()                   # cs客户端套接字 caddr 客户端地址
    print('...连接来自:',caddr)

    data = '欢迎你的到来！\r\n'
    cs.sendall(bytes(data,'UTF-8'))          # 向客户端发送欢迎信息
    data = cs.recv(BUFSIZ).decode('UTF-8')   # 接收客户端发送的信息
    if not data:
        break
    data = '[%s] %s\r\n'%(ctime(),data)
    cs.sendall(bytes(data,'UTF-8'))          # 向客户端发送新的信息
    print(data)
    cs.close()                               # 关闭客户端套接字

ss.close()                          # 关闭服务端的套接字
