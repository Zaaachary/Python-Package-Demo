# TCP_Client.py
from socket import *

HOST = '127.0.0.1'
PORT = 4700
BUFSIZ = 1024
ADDR = (HOST,PORT)

cs = socket(AF_INET,SOCK_STREAM,0)
cs.connect(ADDR)

data = cs.recv(BUFSIZ).decode('UTF-8')
if data:
    print(data)
data = '草莓君\r\n'

if data:
    cs.sendall(bytes(data,'UTF-8'))
data = cs.recv(BUFSIZ).decode('UTF-8')

if data:
    print(data)

cs.close()