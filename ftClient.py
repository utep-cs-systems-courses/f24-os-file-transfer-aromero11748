#! /usr/bin/env python3

import socket, sys, re, os
sys.path.append("../lib")
#import params
serverHost = '127.0.0.1'
serverPort = 50001
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print('creating socket: af=%d, type=%d, proto=%d' % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)

    except socket.error as msg:
        print(msg)
        s = None
        continue

    try:
        print('connecting to : %s' % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(msg)
        s.close()
        s = None
        continue
    break

if s == None:
    print('Could not connect to socket')
    sys.exit(1)

sentData = "here goes the frammed file".encode()

while len(sentData):
    sentBytes = os.write(s.fileno(), sentData)
    print('remaining data: %s' % sentData.decode())
    sentData = sentData[sentBytes:]
s.shutdown(socket.SHUT_WR)

while 1:
    recievedData = os.read(s.fileno(), 1024).decode()
    print('before recievedDATA')
    print(recievedData)
    if len(recievedData) < 1:
        break

s.close()
    
