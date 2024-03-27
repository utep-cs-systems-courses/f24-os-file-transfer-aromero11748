#! /usr/bin/env python3

import socket, sys, re, os
sys.path.append("../lib")
#import params

#HOST = '127.0.0.1'  # Localhost
port = 50001        # Port number
listenAddr = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, port))
s.listen(1) #only allows 1 outstanding request

conn, addr = s.accept() #accepts incoming requests
print('connected to: ', addr)

while 1:
    data = conn.recv(1024).decode()
    if len(data) == 0:
        print('data is empty leaving loop')
        break
    sentData = ('Hello from server').encode()
    print('From client: %s' % data)

    #if we want to send a message
    while len(sentData):
        numBytes = conn.send(sentData)
        sentData = sentData[numBytes:0]
        
#once done
conn.shutdown(socket.SHUT_WR)
conn.close()
