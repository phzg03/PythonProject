from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # use SO_DGRAM to change to UDP
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

print(tcpSerSock.getsockname())

while True:
    print('waitting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data = ctime() + " : " + data.decode('utf-8')
        print('message from %s : %s'%(addr,data))
        redata = input('some message to >')
        tcpCliSock.send(redata.encode('utf-8'))
    tcpCliSock.close()

tcpSerSock.close()